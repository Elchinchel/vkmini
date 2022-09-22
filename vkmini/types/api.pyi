from vkmini.types import methods
from vkmini.api import VkApi as _VkApi


class VkApi(_VkApi):
    account: methods.account
    ads: methods.ads
    adsweb: methods.adsweb
    appWidgets: methods.appWidgets
    apps: methods.apps
    auth: methods.auth
    board: methods.board
    database: methods.database
    docs: methods.docs
    downloadedGames: methods.downloadedGames
    fave: methods.fave
    friends: methods.friends
    gifts: methods.gifts
    groups: methods.groups
    likes: methods.likes
    market: methods.market
    messages: methods.messages
    newsfeed: methods.newsfeed
    notes: methods.notes
    notifications: methods.notifications
    orders: methods.orders
    pages: methods.pages
    photos: methods.photos
    podcasts: methods.podcasts
    polls: methods.polls
    prettyCards: methods.prettyCards
    search: methods.search
    secure: methods.secure
    stats: methods.stats
    status: methods.status
    storage: methods.storage
    stories: methods.stories
    streaming: methods.streaming
    users: methods.users
    utils: methods.utils
    video: methods.video
    wall: methods.wall
    widgets: methods.widgets
