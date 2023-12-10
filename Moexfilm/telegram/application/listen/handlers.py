import logging
from queue import Queue

from pyrogram import Client, filters
from pyrogram.types import Message

from Moexfilm.core.media.application import TmdbService, MovieService, TvShowStoreService, TvShowService
from Moexfilm.core.media.domain.models import MediaType, Movie, Provider, TvShow, Season, Episode
from Moexfilm.core.media.infrastructure import TmdbRepositoryImpl
from Moexfilm.core.media.infrastructure.database import TvShowRepositoryImpl, MovieRepositoryImpl
from Moexfilm.telegram.application.listen.utils import get_type, get_search_params
from Moexfilm.telegram.domain import MessageHeader, MessageMovieHeader, MessageTvShowHeader

headers: Queue = Queue()

tmdb_service = TmdbService(TmdbRepositoryImpl())

movie_service = MovieService(MovieRepositoryImpl())

tv_show_store = TvShowStoreService(TvShowRepositoryImpl())
tv_show_service = TvShowService(TvShowRepositoryImpl())


@Client.on_message()
async def route_handler(_, m: Message):
    if await filters.text_filter(_, None, m):
        await message_header_handler(_, m)
        return
    if await filters.video_filter(_, None, m) or await filters.document_filter(_, None, m):
        await media_handler(_, m)


async def message_header_handler(_, m: Message):
    media_type: MediaType = get_type(m)
    header = None
    if media_type == MediaType.MOVIE:
        header = MessageMovieHeader(m.text)
        logging.info(f"Movie header added: {m.text}) ✅")
    else:
        if media_type == MediaType.TV_SHOW:
            header = MessageTvShowHeader(m.text)
            logging.info(f"Tv show header added: {m.text} ✅")
    if header:
        headers.put(header)


async def media_handler(_, m: Message):
    message_header: MessageHeader = headers.get()

    if not message_header:
        await m.reply_text("Before is needed a header 🤔")
        return

    if isinstance(message_header, MessageMovieHeader):
        movie: Movie = tmdb_service.search_movie(get_search_params(message_header))
        movie.id = m.id
        movie.provider = Provider.TELEGRAM

        movie_service.save_movie(movie)
        logging.info(f"Movie saved: ✨ {movie.title} {movie.provider} ✨")
    else:
        if isinstance(message_header, MessageTvShowHeader):
            params = get_search_params(message_header)
            tv = tv_show_store.get(f"{params.title}#{params.release_date}")
            if tv:
                tv = handle_existing_tv_show(tv, params, m)
            else:
                tv = handle_new_tv_show(params, m)

            tv_show_store.save(tv)


def handle_existing_tv_show(tv, params, message: Message) -> TvShow:
    if not any(int(season.season_number) == int(params.season) for season in tv.seasons):
        season = tmdb_service.search_season(tv.tmdb_id, params.season)
        episode = tmdb_service.search_episode(tv.tmdb_id, params.season, params.episode)
        episode.season_id = season.tmdb_id
        episode.provider = Provider.TELEGRAM
        episode.id = message.id
        season.episodes.append(episode)
        tv_show_service.save_season(season)
        _save_season_log(tv, season)
    else:
        tv = handle_existing_season(tv, params, message)
    return tv


def handle_existing_season(tv, params, message: Message) -> TvShow:
    for season in tv.seasons:
        if season.season_number == params.season and not any(
                int(episode.episode_number) == int(params.episode) for episode in season.episodes):
            episode = tmdb_service.search_episode(tv.tmdb_id, params.season, params.episode)
            episode.season_id = season.tmdb_id
            episode.provider = Provider.TELEGRAM
            episode.id = message.id
            season.episodes.append(episode)
            tv_show_service.save_episode(episode)
            _save_episode_log(tv, season, episode)
            return tv
    return tv


def handle_new_tv_show(params, message: Message) -> TvShow:
    tv = tmdb_service.search_tv_show(params)
    season = tmdb_service.search_season(tv.tmdb_id, params.season)
    season.tv_show_id = tv.tmdb_id
    episode = tmdb_service.search_episode(tv.tmdb_id, params.season, params.episode)
    episode.season_id = season.tmdb_id
    episode.provider = Provider.TELEGRAM
    episode.id = message.id
    season.episodes.append(episode)
    tv.seasons.append(season)
    tv_show_service.save_tv_show(tv)
    _save_tv_show_log(tv)
    return tv


def _save_tv_show_log(tv: TvShow):
    logging.info(f"Tv Show saved: ✨ {tv.title} ({tv.release_date.year}) ✨")

    if tv.seasons:
        for season in tv.seasons:
            _save_season_log(tv, season)


def _save_season_log(tv: TvShow, season: Season):
    logging.info(f"Season saved: ✨ {tv.title} S{season.season_number} ✨")

    if season.episodes:
        for episode in season.episodes:
            _save_episode_log(tv, season, episode)


def _save_episode_log(tv: TvShow, season: Season, episode: Episode):
    logging.info(f"Episode saved: ✨ {tv.title} S{season.season_number}e{episode.episode_number} ✨")
