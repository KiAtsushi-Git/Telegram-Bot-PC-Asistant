from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager


async def get_media_info() -> str | None:
    sessions = await MediaManager.request_async()
    current = sessions.get_current_session()
    if current is not None:
        info = await current.try_get_media_properties_async()
        artist = info.artist
        title = info.title
        if artist and title:
            return f"{artist} — {title}"
    return None