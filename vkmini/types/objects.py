from typing import List, Union, Literal

from typing_extensions import TypeAlias, TypedDict, NotRequired


Flag: TypeAlias = int

vk_ref_enum: TypeAlias = Literal['snippet_im', 'snippet_post']
platforms_enum: TypeAlias = Literal['mobile', 'web', 'mvk']


account_counters_filter: TypeAlias = Literal['app_requests', 'events', 'friends', 'friends_recommendations', 'games', 'gifts', 'groups', 'messages', 'notes', 'notifications', 'photos', 'faves', 'memories']

account_name_request_status: TypeAlias = Literal['success', 'processing', 'declined', 'was_accepted', 'was_declined', 'declined_with_link', 'response', 'response_with_link']  # Request status

account_push_params_mode: TypeAlias = Literal['on', 'off', 'no_sound', 'no_text']  # Settings parameters

account_push_params_onoff: TypeAlias = Literal['on', 'off']  # Settings parameters

account_push_params_settings: TypeAlias = Literal['on', 'off', 'fr_of_fr']  # Settings parameters

address_fields: TypeAlias = Literal['id', 'title', 'address', 'additional_address', 'country_id', 'city_id', 'city', 'metro_station_id', 'metro_station', 'latitude', 'longitude', 'distance', 'work_info_status', 'timetable', 'phone', 'time_offset']

addresses_fields: TypeAlias = Literal['id', 'title', 'address', 'additional_address', 'country_id', 'city_id', 'metro_station_id', 'latitude', 'longitude', 'distance', 'work_info_status', 'timetable', 'phone', 'time_offset']

ads_access_role: TypeAlias = Literal['admin', 'manager', 'reports']  # Current user's role

ads_access_role_public: TypeAlias = Literal['manager', 'reports']  # Current user's role

ads_account_type: TypeAlias = Literal['general', 'agency']  # Account type

ads_ad_approved = Literal[
    0,  # not moderated
    1,  # pending moderation
    2,  # approved
    3  # rejected
]

ads_ad_cost_type = Literal[
    0,  # per clicks
    1,  # per impressions
    2,  # per actions
    3  # per impressions optimized
]

ads_ad_status = Literal[
    0,  # stopped
    1,  # started
    2  # deleted
]

ads_campaign_status = Literal[
    0,  # stopped
    1,  # started
    2  # deleted
]

ads_campaign_type: TypeAlias = Literal['normal', 'vk_apps_managed', 'mobile_apps', 'promoted_posts', 'adaptive_ads', 'stories']  # Campaign type

ads_criteria_sex = Literal[
    '0',  # any
    '1',  # male
    '2'  # female
]

ads_object_type: TypeAlias = Literal['ad', 'campaign', 'client', 'office']  # Object type

ads_ord_client_type: TypeAlias = Literal['person', 'individual', 'legal', 'foreign', 'unknown']

ads_stats_sex_value = Literal[
    'f',  # female
    'm'  # male
]

ads_targ_suggestions_schools_type: TypeAlias = Literal['school', 'university', 'faculty', 'chair']  # School type

apps_app_fields: TypeAlias = Literal['author_group', 'author_id', 'author_url', 'banner_1120', 'banner_560', 'banner_186', 'banner_896', 'icon_16', 'icon_25', 'icon_50', 'icon_100', 'icon_200', 'icon_128', 'icon_256', 'is_new', 'new', 'is_html5_app', 'push_enabled', 'catalog_banner', 'friends', 'catalog_position', 'description', 'genre', 'genre_id', 'international', 'is_in_catalog', 'installed', 'leaderboard_type', 'members_count', 'platform_id', 'published_date', 'screen_name', 'section', 'type', 'id', 'title', 'author_owner_id', 'is_installed', 'icon_139', 'icon_150', 'icon_278', 'icon_576', 'background_loader_color', 'loader_icon', 'icon_75', 'open_in_external_browser', 'ad_config', 'screen_orientation']  # App fields available for response

apps_app_leaderboard_type = Literal[
    0,  # not supported
    1,  # levels
    2  # points
]

apps_app_type: TypeAlias = Literal['app', 'game', 'site', 'standalone', 'vk_app', 'community_app', 'html5_game', 'mini_app']  # Application type

base_bool_int = Literal[
    0,  # no
    1  # yes
]

base_lang = Literal[
    'ru',  # russian
    'ua',  # ukrainian
    'be',  # belarusian
    'en',  # english
    'es',  # spanish
    'fi',  # finnish
    'de',  # german
    'it'  # italian
]

base_link_button_action_type: TypeAlias = Literal['open_url', 'market_clear_recent_queries', 'close_web_app', 'open_search_tab', 'import_contacts', 'add_friends', 'onboarding', 'show_filters']  # Action type

base_link_button_style = Literal[
    'primary',  # primary
    'secondary'  # secondary
]

base_link_product_category: TypeAlias = Union[str, 'market_market_category_nested']

base_link_product_status: TypeAlias = Literal['active', 'blocked', 'sold', 'deleted', 'archived']  # Status representation

base_name_case = Literal[
    'Nom',  # nominative
    'Gen',  # genitive
    'Dat',  # dative
    'Acc',  # accusative
    'Ins',  # instrumental
    'Abl'  # prepositional
]

base_property_exists = Literal[
    1  # Property exists
]

base_sex = Literal[
    0,  # unknown
    1,  # female
    2  # male
]

base_sticker: TypeAlias = 'base_sticker_new'

base_user_group_fields: TypeAlias = Literal['about', 'action_button', 'activities', 'activity', 'addresses', 'admin_level', 'age_limits', 'author_id', 'ban_info', 'bdate', 'blacklisted', 'blacklisted_by_me', 'books', 'can_ban', 'can_create_topic', 'can_message', 'can_post', 'can_see_all_posts', 'can_see_audio', 'can_send_friend_request', 'can_upload_video', 'can_write_private_message', 'career', 'city', 'common_count', 'connections', 'contacts', 'counters', 'cover', 'crop_photo', 'deactivated', 'description', 'domain', 'education', 'exports', 'finish_date', 'fixed_post', 'followers_count', 'friend_status', 'games', 'has_market_app', 'has_mobile', 'has_photo', 'home_town', 'id', 'interests', 'is_admin', 'is_closed', 'is_favorite', 'is_friend', 'is_best_friend', 'is_hidden_from_feed', 'is_member', 'is_messages_blocked', 'can_send_notify', 'is_subscribed', 'last_seen', 'links', 'lists', 'maiden_name', 'main_album_id', 'main_section', 'market', 'member_status', 'members_count', 'military', 'movies', 'music', 'name', 'nickname', 'occupation', 'online', 'online_status', 'personal', 'phone', 'photo_100', 'photo_200', 'photo_200_orig', 'photo_400_orig', 'photo_50', 'photo_id', 'photo_max', 'photo_max_orig', 'photo_avg_color', 'quotes', 'relation', 'relatives', 'schools', 'screen_name', 'sex', 'site', 'start_date', 'status', 'timezone', 'trending', 'tv', 'type', 'universities', 'verified', 'wall_comments', 'wiki_page', 'first_name', 'first_name_acc', 'first_name_dat', 'first_name_gen', 'last_name', 'last_name_acc', 'last_name_dat', 'last_name_gen', 'can_subscribe_stories', 'is_subscribed_stories', 'vk_admin_status', 'can_upload_story', 'clips_count', 'image_status', 'is_nft', 'is_nft_photo', 'is_verified']

board_default_order = Literal[
    1,  # desc_updated
    2,  # desc_created
    -1,  # asc_updated
    -2  # asc_created
]

callback_audio_new: TypeAlias = 'audio_audio'

callback_board_post_edit: TypeAlias = 'board_topic_comment'

callback_board_post_new: TypeAlias = 'board_topic_comment'

callback_board_post_restore: TypeAlias = 'board_topic_comment'

callback_group_join_type: TypeAlias = Literal['join', 'unsure', 'accepted', 'approved', 'request']

callback_group_market = Literal[
    0,  # disabled
    1  # open
]

callback_group_officer_role = Literal[
    0,  # none
    1,  # moderator
    2,  # editor
    3  # administrator
]

callback_photo_new: TypeAlias = 'photos_photo'

callback_type: TypeAlias = Literal['audio_new', 'board_post_new', 'board_post_edit', 'board_post_restore', 'board_post_delete', 'confirmation', 'group_leave', 'group_join', 'group_change_photo', 'group_change_settings', 'group_officers_edit', 'lead_forms_new', 'market_comment_new', 'market_comment_delete', 'market_comment_edit', 'market_comment_restore', 'market_order_new', 'market_order_edit', 'message_new', 'message_reply', 'message_edit', 'message_allow', 'message_deny', 'message_read', 'message_typing_state', 'messages_edit', 'message_reaction_event', 'photo_new', 'photo_comment_new', 'photo_comment_delete', 'photo_comment_edit', 'photo_comment_restore', 'poll_vote_new', 'user_block', 'user_unblock', 'video_new', 'video_comment_new', 'video_comment_delete', 'video_comment_edit', 'video_comment_restore', 'wall_post_new', 'wall_reply_new', 'wall_reply_edit', 'wall_reply_delete', 'wall_reply_restore', 'wall_repost', 'wall_schedule_post_new', 'wall_schedule_post_delete']

callback_video_new: TypeAlias = 'audio_audio'

callback_wall_post_new: TypeAlias = 'wall_wallpost'

callback_wall_reply_edit: TypeAlias = 'wall_wall_comment'

callback_wall_reply_new: TypeAlias = 'wall_wall_comment'

callback_wall_reply_restore: TypeAlias = 'wall_wall_comment'

callback_wall_repost: TypeAlias = 'wall_wallpost'

calls_end_state: TypeAlias = Literal['canceled_by_initiator', 'canceled_by_receiver', 'reached']  # State in which call ended up

database_city_by_id: TypeAlias = 'base_object'

database_school_class: TypeAlias = 'base_object'

docs_doc_attachment_type: TypeAlias = Literal['doc', 'graffiti', 'audio_message']  # Doc attachment type

fave_bookmark_type: TypeAlias = Literal['post', 'video', 'product', 'article', 'link', 'clip']

fave_page_type: TypeAlias = Literal['user', 'group', 'hints']

friends_friend_status_status = Literal[
    0,  # not a friend
    1,  # outcoming request
    2,  # incoming request
    3  # is friend
]

gifts_gift_privacy = Literal[
    0,  # name and message for all
    1,  # name for all
    2  # name and message for recipient only
]

groups_address_work_info_status: TypeAlias = Literal['no_information', 'temporarily_closed', 'always_opened', 'timetable', 'forever_closed']  # Status of information about timetable

groups_ban_info_reason = Literal[
    0,  # other
    1,  # spam
    2,  # verbal abuse
    3,  # strong language
    4  # flood
]

groups_fields: TypeAlias = Literal['id', 'name', 'screen_name', 'is_closed', 'type', 'is_admin', 'admin_level', 'is_member', 'is_advertiser', 'start_date', 'finish_date', 'deactivated', 'photo_50', 'photo_100', 'photo_200', 'photo_200_orig', 'photo_400', 'photo_400_orig', 'photo_max', 'photo_max_orig', 'est_date', 'public_date_label', 'photo_max_size', 'is_video_live_notifications_blocked', 'video_live', 'market', 'member_status', 'is_adult', 'is_hidden_from_feed', 'is_favorite', 'is_subscribed', 'city', 'verified', 'description', 'wiki_page', 'members_count', 'members_count_text', 'requests_count', 'video_live_level', 'video_live_count', 'clips_count', 'textlives_count', 'counters', 'cover', 'can_post', 'can_suggest', 'can_upload_story', 'can_upload_doc', 'can_upload_video', 'can_upload_clip', 'can_see_all_posts', 'can_create_topic', 'activity', 'fixed_post', 'has_photo', 'crop_photo', 'status', 'status_audio', 'main_album_id', 'links', 'contacts', 'wall', 'site', 'main_section', 'secondary_section', 'trending', 'can_message', 'is_messages_blocked', 'can_send_notify', 'online_status', 'invited_by', 'age_limits', 'ban_info', 'has_market_app', 'using_vkpay_market_app', 'has_group_channel', 'addresses', 'is_subscribed_podcasts', 'can_subscribe_podcasts', 'can_subscribe_posts', 'live_covers', 'stories_archive_count', 'has_unseen_stories', 'rating']

groups_filter: TypeAlias = Literal['admin', 'editor', 'moder', 'advertiser', 'groups', 'publics', 'events', 'has_addresses']

groups_group_access = Literal[
    0,  # open
    1,  # closed
    2  # private
]

groups_group_admin_level = Literal[
    1,  # moderator
    2,  # editor
    3  # administrator
]

groups_group_age_limits = Literal[
    1,  # unlimited
    2,  # 16 plus
    3  # 18 plus
]

groups_group_audio = Literal[
    0,  # disabled
    1,  # open
    2  # limited
]

groups_group_docs = Literal[
    0,  # disabled
    1,  # open
    2  # limited
]

groups_group_full_age_limits = Literal[
    1,  # no
    2,  # over 16
    3  # over 18
]

groups_group_full_member_status = Literal[
    0,  # not a member
    1,  # member
    2,  # not sure
    3,  # declined
    4,  # has sent a request
    5  # invited
]

groups_group_full_section = Literal[
    0,  # none
    1,  # photos
    2,  # topics
    3,  # audios
    4,  # videos
    5,  # market
    6,  # stories
    7,  # apps
    8,  # followers
    9,  # links
    10,  # events
    11,  # places
    12,  # contacts
    13,  # app_btns
    14,  # docs
    15,  # event_counters
    16,  # group_messages
    24,  # albums
    26,  # categories
    27,  # admin_help
    31,  # app_widget
    32,  # public_help
    33,  # hs_donation_app
    34,  # hs_market_app
    35,  # addresses
    36,  # artist_page
    37,  # podcast
    39,  # articles
    40,  # admin_tips
    41,  # menu
    42,  # fixed_post
    43,  # chats
    44,  # evergreen_notice
    45,  # musicians
    46,  # narratives
    47,  # donut_donate
    48,  # clips
    49,  # market_cart
    50,  # curators
    51,  # market_services
    53,  # classifieds
    54,  # textlives
    55,  # donut_for_dons
    57,  # badges
    58,  # chats_creation
    59,  # stream_creation
    60,  # rating
    61,  # service_rating
    62  # recommended_tips_widget
]

groups_group_is_closed = Literal[
    0,  # open
    1,  # closed
    2  # private
]

groups_group_market_currency = Literal[
    643,  # russian rubles
    980,  # ukrainian hryvnia
    398,  # kazakh tenge
    978,  # euro
    840  # us dollars
]

groups_group_photos = Literal[
    0,  # disabled
    1,  # open
    2  # limited
]

groups_group_role: TypeAlias = Literal['moderator', 'editor', 'administrator', 'advertiser']

groups_group_subject = Literal[
    1,  # auto
    2,  # activity holidays
    3,  # business
    4,  # pets
    5,  # health
    6,  # dating and communication
    7,  # games
    8,  # it
    9,  # cinema
    10,  # beauty and fashion
    11,  # cooking
    12,  # art and culture
    13,  # literature
    14,  # mobile services and internet
    15,  # music
    16,  # science and technology
    17,  # real estate
    18,  # news and media
    19,  # security
    20,  # education
    21,  # home and renovations
    22,  # politics
    23,  # food
    24,  # industry
    25,  # travel
    26,  # work
    27,  # entertainment
    28,  # religion
    29,  # family
    30,  # sports
    31,  # insurance
    32,  # television
    33,  # goods and services
    34,  # hobbies
    35,  # finance
    36,  # photo
    37,  # esoterics
    38,  # electronics and appliances
    39,  # erotic
    40,  # humor
    41,  # society_humanities
    42  # design and graphics
]

groups_group_suggested_privacy = Literal[
    0,  # none
    1,  # all
    2  # subscribers
]

groups_group_topics = Literal[
    0,  # disabled
    1,  # open
    2  # limited
]

groups_group_type: TypeAlias = Literal['group', 'page', 'event']  # Community type

groups_group_video = Literal[
    0,  # disabled
    1,  # open
    2  # limited
]

groups_group_wall = Literal[
    0,  # disabled
    1,  # open
    2,  # limited
    3  # closed
]

groups_group_wiki = Literal[
    0,  # disabled
    1,  # open
    2  # limited
]

groups_market_state: TypeAlias = Literal['none', 'basic', 'advanced']  # Declares state if market is enabled in group.

groups_member_role_permission: TypeAlias = Literal['ads']

groups_member_role_status: TypeAlias = Literal['moderator', 'editor', 'administrator', 'creator', 'advertiser']  # User's credentials as community admin

groups_online_status_type: TypeAlias = Literal['none', 'online', 'answer_mark']  # Type of online status of group

groups_role_options: TypeAlias = Literal['moderator', 'editor', 'administrator', 'creator']  # User's credentials as community admin

groups_sections_list_item: TypeAlias = 'base_object'

leadForms_answer_one_of: TypeAlias = Union['leadForms_answer_item', List['leadForms_answer_item']]

likes_type: TypeAlias = Literal['post', 'comment', 'photo', 'audio', 'video', 'note', 'market', 'photo_comment', 'video_comment', 'topic_comment', 'market_comment', 'sitepage', 'textpost', 'community_review', 'story', 'group_like']

market_market_category: TypeAlias = 'market_market_category_nested'

market_market_item_availability = Literal[
    0,  # available
    1,  # removed
    2  # unavailable
]

market_owner_type: TypeAlias = Literal['base', 'pro', 'disabled']  # Type of the market group

market_services_view_type = Literal[
    1,  # cards
    2  # rows
]

messages_action_one_of: TypeAlias = 'messages_message_action'

messages_chat_settings_state: TypeAlias = Literal['in', 'kicked', 'left', 'out']

messages_conversation_peer_type: TypeAlias = Literal['chat', 'email', 'user', 'group']  # Peer type

messages_fwd_messages: TypeAlias = List['messages_foreign_message']  # Forwarded messages

messages_history_message_attachment_type: TypeAlias = Literal['app_action', 'audio', 'doc', 'link', 'market', 'photo', 'video', 'wall', 'graffiti', 'audio_message']  # Attachments type

messages_keyboard_button_property_action: TypeAlias = Union['messages_keyboard_button_action_location', 'messages_keyboard_button_action_open_app', 'messages_keyboard_button_action_open_link', 'messages_keyboard_button_action_open_photo', 'messages_keyboard_button_action_text', 'messages_keyboard_button_action_callback', 'messages_keyboard_button_action_vkpay']

messages_message_action_status: TypeAlias = Literal['chat_photo_update', 'chat_photo_remove', 'chat_create', 'chat_title_update', 'chat_invite_user', 'chat_kick_user', 'chat_pin_message', 'chat_unpin_message', 'chat_invite_user_by_link', 'chat_invite_user_by_message_request', 'chat_screenshot']  # Action status

messages_message_attachment_type: TypeAlias = Literal['photo', 'audio', 'video', 'video_playlist', 'doc', 'link', 'market', 'gift', 'sticker', 'wall', 'wall_reply', 'article', 'poll', 'call', 'graffiti', 'audio_message']  # Attachment type

messages_template_action_type_names: TypeAlias = Literal['text', 'start', 'location', 'vkpay', 'open_app', 'open_photo', 'open_link', 'callback', 'intent_subscribe', 'intent_unsubscribe', 'open_modal_view']  # Template action type names

messages_user_type_for_xtr_invited_by: TypeAlias = Literal['profile', 'group']  # Object type

newsfeed_comments_filters: TypeAlias = Literal['post', 'photo', 'video', 'topic', 'note']

newsfeed_comments_item: TypeAlias = Union['newsfeed_comments_item_type_topic', 'newsfeed_comments_item_type_photo', 'newsfeed_comments_item_type_video', 'newsfeed_comments_item_type_notes', 'newsfeed_comments_item_type_post', 'newsfeed_comments_item_type_market']

newsfeed_ignore_item_type = Literal[
    'wall',  # post on the wall
    'tag',  # tag on a photo
    'profilephoto',  # profile photo
    'video',  # video
    'photo',  # photo
    'audio'  # audio
]

newsfeed_item_digest_item: TypeAlias = 'newsfeed_item_digest_full_item'

newsfeed_item_wallpost_feedback_type: TypeAlias = Literal['buttons', 'stars']

newsfeed_newsfeed_item: TypeAlias = Union['newsfeed_item_wallpost', 'newsfeed_item_photo', 'newsfeed_item_photo_tag', 'newsfeed_item_friend', 'newsfeed_item_audio', 'newsfeed_item_video', 'newsfeed_item_topic', 'newsfeed_item_digest', 'newsfeed_item_promo_button']

newsfeed_newsfeed_item_type: TypeAlias = Literal['post', 'photo', 'photo_tag', 'wall_photo', 'friend', 'audio', 'video', 'topic', 'digest', 'stories', 'note', 'audio_playlist', 'clip', 'clips_retention']  # Item type

notifications_notification_item: TypeAlias = 'notifications_notification'

pages_privacy_settings = Literal[
    0,  # community managers only
    1,  # community members only
    2  # everyone
]

photos_image_type: TypeAlias = Literal['s', 'm', 'x', 'l', 'o', 'p', 'q', 'r', 'y', 'z', 'w', 'base']  # Photo's type.

photos_photo_sizes_type: TypeAlias = Literal['t', 's', 'm', 'x', 'o', 'p', 'q', 'r', 'k', 'l', 'y', 'z', 'c', 'w', 'a', 'b', 'e', 'i', 'd', 'j', 'temp', 'h', 'g', 'n', 'f', 'max', 'base', 'u', 'v', 'orig']  # Size type

polls_poll_anonymous: TypeAlias = Flag  # Information whether the field is anonymous

prettyCards_button_one_of: TypeAlias = Union['base_link_button', str]

prettyCards_prettyCardOrError: TypeAlias = Union['prettyCards_prettyCard', 'base_error']

search_hint_section: TypeAlias = Literal['groups', 'events', 'publics', 'correspondents', 'people', 'friends', 'mutual_friends', 'promo']  # Section title

search_hint_type: TypeAlias = Literal['group', 'profile', 'vk_app', 'app', 'html5_game', 'link']  # Object type

stats_period_from_one_of: TypeAlias = int  # Unix timestamp

stats_period_to_one_of: TypeAlias = int  # Unix timestamp

store_product_icon: TypeAlias = 'stickers_image_set'

stories_story_stats_state: TypeAlias = Literal['on', 'off', 'hidden']  # Statistic state

stories_story_type: TypeAlias = Literal['photo', 'video', 'live_active', 'live_finished']  # Story type.

stories_upload_link_text: TypeAlias = Literal['to_store', 'vote', 'more', 'book', 'order', 'enroll', 'fill', 'signup', 'buy', 'ticket', 'write', 'open', 'learn_more', 'view', 'go_to', 'contact', 'watch', 'play', 'install', 'read', 'calendar']

support_unblock_screen_item: TypeAlias = Union['support_unblock_screen_textBorderedFields', 'support_unblock_screen_textBackgroundFields', 'support_unblock_screen_buttonUnblockFields', 'support_unblock_screen_buttonSubmitFields', 'support_unblock_screen_headerFields', 'support_unblock_screen_modalButtonFields', 'support_unblock_screen_tutorialFields', 'support_unblock_screen_stepperFields', 'support_unblock_screen_buttonFields', 'support_unblock_screen_contentBlockFields', 'support_unblock_screen_slidersFields', 'support_unblock_screen_eventsListFields', 'support_unblock_screen_buttonSupportFields']

users_fields: TypeAlias = Literal['first_name_nom', 'first_name_gen', 'first_name_dat', 'first_name_acc', 'first_name_ins', 'first_name_abl', 'last_name_nom', 'last_name_gen', 'last_name_dat', 'last_name_acc', 'last_name_ins', 'last_name_abl', 'photo_id', 'verified', 'sex', 'bdate', 'bdate_visibility', 'city', 'home_town', 'has_photo', 'photo', 'photo_rec', 'photo_50', 'photo_100', 'photo_200_orig', 'photo_200', 'photo_400', 'photo_400_orig', 'photo_big', 'photo_medium', 'photo_medium_rec', 'photo_max', 'photo_max_orig', 'photo_max_size', 'third_party_buttons', 'online', 'lists', 'domain', 'has_mobile', 'contacts', 'language', 'site', 'education', 'universities', 'schools', 'status', 'last_seen', 'followers_count', 'counters', 'common_count', 'online_info', 'occupation', 'nickname', 'relatives', 'relation', 'personal', 'connections', 'exports', 'wall_comments', 'wall_default', 'activities', 'activity', 'interests', 'music', 'movies', 'tv', 'books', 'is_no_index', 'no_index', 'games', 'about', 'quotes', 'can_post', 'can_see_all_posts', 'can_see_audio', 'can_see_gifts', 'work', 'places', 'can_write_private_message', 'can_send_friend_request', 'can_upload_doc', 'can_ban', 'is_favorite', 'is_hidden_from_feed', 'timezone', 'screen_name', 'maiden_name', 'crop_photo', 'is_friend', 'is_best_friend', 'friend_status', 'career', 'military', 'blacklisted', 'blacklisted_by_me', 'can_subscribe_posts', 'descriptions', 'trending', 'mutual', 'friendship_weeks', 'can_invite_to_chats', 'stories_archive_count', 'has_unseen_stories', 'video_live', 'video_live_level', 'video_live_count', 'clips_count', 'service_description', 'can_see_wishes', 'is_subscribed_podcasts', 'can_subscribe_podcasts', 'animated_avatar', 'owner_state', 'is_esia_verified', 'is_esia_linked', 'is_tinkoff_linked', 'is_tinkoff_verified', 'is_sber_verified', 'is_verified', 'oauth_linked', 'oauth_verification', 'is_sber_linked']

users_subscriptions_item: TypeAlias = Union['users_user_full', 'groups_group_full']

users_user_relation = Literal[
    0,  # not specified
    1,  # single
    2,  # in a relationship
    3,  # engaged
    4,  # married
    5,  # complicated
    6,  # actively searching
    7,  # in love
    8  # in a civil union
]

users_user_type: TypeAlias = Literal['profile']  # Object type

utils_domain_resolved_type: TypeAlias = Literal['user', 'group', 'application', 'page', 'vk_app', 'community_application']  # Object type

utils_link_checked_status: TypeAlias = Literal['not_banned', 'banned', 'processing']  # Link status

wall_comment_attachment_type: TypeAlias = Literal['photo', 'audio', 'audio_playlist', 'video', 'doc', 'link', 'note', 'page', 'market_market_album', 'market', 'sticker', 'graffiti']  # Attachment type

wall_get_filter: TypeAlias = Literal['owner', 'others', 'all', 'postponed', 'suggests', 'archived', 'donut']  # Filter to apply: 'owner' - posts by the wall owner, 'others' - posts by someone else, 'all' - posts by the wall owner and others (default), 'postponed' - timed posts (only available for calls with an 'access_token'), 'suggests' - suggested posts on a community wall

wall_post_source_type: TypeAlias = Literal['vk', 'widget', 'api', 'rss', 'sms', 'mvk']  # Type of post source

wall_post_type: TypeAlias = Literal['post', 'copy', 'reply', 'postpone', 'suggest', 'post_ads', 'photo', 'video', 'clip']  # Post type

wall_wall_item: TypeAlias = 'wall_wallpost_full'

wall_wallpost_attachment_type: TypeAlias = Literal['photo', 'photos_list', 'posted_photo', 'audio', 'audio_playlist', 'video', 'clip', 'video_playlist', 'doc', 'link', 'graffiti', 'note', 'app', 'poll', 'page', 'album', 'market_album', 'market', 'event', 'donut_link', 'article', 'textlive', 'textpost', 'textpost_publish', 'situational_theme', 'group', 'sticker', 'podcast']  # Attachment type

widgets_comment_media_type: TypeAlias = Literal['audio', 'photo', 'video']  # Media type

class account_account_counters(TypedDict):
    app_requests: NotRequired[int]  # New app requests number
    events: NotRequired[int]  # New events number
    faves: NotRequired[int]  # New faves number
    friends: NotRequired[int]  # New friends requests number
    friends_recommendations: NotRequired[int]  # New friends recommendations number
    gifts: NotRequired[int]  # New gifts number
    groups: NotRequired[int]  # New groups number
    messages: NotRequired[int]  # New messages number. Will be removed when messages.getCounters is released.
    memories: NotRequired[int]  # New memories number
    notes: NotRequired[int]  # New notes number
    notifications: NotRequired[int]  # New notifications number
    photos: NotRequired[int]  # New photo tags number

class account_info(TypedDict):
    # 2fa_required: NotRequired['base_bool_int']  # Two factor authentication is enabled
    https_required: NotRequired['base_bool_int']  # Information whether HTTPS-only is enabled
    intro: NotRequired[int]  # Information whether user has been processed intro
    lang: NotRequired[int]  # Language ID
    no_wall_replies: NotRequired['base_bool_int']  # Information whether wall comments should be hidden
    own_posts_default: NotRequired['base_bool_int']  # Information whether only owners posts should be shown

class account_name_request(TypedDict):
    first_name: NotRequired[str]  # First name in request
    id: NotRequired[int]  # Request ID needed to cancel the request
    last_name: NotRequired[str]  # Last name in request
    status: NotRequired['account_name_request_status']
    lang: NotRequired[str]  # Text to display to user
    link_href: NotRequired[str]  # href for link in lang field
    link_label: NotRequired[str]  # label to display for link in lang field

class account_offer(TypedDict):
    description: NotRequired[str]  # Offer description
    id: NotRequired[int]  # Offer ID
    img: NotRequired[str]  # URL of the preview image
    instruction: NotRequired[str]  # Instruction how to process the offer
    instruction_html: NotRequired[str]  # Instruction how to process the offer (HTML format)
    price: NotRequired[int]  # Offer price
    short_description: NotRequired[str]  # Offer short description
    tag: NotRequired[str]  # Offer tag
    title: NotRequired[str]  # Offer title
    currency_amount: NotRequired[float]  # Currency amount
    link_id: NotRequired[int]  # Link id
    link_type: NotRequired[Literal['profile', 'group', 'app']]  # Link type

class account_push_conversations(TypedDict):
    count: NotRequired[int]  # Items count
    items: NotRequired[List['account_push_conversations_item']]

class account_push_conversations_item(TypedDict):
    disabled_until: int  # Time until that notifications are disabled in seconds
    peer_id: int  # Peer ID
    sound: 'base_bool_int'  # Information whether the sound are enabled
    disabled_mentions: NotRequired['base_bool_int']  # Information whether the mentions are disabled
    disabled_mass_mentions: NotRequired['base_bool_int']  # Information whether the mass mentions (like '@all', '@online') are disabled. Can be affected by 'disabled_mentions'

class account_push_params(TypedDict):
    msg: NotRequired[List['account_push_params_mode']]
    chat: NotRequired[List['account_push_params_mode']]
    like: NotRequired[List['account_push_params_settings']]
    repost: NotRequired[List['account_push_params_settings']]
    comment: NotRequired[List['account_push_params_settings']]
    mention: NotRequired[List['account_push_params_settings']]
    reply: NotRequired[List['account_push_params_onoff']]
    new_post: NotRequired[List['account_push_params_onoff']]
    wall_post: NotRequired[List['account_push_params_onoff']]
    wall_publish: NotRequired[List['account_push_params_onoff']]
    friend: NotRequired[List['account_push_params_onoff']]
    friend_found: NotRequired[List['account_push_params_onoff']]
    friend_accepted: NotRequired[List['account_push_params_onoff']]
    group_invite: NotRequired[List['account_push_params_onoff']]
    group_accepted: NotRequired[List['account_push_params_onoff']]
    birthday: NotRequired[List['account_push_params_onoff']]
    event_soon: NotRequired[List['account_push_params_onoff']]
    app_request: NotRequired[List['account_push_params_onoff']]
    sdk_open: NotRequired[List['account_push_params_onoff']]

class account_push_settings(TypedDict):
    disabled: NotRequired['base_bool_int']  # Information whether notifications are disabled
    disabled_until: NotRequired[int]  # Time until that notifications are disabled in Unixtime
    settings: NotRequired['account_push_params']
    conversations: NotRequired['account_push_conversations']

class account_user_settings_interest(TypedDict):
    title: str
    value: str

class account_user_settings_interests(TypedDict):
    activities: NotRequired['account_user_settings_interest']
    interests: NotRequired['account_user_settings_interest']
    music: NotRequired['account_user_settings_interest']
    tv: NotRequired['account_user_settings_interest']
    movies: NotRequired['account_user_settings_interest']
    books: NotRequired['account_user_settings_interest']
    games: NotRequired['account_user_settings_interest']
    quotes: NotRequired['account_user_settings_interest']
    about: NotRequired['account_user_settings_interest']

class ads_accesses(TypedDict):
    client_id: NotRequired[str]  # Client ID
    role: NotRequired['ads_access_role']

class ads_account(TypedDict):
    access_role: 'ads_access_role'
    account_id: int  # Account ID
    account_status: 'base_bool_int'  # Information whether account is active
    account_type: 'ads_account_type'
    account_name: str  # Account name
    can_view_budget: Flag  # Can user view account budget

class ads_ad(TypedDict):
    ad_format: int  # Ad format
    ad_platform: Union[int, str]  # Ad platform
    all_limit: str  # Total limit
    approved: 'ads_ad_approved'
    campaign_id: int  # Campaign ID
    category1_id: NotRequired[int]  # Category ID
    category2_id: NotRequired[int]  # Additional category ID
    cost_type: 'ads_ad_cost_type'
    cpc: NotRequired[str]  # Cost of a click, kopecks
    cpm: NotRequired[str]  # Cost of 1000 impressions, kopecks
    cpa: NotRequired[str]  # Cost of an action, kopecks
    ocpm: NotRequired[str]  # Cost of 1000 impressions optimized, kopecks
    autobidding: NotRequired['base_bool_int']  # Autobidding
    autobidding_max_cost: NotRequired[str]  # Max cost of target actions for autobidding, kopecks
    disclaimer_medical: NotRequired['base_bool_int']  # Information whether disclaimer is enabled
    disclaimer_specialist: NotRequired['base_bool_int']  # Information whether disclaimer is enabled
    disclaimer_supplements: NotRequired['base_bool_int']  # Information whether disclaimer is enabled
    id: int  # Ad ID
    impressions_limit: NotRequired[int]  # Impressions limit
    impressions_limit_period: NotRequired[int]  # Impressions limit period
    impressions_limited: NotRequired['base_bool_int']  # Information whether impressions are limited
    name: str  # Ad title
    status: 'ads_ad_status'
    video: NotRequired['base_bool_int']  # Information whether the ad is a video
    day_limit: NotRequired[str]  # Day limit
    goal_type: NotRequired[int]  # Goal type
    user_goal_type: NotRequired[int]  # User goal type
    age_restriction: NotRequired[int]  # Age restriction
    conversion_pixel_id: NotRequired[int]  # Conversion pixel id
    conversion_event_id: NotRequired[int]  # Conversion event id
    create_time: NotRequired[int]  # Create time
    update_time: NotRequired[int]  # Update time
    start_time: NotRequired[int]  # Start time
    stop_time: NotRequired[int]  # Stop time
    publisher_platforms_auto: NotRequired['base_bool_int']  # Publisher platform auto
    publisher_platforms: NotRequired[str]  # Publisher platforms
    link_url: NotRequired[str]  # Link url
    link_owner_id: NotRequired[int]  # Link owner id
    link_id: NotRequired[int]  # Link id
    has_campaign_budget_optimization: NotRequired[Flag]  # Has campaign budget optimization
    events_retargeting_groups: NotRequired[List['ads_events_retargeting_group']]  # Events retargeting groups
    weekly_schedule_hours: NotRequired[List[str]]  # Weekly schedule hours
    weekly_schedule_use_holidays: NotRequired[int]  # Weekly schedule use holidays
    ad_platform_no_ad_network: NotRequired[int]  # Ad platform no ad network
    ad_platform_no_wall: NotRequired[int]  # Ad platform no wall
    disclaimer_finance: NotRequired[int]  # Disclaimer finance
    disclaimer_finance_name: NotRequired[str]  # Disclaimer finance name
    disclaimer_finance_license_no: NotRequired[str]  # Disclaimer finance license no
    is_promo: NotRequired[Flag]  # is promo
    suggested_criteria: NotRequired[int]  # Suggested criteria
    link_type: NotRequired[int]  # Link type

class ads_ad_layout(TypedDict):
    ad_format: int  # Ad format
    campaign_id: int  # Campaign ID
    cost_type: 'ads_ad_cost_type'
    description: str  # Ad description
    id: int  # Ad ID
    image_src: str  # Image URL
    image_src_2x: NotRequired[str]  # URL of the preview image in double size
    link_domain: NotRequired[str]  # Domain of advertised object
    link_url: str  # URL of advertised object
    link_type: int  # Type of advertised object
    preview_link: NotRequired[str]  # link to preview an ad as it is shown on the website
    title: str  # Ad title
    video: NotRequired['base_bool_int']  # Information whether the ad is a video
    social: NotRequired[Flag]  # Social
    okved: NotRequired[str]  # Okved
    age_restriction: NotRequired[int]  # Age restriction
    goal_type: NotRequired[int]  # Goal type
    link_title: NotRequired[str]  # Link title
    link_button: NotRequired[str]  # Link button
    repeat_video: NotRequired[int]  # Repeat video
    video_src_240: NotRequired[str]  # Video source 240p
    video_src_360: NotRequired[str]  # Video source 360p
    video_src_480: NotRequired[str]  # Video source 480p
    video_src_720: NotRequired[str]  # Video source 720p
    video_src_1080: NotRequired[str]  # Video source 1080p
    video_src_1440: NotRequired[str]  # Video source 1440p
    video_src_2160: NotRequired[str]  # Video source 2160p
    video_image_src: NotRequired[str]  # Video image source
    video_image_src_2x: NotRequired[str]  # Video image source 2x
    video_duration: NotRequired[int]  # Video duration
    icon_src: NotRequired[str]  # Icon source
    icon_src_2x: NotRequired[str]  # Icon source 2x
    post: NotRequired['ads_post']
    stories_data: NotRequired['ads_stories']
    clips_list: NotRequired[List['ads_clip_item']]

class ads_campaign(TypedDict):
    ads_count: NotRequired[int]  # Amount of active ads in campaign
    all_limit: str  # Campaign's total limit, rubles
    create_time: NotRequired[int]  # Campaign create time, as Unixtime
    goal_type: NotRequired[int]  # Campaign goal type
    user_goal_type: NotRequired[int]  # Campaign user goal type
    is_cbo_enabled: NotRequired[Flag]  # Shows if Campaign Budget Optimization is on
    day_limit: str  # Campaign's day limit, rubles
    id: int  # Campaign ID
    name: str  # Campaign title
    start_time: int  # Campaign start time, as Unixtime
    status: 'ads_campaign_status'
    stop_time: int  # Campaign stop time, as Unixtime
    type: 'ads_campaign_type'
    update_time: NotRequired[int]  # Campaign update time, as Unixtime
    views_limit: NotRequired[int]  # Limit of views per user per campaign

class ads_category(TypedDict):
    id: int  # Category ID
    name: str  # Category name
    subcategories: NotRequired[List['ads_category']]

class ads_client(TypedDict):
    all_limit: str  # Client's total limit, rubles
    day_limit: str  # Client's day limit, rubles
    id: int  # Client ID
    name: str  # Client name
    ord_data: NotRequired['ads_ord_data']  # Ord data

class ads_clip_item(TypedDict):
    video_id: NotRequired[int]  # Video id
    preview_url: NotRequired[str]  # Preview url
    link: NotRequired['ads_clip_item_link']

class ads_clip_item_link(TypedDict):
    '''Link'''
    text: NotRequired[str]  # Text
    key: NotRequired[str]  # Key
    url: NotRequired[str]  # Url

class ads_create_ad_status(TypedDict):
    id: int  # Ad ID
    post_id: NotRequired[int]  # Stealth Post ID
    error_code: NotRequired[int]  # Error code
    error_desc: NotRequired[str]  # Error description

class ads_create_campaign_status(TypedDict):
    id: int  # Campaign ID
    error_code: NotRequired[int]  # Error code
    error_desc: NotRequired[str]  # Error description

class ads_create_clients_status(TypedDict):
    id: int  # Client ID
    error_code: NotRequired[int]  # Error code
    error_desc: NotRequired[str]  # Error description

class ads_criteria(TypedDict):
    age_from: NotRequired[str]  # Age from
    age_to: NotRequired[str]  # Age to
    apps: NotRequired[str]  # Apps IDs
    apps_not: NotRequired[str]  # Apps IDs to except
    birthday: NotRequired[str]  # Days to birthday
    cities: NotRequired[str]  # Cities IDs
    cities_not: NotRequired[str]  # Cities IDs to except
    districts: NotRequired[str]  # Districts IDs
    groups: NotRequired[str]  # Communities IDs
    interest_categories: NotRequired[str]  # Interests categories IDs
    interests: NotRequired[str]  # Interests
    paying: NotRequired[str]  # Information whether the user has proceeded VK payments before
    positions: NotRequired[str]  # Positions IDs
    religions: NotRequired[str]  # Religions IDs
    retargeting_groups: NotRequired[str]  # Retargeting groups ids
    retargeting_groups_not: NotRequired[str]  # Retargeting groups NOT ids
    school_from: NotRequired[str]  # School graduation year from
    school_to: NotRequired[str]  # School graduation year to
    schools: NotRequired[str]  # Schools IDs
    sex: NotRequired['ads_criteria_sex']
    stations: NotRequired[str]  # Stations IDs
    statuses: NotRequired[str]  # Relationship statuses
    streets: NotRequired[str]  # Streets IDs
    travellers: NotRequired[str]  # Travellers
    ab_test: NotRequired[str]  # AB test
    uni_from: NotRequired[str]  # University graduation year from
    uni_to: NotRequired[str]  # University graduation year to
    user_browsers: NotRequired[str]  # Browsers
    user_devices: NotRequired[str]  # Devices
    user_os: NotRequired[str]  # Operating systems
    suggested_criteria: NotRequired[str]  # Suggested criteria
    groups_not: NotRequired[str]  # Group not
    price_list_audience_type: NotRequired[str]  # Price list audience type
    count: NotRequired[str]  # Count
    groups_active_formula: NotRequired[str]  # Group active formula
    interest_categories_formula: NotRequired[str]  # Interest categories formula
    groups_formula: NotRequired[str]  # Groups formula
    groups_active: NotRequired[str]  # Groups active
    group_types: NotRequired[str]  # Group types
    key_phrases: NotRequired[str]  # Key phrases
    key_phrases_days: NotRequired[str]  # Key phrases days
    geo_near: NotRequired[str]  # Geo near
    geo_point_type: NotRequired[str]  # Geo point type
    price_list_id: NotRequired[str]  # Price list id
    groups_recommended: NotRequired[str]  # Groups recommended ids
    groups_active_recommended: NotRequired[str]  # Groups active recommended ids
    music_artists_formula: NotRequired[str]  # Music artists formula
    price_list_retargeting_formula: NotRequired[str]  # Price list retargeting formula
    tags: NotRequired[str]  # Tags
    browsers: NotRequired[str]  # Browsers
    mobile_os_min_version: NotRequired[str]  # Mobile os min version
    mobile_apps_events_formula: NotRequired[str]  # Mobile apps events formula
    mobile_os_max_version: NotRequired[str]  # Mobile os max version
    operators: NotRequired[str]  # operators
    wifi_only: NotRequired[str]  # wifi_only
    mobile_manufacturers: NotRequired[str]  # mobile_manufacturers

class ads_demo_stats(TypedDict):
    id: NotRequired[int]  # Object ID
    stats: NotRequired[List['ads_demostats_format']]
    type: NotRequired['ads_object_type']

class ads_demographic_stats_period_item_base(TypedDict):
    clicks_rate: NotRequired[float]  # Clicks rate
    impressions_rate: NotRequired[float]  # Impressions rate

class ads_demostats_format(TypedDict):
    age: NotRequired[List['ads_stats_age']]
    cities: NotRequired[List['ads_stats_cities']]
    day: NotRequired[str]  # Day as YYYY-MM-DD
    day_from: NotRequired[str]
    day_to: NotRequired[str]
    month: NotRequired[str]  # Month as YYYY-MM
    overall: NotRequired[int]  # 1 if period=overall
    sex: NotRequired[List['ads_stats_sex']]
    sex_age: NotRequired[List['ads_stats_sex_age']]

class ads_events_retargeting_group(TypedDict):
    id: NotRequired[int]
    value: NotRequired[List[int]]

class ads_flood_stats(TypedDict):
    left: int  # Requests left
    refresh: int  # Time to refresh in seconds
    stats_by_user: NotRequired[List['ads_flood_stats_by_user_item']]  # Used requests per user

class ads_flood_stats_by_user_item(TypedDict):
    user_id: int  # User ID
    requests_count: int  # Used requests

class ads_link_status(TypedDict):
    description: NotRequired[str]  # Reject reason
    redirect_url: NotRequired[str]  # URL
    status: str  # Link status

class ads_lookalike_request(TypedDict):
    id: int  # Lookalike request ID
    create_time: int  # Lookalike request create time, as Unixtime
    update_time: int  # Lookalike request update time, as Unixtime
    scheduled_delete_time: NotRequired[int]  # Time by which lookalike request would be deleted, as Unixtime
    status: Literal['search_in_progress', 'search_failed', 'search_done', 'save_in_progress', 'save_failed', 'save_done']  # Lookalike request status
    source_type: Literal['retargeting_group']  # Lookalike request source type
    source_retargeting_group_id: NotRequired[int]  # Retargeting group id, which was used as lookalike seed
    source_name: NotRequired[str]  # Lookalike request seed name (retargeting group name)
    audience_count: NotRequired[int]  # Lookalike request seed audience size
    save_audience_levels: NotRequired[List['ads_lookalike_request_save_audience_level']]

class ads_lookalike_request_save_audience_level(TypedDict):
    level: NotRequired[int]  # Save audience level id, which is used in save audience queries
    audience_count: NotRequired[int]  # Saved audience audience size for according level

class ads_mobile_stat_item(TypedDict):
    key: NotRequired[str]
    value: NotRequired[float]

class ads_musician(TypedDict):
    id: int  # Targeting music artist ID
    original_id: str  # Music artist ID as in VKMusic
    name: str  # Music artist name
    avatar: NotRequired[str]  # Music artist photo

class ads_ord_data(TypedDict):
    client_type: 'ads_ord_client_type'
    client_name: str
    inn: NotRequired[str]
    phone: str
    subagent: NotRequired['ads_ord_subagent']
    contract_number: str
    contract_date: str
    contract_type: str
    contract_object: str
    with_vat: Flag

class ads_ord_subagent(TypedDict):
    type: 'ads_ord_client_type'
    name: str
    inn: NotRequired[str]
    phone: str

class ads_post(TypedDict):
    id: NotRequired[int]  # Post id
    from_id: NotRequired[int]  # From id
    owner_id: NotRequired[int]  # Owner id
    date: NotRequired[int]  # Date
    edited: NotRequired[int]  # Edited date
    is_pinned: NotRequired[int]  # Is pinned
    marked_as_ads: NotRequired[int]  # Marked as ads
    ads_easy_promote: NotRequired['ads_post_easy_promote']
    donut: NotRequired['ads_post_donut']
    comments: NotRequired['ads_post_comments']
    copyright: NotRequired['wall_post_copyright']
    short_text_rate: NotRequired[float]  # Short text rate
    type: NotRequired[str]  # Type
    is_favorite: NotRequired[Flag]  # Is favorite
    likes: NotRequired['ads_post_likes']
    views: NotRequired['ads_post_views']
    post_type: NotRequired[str]  # Post type
    reposts: NotRequired['ads_post_reposts']
    text: NotRequired[str]  # Text
    is_promoted_post_stealth: NotRequired[Flag]  # Is promoted post stealth
    hash: NotRequired[str]  # Hash
    owner: NotRequired['ads_post_owner']
    attachments: NotRequired[List['wall_wallpost_attachment']]
    created_by: NotRequired[int]  # Created by
    carousel_offset: NotRequired[int]  # Carousel offset
    can_edit: NotRequired[int]  # Can edit
    can_delete: NotRequired[int]  # Can delete
    can_pin: NotRequired[int]  # Can pin

class ads_post_comments(TypedDict):
    '''Comments'''
    count: NotRequired[int]  # Count

class ads_post_donut(TypedDict):
    '''Donut'''
    is_donut: NotRequired[Flag]  # Is donut

class ads_post_easy_promote(TypedDict):
    '''Ads easy promote'''
    type: NotRequired[int]  # Type
    text: NotRequired[str]  # Text
    label_text: NotRequired[str]  # Label text
    button_text: NotRequired[str]  # Button text
    is_ad_not_easy: NotRequired[Flag]  # Is ad not easy
    ad_id: NotRequired[int]  # Ad id
    top_union_id: NotRequired[int]  # Top union id

class ads_post_likes(TypedDict):
    '''Likes'''
    can_like: NotRequired[int]  # Can like
    count: NotRequired[int]  # Count
    user_likes: NotRequired[int]  # User likes

class ads_post_owner(TypedDict):
    '''Owner'''
    id: NotRequired[int]  # Owner id
    name: NotRequired[str]  # Name
    photo: NotRequired[str]  # Photo url
    url: NotRequired[str]  # Profile url

class ads_post_reposts(TypedDict):
    '''Reposts'''
    count: NotRequired[int]  # Count
    wall_count: NotRequired[int]  # Wall count
    mail_count: NotRequired[int]  # Mail count

class ads_post_views(TypedDict):
    '''Views'''
    count: NotRequired[int]  # Count

class ads_promoted_post_reach(TypedDict):
    hide: int  # Hides amount
    id: int  # Object ID from 'ids' parameter
    join_group: int  # Community joins
    links: int  # Link clicks
    reach_subscribers: int  # Subscribers reach
    reach_total: int  # Total reach
    report: int  # Reports amount
    to_group: int  # Community clicks
    unsubscribe: int  # 'Unsubscribe' events amount
    video_views_100p: NotRequired[int]  # Video views for 100 percent
    video_views_25p: NotRequired[int]  # Video views for 25 percent
    video_views_3s: NotRequired[int]  # Video views for 3 seconds
    video_views_10s: NotRequired[int]  # Video views for 10 seconds
    video_views_50p: NotRequired[int]  # Video views for 50 percent
    video_views_75p: NotRequired[int]  # Video views for 75 percent
    video_views_start: NotRequired[int]  # Video starts
    pretty_cards_clicks: NotRequired[int]  # Pretty cards clicks

class ads_reject_reason(TypedDict):
    comment: NotRequired[str]  # Comment text
    rules: NotRequired[List['ads_rules']]

class ads_rules(TypedDict):
    help_url: NotRequired[Union[str, Flag]]  # Help url
    help_label: NotRequired[str]  # Label
    content_html: NotRequired[str]  # Content Html
    help_chat: NotRequired[Flag]  # Help chat

class ads_statistic_click_action(TypedDict):
    type: NotRequired[Literal['load', 'impression', 'click_deeplink', 'click', 'click_post_owner', 'click_post_link', 'click_pretty_card', 'like_post', 'share_post', 'video_start', 'video_pause', 'video_resume', 'video_play_3s', 'video_play_10s', 'video_play_25', 'video_play_50', 'video_play_75', 'video_play_95', 'video_play_100', 'video_volume_on', 'video_volume_off', 'video_fullscreen_on', 'video_fullscreen_off', 'hide']]
    url: NotRequired[str]

class ads_stats(TypedDict):
    id: NotRequired[int]  # Object ID
    stats: NotRequired[List['ads_stats_format']]
    type: NotRequired['ads_object_type']
    views_times: NotRequired['ads_stats_views_times']

class ads_stats_format(TypedDict):
    clicks: NotRequired[int]  # Clicks number
    link_external_clicks: NotRequired[int]  # External clicks number
    day: NotRequired[str]  # Day as YYYY-MM-DD
    impressions: NotRequired[int]  # Impressions number
    join_rate: NotRequired[int]  # Events number
    month: NotRequired[str]  # Month as YYYY-MM
    year: NotRequired[int]  # Year as YYYY
    overall: NotRequired[int]  # 1 if period=overall
    reach: NotRequired[int]  # Reach
    spent: NotRequired[str]  # Spent funds
    video_plays_unique_started: NotRequired[int]  # Video plays unique started count
    video_plays_unique_3_seconds: NotRequired[int]  # Video plays unique 3 seconds count
    video_plays_unique_10_seconds: NotRequired[int]  # Video plays unique 10 seconds count
    video_plays_unique_25_percents: NotRequired[int]  # Video plays unique 25 percents count
    video_plays_unique_50_percents: NotRequired[int]  # Video plays unique 50 percents count
    video_plays_unique_75_percents: NotRequired[int]  # Video plays unique 75 percents count
    video_plays_unique_100_percents: NotRequired[int]  # Video plays unique 100 percents count
    effective_cost_per_click: NotRequired[str]  # Effective cost per click
    effective_cost_per_mille: NotRequired[str]  # Effective cost per mille
    effective_cpf: NotRequired[str]  # Effective cpf
    effective_cost_per_message: NotRequired[str]  # Effective cost per message
    message_sends: NotRequired[int]  # Message sends count
    message_sends_by_any_user: NotRequired[int]  # Message sends by anu user
    conversions_external: NotRequired[int]  # Conversions external
    conversion_count: NotRequired[int]  # Conversions count
    conversion_cr: NotRequired[str]  # Conversions CR
    day_from: NotRequired[str]  # Day from
    day_to: NotRequired[str]  # Day to
    ctr: NotRequired[str]  # Ctr
    uniq_views_count: NotRequired[int]  # Unique views count
    mobile_app_stat: NotRequired[List['ads_mobile_stat_item']]  # Mobile app stat

class ads_stats_views_times(TypedDict):
    views_ads_times_1: NotRequired[int]
    views_ads_times_2: NotRequired[int]
    views_ads_times_3: NotRequired[int]
    views_ads_times_4: NotRequired[int]
    views_ads_times_5: NotRequired[str]
    views_ads_times_6: NotRequired[int]
    views_ads_times_7: NotRequired[int]
    views_ads_times_8: NotRequired[int]
    views_ads_times_9: NotRequired[int]
    views_ads_times_10: NotRequired[int]
    views_ads_times_11_plus: NotRequired[int]

class ads_stories(TypedDict):
    stories: NotRequired[List['ads_story_item']]
    owner: NotRequired['ads_stories_owner']
    stories_disclaimers_text: NotRequired[str]  # Stories disclaimers text

class ads_stories_owner(TypedDict):
    id: NotRequired[Union[int, Flag]]  # Owner id
    href: NotRequired[str]  # Href
    name: NotRequired[str]  # Name
    photo: NotRequired[str]  # Photo
    verify: NotRequired[str]  # Verify
    gender: NotRequired[str]  # Gender
    name_get: NotRequired[str]  # Name get
    firstName: NotRequired[str]  # First name
    first_name_gen: NotRequired[str]  # First name gen
    first_name_ins: NotRequired[str]  # First name ins
    can_follow: NotRequired[Flag]  # Can follow

class ads_story_item(TypedDict):
    id: NotRequired[int]  # Story id
    owner_id: NotRequired[int]  # Owner id
    raw_id: NotRequired[str]  # Story raw id
    date: NotRequired[str]  # Date
    time: NotRequired[int]  # Time
    type: NotRequired[str]  # Type
    unread: NotRequired[Flag]  # Is unread
    canLike: NotRequired[Flag]  # Can like
    can_comment: NotRequired[Flag]  # Can comment
    can_share: NotRequired[Flag]  # Can share
    can_remove: NotRequired[Flag]  # Can remove
    can_manage: NotRequired[Flag]  # Can manage
    can_ask: NotRequired[Flag]  # Can ask
    can_ask_anonymous: NotRequired[Flag]  # Can ask anonymous
    isProfileQuestion: NotRequired[Flag]  # Is profile question
    stats: NotRequired['ads_story_item_stats']
    link: NotRequired['ads_story_item_link']
    photo_url: NotRequired[str]  # Photo url
    preview_url: NotRequired[str]  # Preview url
    track_code: NotRequired[str]  # Track code
    isPartOfNarrative: NotRequired[Flag]  # Is part of narrative
    isAds: NotRequired[Flag]  # Is ads
    video_url: NotRequired[str]  # Video url
    first_frame: NotRequired[str]  # First frame
    small_preview: NotRequired[str]  # Small preview
    isLiked: NotRequired[Flag]  # Is liked

class ads_story_item_link(TypedDict):
    key: NotRequired[str]  # Key
    text: NotRequired[str]  # Text
    url: NotRequired[str]  # Url
    raw_url: NotRequired[str]  # Raw url

class ads_story_item_stats(TypedDict):
    follow: NotRequired['ads_story_item_stats_follow']
    url_view: NotRequired['ads_story_item_stats_url_view']

class ads_story_item_stats_follow(TypedDict):
    '''Follow event stats'''
    event_type: NotRequired[str]  # Event type
    rhash: NotRequired[str]  # Event hash

class ads_story_item_stats_url_view(TypedDict):
    '''Url view event stats'''
    event_type: NotRequired[str]  # Event type
    rhash: NotRequired[str]  # Event hash

class ads_targ_stats(TypedDict):
    audience_count: int  # Audience
    recommended_cpc: NotRequired[str]  # Recommended CPC value for 50% reach (old format)
    recommended_cpm: NotRequired[str]  # Recommended CPM value for 50% reach (old format)
    recommended_cpc_50: NotRequired[str]  # Recommended CPC value for 50% reach
    recommended_cpm_50: NotRequired[str]  # Recommended CPM value for 50% reach
    recommended_cpc_70: NotRequired[str]  # Recommended CPC value for 70% reach
    recommended_cpm_70: NotRequired[str]  # Recommended CPM value for 70% reach
    recommended_cpc_90: NotRequired[str]  # Recommended CPC value for 90% reach
    recommended_cpm_90: NotRequired[str]  # Recommended CPM value for 90% reach
    total_alive_audience: NotRequired[int]  # Total alive audience

class ads_targ_suggestions(TypedDict):
    id: NotRequired[int]  # Object ID
    name: NotRequired[str]  # Object name
    type: NotRequired[str]  # Object type
    parent: NotRequired[str]  # Parent

class ads_targ_suggestions_cities(TypedDict):
    id: NotRequired[int]  # Object ID
    name: NotRequired[str]  # Object name
    parent: NotRequired[str]  # Parent object

class ads_targ_suggestions_regions(TypedDict):
    id: NotRequired[int]  # Object ID
    name: NotRequired[str]  # Object name
    type: NotRequired[str]  # Object type

class ads_targ_suggestions_schools(TypedDict):
    desc: NotRequired[str]  # Full school title
    id: NotRequired[int]  # School ID
    name: NotRequired[str]  # School title
    parent: NotRequired[str]  # City name
    type: NotRequired['ads_targ_suggestions_schools_type']

class ads_target_group(TypedDict):
    id: NotRequired[int]  # Group ID
    name: NotRequired[str]  # Group name
    is_audience: NotRequired[Flag]  # Is audience
    is_shared: NotRequired[Flag]  # Is shared
    file_source: NotRequired[Flag]  # File source
    api_source: NotRequired[Flag]  # API source
    lookalike_source: NotRequired[Flag]  # File source
    audience_count: NotRequired[int]  # Audience
    domain: NotRequired[str]  # Site domain
    lifetime: NotRequired[int]  # Number of days for user to be in group
    pixel: NotRequired[str]  # Pixel code
    target_pixel_id: NotRequired[int]  # Target Pixel id
    target_pixel_rules: NotRequired[List['ads_target_group_target_pixel_rule']]  # Target Pixel rules
    last_updated: NotRequired[int]  # Last updated

class ads_target_group_target_pixel_rule(TypedDict):
    url_full_match: NotRequired[str]
    event_full_match: NotRequired[str]
    url_substrings_match: NotRequired[List[str]]
    event_substrings_match: NotRequired[List[str]]
    url_regex_match: NotRequired[str]
    event_regex_match: NotRequired[str]

class ads_target_pixel_info(TypedDict):
    target_pixel_id: int
    name: str
    domain: str
    category_id: int
    last_updated: int
    pixel: str

class ads_updateOfficeUsers_result(TypedDict):
    user_id: int
    is_success: Flag
    error: NotRequired['base_error']

class ads_update_ads_status(TypedDict):
    id: int  # Ad ID
    error_code: NotRequired[int]  # Error code
    error_desc: NotRequired[str]  # Error description

class ads_update_clients_status(TypedDict):
    id: int  # Client ID
    error_code: NotRequired[int]  # Error code
    error_desc: NotRequired[str]  # Error description

class ads_user_specification(TypedDict):
    user_id: int
    role: 'ads_access_role_public'
    grant_access_to_all_clients: NotRequired[Flag]
    client_ids: NotRequired[List[int]]
    view_budget: NotRequired[Flag]

class ads_user_specification_cutted(TypedDict):
    user_id: int
    role: 'ads_access_role_public'
    client_id: NotRequired[int]
    view_budget: NotRequired[Flag]

class ads_users(TypedDict):
    accesses: List['ads_accesses']
    user_id: int  # User ID

class adsweb_getAdCategories_response_categories_category(TypedDict):
    id: int
    name: str

class adsweb_getAdUnits_response_ad_units_ad_unit(TypedDict):
    id: int
    site_id: int
    name: NotRequired[str]

class adsweb_getFraudHistory_response_entries_entry(TypedDict):
    site_id: int
    day: str

class adsweb_getSites_response_sites_site(TypedDict):
    id: int
    status_user: NotRequired[str]
    status_moder: NotRequired[str]
    domains: NotRequired[str]

class adsweb_getStatistics_response_items_item(TypedDict):
    site_id: NotRequired[int]
    ad_unit_id: NotRequired[int]
    overall_count: NotRequired[int]
    months_count: NotRequired[int]
    month_min: NotRequired[str]
    month_max: NotRequired[str]
    days_count: NotRequired[int]
    day_min: NotRequired[str]
    day_max: NotRequired[str]
    hours_count: NotRequired[int]
    hour_min: NotRequired[str]
    hour_max: NotRequired[str]

class apps_app_min(TypedDict):
    type: 'apps_app_type'
    id: int  # Application ID
    title: str  # Application title
    author_owner_id: NotRequired[int]  # Application author's ID
    is_installed: NotRequired[Flag]  # Is application installed
    icon_139: NotRequired[str]  # URL of the app icon with 139 px in width
    icon_150: NotRequired[str]  # URL of the app icon with 150 px in width
    icon_278: NotRequired[str]  # URL of the app icon with 278 px in width
    icon_576: NotRequired[str]  # URL of the app icon with 576 px in width
    background_loader_color: NotRequired[str]  # Hex color code without hash sign
    loader_icon: NotRequired[str]  # SVG data
    icon_75: NotRequired[str]  # URL of the app icon with 75 px in width
    screen_orientation: NotRequired[int]  # Screen orientation

class apps_catalog_list(TypedDict):
    count: int  # Total number
    items: List['apps_app']
    profiles: NotRequired[List['users_user_min']]

class apps_custom_snippet(TypedDict):
    vk_ref: NotRequired[vk_ref_enum]
    group_id: NotRequired[List[int]]
    hash: NotRequired[List[str]]
    snippet_id: NotRequired[int]
    title: NotRequired[str]
    description: NotRequired[str]
    expired_at: NotRequired[int]
    image_url: NotRequired[str]
    small_image_url: NotRequired[str]
    button: NotRequired[Literal['buy', 'buy_ticket', 'contact', 'create', 'enroll', 'fill', 'go', 'open', 'play']]

class apps_leaderboard(TypedDict):
    level: NotRequired[int]  # Level
    points: NotRequired[int]  # Points number
    score: NotRequired[int]  # Score number
    user_id: int  # User ID

class apps_scope(TypedDict):
    '''Scope description'''
    name: Literal['friends', 'photos', 'video', 'pages', 'status', 'notes', 'wall', 'docs', 'groups', 'stats', 'market', 'stories', 'app_widget', 'messages', 'manage', 'notify', 'audio', 'support', 'menu', 'wallmenu', 'ads', 'offline', 'notifications', 'email', 'adsweb', 'leads', 'group_messages', 'exchange', 'phone']  # Scope name
    title: NotRequired[str]  # Scope title

class apps_testing_group(TypedDict):
    user_ids: List[int]
    group_id: int
    name: NotRequired[str]
    webview: NotRequired[str]
    platforms: NotRequired[platforms_enum]

class appWidgets_photo(TypedDict):
    id: str  # Image ID
    images: List['base_image']

class appWidgets_photos(TypedDict):
    count: NotRequired[int]
    items: NotRequired[List['appWidgets_photo']]

class asr_task(TypedDict):
    id: str  # Task ID in UUID format.
    status: Literal['processing', 'finished', 'internal_error', 'transcoding_error', 'recognition_error']  # Status of the task.
    text: str  # Recognised text, if task is `finished`.

class audio_audio(TypedDict):
    access_key: NotRequired[str]  # Access key for the audio
    artist: str  # Artist name
    id: int  # Audio ID
    owner_id: int  # Audio owner's ID
    title: str  # Title
    url: NotRequired[str]  # URL of mp3 file
    duration: int  # Duration in seconds
    stream_duration: NotRequired[int]  # Stream duration in seconds
    date: NotRequired[int]  # Date when uploaded
    album_id: NotRequired[int]  # Album ID
    performer: NotRequired[str]  # Performer name

class base_city(TypedDict):
    id: int  # City ID
    title: str  # City title

class base_comments_info(TypedDict):
    can_post: NotRequired['base_bool_int']  # Information whether current user can comment the post
    can_open: NotRequired['base_bool_int']
    can_close: NotRequired['base_bool_int']
    can_view: NotRequired['base_bool_int']  # Information whether current user can view the comments
    count: NotRequired[int]  # Comments number
    groups_can_post: NotRequired[Flag]  # Information whether groups can comment the post
    donut: NotRequired['wall_wallpost_comments_donut']
    list: NotRequired[List['wall_wall_comment']]

class base_country(TypedDict):
    id: int  # Country ID
    title: str  # Country title

class base_crop_photo(TypedDict):
    photo: 'photos_photo'
    crop: 'base_crop_photo_crop'
    rect: 'base_crop_photo_rect'

class base_crop_photo_crop(TypedDict):
    x: float  # Coordinate X of the left upper corner
    y: float  # Coordinate Y of the left upper corner
    x2: float  # Coordinate X of the right lower corner
    y2: float  # Coordinate Y of the right lower corner

class base_crop_photo_rect(TypedDict):
    x: float  # Coordinate X of the left upper corner
    y: float  # Coordinate Y of the left upper corner
    x2: float  # Coordinate X of the right lower corner
    y2: float  # Coordinate Y of the right lower corner

class base_error(TypedDict):
    inner_type: Literal['base_error']
    error_code: int  # Error code
    error_subcode: NotRequired[int]  # Error subcode
    error_msg: NotRequired[str]  # Error message
    error_text: NotRequired[str]  # Localized error message
    request_params: NotRequired[List['base_request_param']]

class base_geo(TypedDict):
    coordinates: NotRequired['base_geo_coordinates']
    place: NotRequired['base_place']
    showmap: NotRequired[int]  # Information whether a map is showed
    type: NotRequired[str]  # Place type

class base_geo_coordinates(TypedDict):
    latitude: float
    longitude: float

class base_gradient_point(TypedDict):
    color: str  # Hex color code without #
    position: float  # Point position

class base_image(TypedDict):
    id: NotRequired[str]
    url: str  # Image url
    width: int  # Image width
    height: int  # Image height
    theme: NotRequired[Literal['light', 'dark']]

class base_likes(TypedDict):
    count: NotRequired[int]  # Likes number
    user_likes: NotRequired['base_bool_int']  # Information whether current user likes the photo

class base_likes_info(TypedDict):
    can_like: 'base_bool_int'  # Information whether current user can like the post
    can_publish: NotRequired['base_bool_int']  # Information whether current user can repost
    can_like_as_author: NotRequired['base_bool_int']  # Whether user can like comment as author
    can_like_by_group: NotRequired['base_bool_int']  # Whether current owner of the group can like the reply
    count: int  # Likes number
    user_likes: 'base_bool_int'  # Information whether current uer has liked the post
    author_liked: NotRequired[Flag]  # Information whether post author liked the reply
    group_liked: NotRequired[Flag]  # Information whether group liked the reply
    repost_disabled: NotRequired[Flag]  # Remove repost feature for post

class base_link_application(TypedDict):
    app_id: NotRequired[float]  # Application Id
    store: NotRequired['base_link_application_store']

class base_link_application_store(TypedDict):
    id: NotRequired[float]  # Store Id
    name: NotRequired[str]  # Store name

class base_link_button(TypedDict):
    action: NotRequired['base_link_button_action']  # Button action
    title: NotRequired[str]  # Button title
    block_id: NotRequired[str]  # Target block id
    section_id: NotRequired[str]  # Target section id
    artist_id: NotRequired[str]  # artist id
    curator_id: NotRequired[int]  # curator id
    album_id: NotRequired[int]  # Video album id
    owner_id: NotRequired[int]  # Owner id
    icon: NotRequired[str]  # Button icon name, e.g. 'phone' or 'gift'
    style: NotRequired['base_link_button_style']
    audio_id: NotRequired[int]
    hashtag: NotRequired[str]

class base_link_button_action(TypedDict):
    type: 'base_link_button_action_type'
    url: NotRequired[str]  # Action URL
    consume_reason: NotRequired[str]

class base_link_no_product(TypedDict):
    application: NotRequired['base_link_application']
    button: NotRequired['base_link_button']
    caption: NotRequired[str]  # Link caption
    description: NotRequired[str]  # Link description
    id: NotRequired[str]  # Link ID
    is_favorite: NotRequired[Flag]
    photo: NotRequired['photos_photo']
    preview_page: NotRequired[str]  # String ID of the page with article preview
    preview_url: NotRequired[str]  # URL of the page with article preview
    rating: NotRequired['base_link_rating']
    title: NotRequired[str]  # Link title
    url: str  # Link URL
    target_object: NotRequired['link_target_object']
    is_external: NotRequired[Flag]  # Information whether the current link is external
    video: NotRequired['video_video_full']  # Video from link

class base_link_product(TypedDict):
    price: 'market_price'
    merchant: NotRequired[str]
    category: NotRequired['base_link_product_category']
    geo: NotRequired['base_geo_coordinates']
    distance: NotRequired[int]
    city: NotRequired[str]
    status: NotRequired['base_link_product_status']
    orders_count: NotRequired[int]
    type: NotRequired[Literal['product']]

class base_link_rating(TypedDict):
    reviews_count: NotRequired[int]  # Count of reviews
    stars: NotRequired[float]  # Count of stars
    type: NotRequired[Literal['rating']]

class base_message_error(TypedDict):
    code: NotRequired[int]  # Error code
    description: NotRequired[str]  # Error message

class base_object(TypedDict):
    id: int  # Object ID
    title: str  # Object title

class base_object_count(TypedDict):
    count: NotRequired[int]  # Items count

class base_object_with_name(TypedDict):
    id: int  # Object ID
    name: str  # Object name

class base_owner_cover(TypedDict):
    enabled: 'base_bool_int'  # Information whether cover is enabled
    images: NotRequired[List['base_image']]
    crop_params: NotRequired['base_owner_cover_crop_params']
    original_image: NotRequired['base_image']
    photo_id: NotRequired[int]

class base_owner_cover_crop_params(TypedDict):
    x: NotRequired[int]
    y: NotRequired[int]
    width: NotRequired[int]
    height: NotRequired[int]

class base_place(TypedDict):
    address: NotRequired[str]  # Place address
    checkins: NotRequired[int]  # Checkins number
    country: NotRequired[str]  # Country name
    created: NotRequired[int]  # Date of the place creation in Unixtime
    icon: NotRequired[str]  # URL of the place's icon
    id: NotRequired[int]  # Place ID
    latitude: NotRequired[float]  # Place latitude
    longitude: NotRequired[float]  # Place longitude
    title: NotRequired[str]  # Place title
    type: NotRequired[str]  # Place type

class base_reposts_info(TypedDict):
    '''Count of views'''
    count: int  # Total reposts counter. Sum of wall and mail reposts counters
    wall_count: NotRequired[int]  # Wall reposts counter
    mail_count: NotRequired[int]  # Mail reposts counter
    user_reposted: NotRequired['base_bool_int']  # Information whether current user has reposted the post

class base_request_param(TypedDict):
    key: str  # Parameter name
    value: str  # Parameter value

class base_sticker_animation(TypedDict):
    type: NotRequired[Literal['light', 'dark']]  # Type of animation script
    url: NotRequired[str]  # URL of animation script

class base_sticker_new(TypedDict):
    inner_type: Literal['base_sticker_new']
    sticker_id: NotRequired[int]  # Sticker ID
    product_id: NotRequired[int]  # Pack ID
    images: NotRequired[List['base_image']]
    images_with_background: NotRequired[List['base_image']]
    animation_url: NotRequired[str]  # URL of sticker animation script
    animations: NotRequired[List['base_sticker_animation']]  # Array of sticker animation script objects
    is_allowed: NotRequired[Flag]  # Information whether the sticker is allowed

class base_upload_server(TypedDict):
    upload_url: str  # Upload URL

class base_user_id(TypedDict):
    user_id: NotRequired[int]  # User ID

class board_topic(TypedDict):
    comments: NotRequired[int]  # Comments number
    created: NotRequired[int]  # Date when the topic has been created in Unixtime
    created_by: NotRequired[int]  # Creator ID
    id: NotRequired[int]  # Topic ID
    is_closed: NotRequired['base_bool_int']  # Information whether the topic is closed
    is_fixed: NotRequired['base_bool_int']  # Information whether the topic is fixed
    title: NotRequired[str]  # Topic title
    updated: NotRequired[int]  # Date when the topic has been updated in Unixtime
    updated_by: NotRequired[int]  # ID of user who updated the topic
    first_comment: NotRequired[str]  # First comment text
    last_comment: NotRequired[str]  # Last comment text

class board_topic_comment(TypedDict):
    attachments: NotRequired[List['wall_comment_attachment']]
    date: int  # Date when the comment has been added in Unixtime
    from_id: int  # Author ID
    id: int  # Comment ID
    real_offset: NotRequired[int]  # Real position of the comment
    text: str  # Comment text
    can_edit: NotRequired['base_bool_int']  # Information whether current user can edit the comment
    likes: NotRequired['base_likes_info']

class bugtracker_add_company_groups_members_error(TypedDict):
    group_id: int
    user_id: int

class bugtracker_attachment(TypedDict):
    doc: NotRequired['docs_doc']
    photo: NotRequired['photos_photo']
    type: Literal['photo', 'doc']

class bugtracker_bugreport(TypedDict):
    id: int
    original_id: NotRequired[int]
    clones_count: NotRequired[int]
    title: str
    owner_id: int
    created: int
    updated: int
    description: NotRequired[str]
    state_actual: NotRequired[str]
    state_supposed: NotRequired[str]
    phone: NotRequired[str]
    comments_count: NotRequired[int]
    can_remove: NotRequired[Flag]
    can_change_status: NotRequired[Flag]
    can_bookmark: NotRequired[Flag]
    is_bookmarked: NotRequired[Flag]
    can_edit: NotRequired[Flag]
    is_deleted: NotRequired[Flag]
    can_restore: NotRequired[Flag]
    is_vulnerability: NotRequired[Flag]
    is_severity_by_moderator: NotRequired[Flag]
    hidden_docs: NotRequired[Flag]
    private_comment: NotRequired[str]
    can_change_product: NotRequired[Flag]
    company_id: int
    tournament_score: NotRequired[int]
    moderator_user_id: NotRequired[int]
    moderated: NotRequired[int]

class bugtracker_bugreport_subscribe_state(TypedDict):
    can_set_subscribe: Flag
    is_subscribed: NotRequired[Flag]
    set_subscribe_hash: NotRequired[str]

class bugtracker_comment(TypedDict):
    bugreport_id: int
    comment_id: int
    created: int
    text: str
    meta_text: NotRequired[str]
    from_id: NotRequired[int]
    author_name: NotRequired[str]
    author_photo: NotRequired[str]
    can_edit: NotRequired[Flag]
    can_remove: NotRequired[Flag]
    is_hidden: NotRequired[Flag]
    attachments: NotRequired[List['bugtracker_attachment']]
    is_unread: NotRequired[Flag]

class bugtracker_company_member(TypedDict):
    user_id: int
    company_id: int
    role: int
    role_name: str
    ts: int
    groups_count: int
    products_count: int
    reporter_url: str
    groups: NotRequired[List[int]]
    products: NotRequired[List['bugtracker_company_member_product']]

class bugtracker_company_member_product(TypedDict):
    id: int
    title: NotRequired[str]
    photo_url: NotRequired[str]
    access: int
    status: int
    licence_status_text: NotRequired[str]

class callback_app_payload(TypedDict):
    user_id: int
    app_id: int
    payload: str

class callback_base(TypedDict):
    type: 'callback_type'
    group_id: int
    event_id: str  # Unique event id. If it passed twice or more - you should ignore it.
    v: str  # API object version
    secret: NotRequired[str]

class callback_board_post_delete(TypedDict):
    topic_owner_id: int
    topic_id: int
    id: int
    deleter_id: NotRequired[int]

class callback_donut_money_withdraw(TypedDict):
    amount: float
    amount_without_fee: float

class callback_donut_money_withdraw_error(TypedDict):
    reason: str

class callback_donut_subscription_cancelled(TypedDict):
    user_id: NotRequired[int]

class callback_donut_subscription_create(TypedDict):
    user_id: NotRequired[int]
    amount: int
    amount_without_fee: float

class callback_donut_subscription_expired(TypedDict):
    user_id: NotRequired[int]

class callback_donut_subscription_price_changed(TypedDict):
    user_id: NotRequired[int]
    amount_old: int
    amount_new: int
    amount_diff: NotRequired[float]
    amount_diff_without_fee: NotRequired[float]

class callback_donut_subscription_prolonged(TypedDict):
    user_id: NotRequired[int]
    amount: int
    amount_without_fee: float

class callback_group_change_photo(TypedDict):
    user_id: int
    photo: 'photos_photo'

class callback_group_change_settings(TypedDict):
    user_id: int
    changes: NotRequired['callback_group_settings_changes']

class callback_group_join(TypedDict):
    user_id: int
    join_type: 'callback_group_join_type'

class callback_group_leave(TypedDict):
    user_id: NotRequired[int]
    self: NotRequired['base_bool_int']

class callback_group_officers_edit(TypedDict):
    admin_id: int
    user_id: int
    level_old: 'callback_group_officer_role'
    level_new: 'callback_group_officer_role'

class callback_group_settings_changes(TypedDict):
    title: NotRequired['callback_group_settings_changes_string_values']
    screen_name: NotRequired['callback_group_settings_changes_string_values']
    event_start_date: NotRequired['callback_group_settings_changes_integer_values']
    event_finish_date: NotRequired['callback_group_settings_changes_integer_values']
    event_group_id: NotRequired['callback_group_settings_changes_integer_values']
    donations: NotRequired['callback_group_settings_changes_integer_values']
    wall: NotRequired['callback_group_settings_changes_integer_values']
    replies: NotRequired['callback_group_settings_changes_integer_values']
    topics: NotRequired['callback_group_settings_changes_integer_values']
    photos: NotRequired['callback_group_settings_changes_integer_values']
    docs: NotRequired['callback_group_settings_changes_integer_values']
    messages: NotRequired['callback_group_settings_changes_integer_values']
    market: NotRequired['callback_group_settings_changes_integer_values']
    market_wiki: NotRequired['callback_group_settings_changes_integer_values']
    board: NotRequired['callback_group_settings_changes_integer_values']
    links: NotRequired['callback_group_settings_changes_integer_values']
    audio: NotRequired['callback_group_settings_changes_integer_values']
    video: NotRequired['callback_group_settings_changes_integer_values']
    can_post_topics: NotRequired['callback_group_settings_changes_integer_values']
    can_post_albums: NotRequired['callback_group_settings_changes_integer_values']
    can_post_video: NotRequired['callback_group_settings_changes_integer_values']
    disable_market_comments: NotRequired['callback_group_settings_changes_integer_values']
    status_default: NotRequired['callback_group_settings_changes_integer_values']
    access: NotRequired['callback_group_settings_changes_integer_values']
    email: NotRequired['callback_group_settings_changes_string_values']
    country_id: NotRequired['callback_group_settings_changes_integer_values']
    city_id: NotRequired['callback_group_settings_changes_integer_values']
    address: NotRequired['callback_group_settings_changes_string_values']
    description: NotRequired['callback_group_settings_changes_string_values']
    website: NotRequired['callback_group_settings_changes_string_values']
    phone: NotRequired['callback_group_settings_changes_string_values']
    age_limits: NotRequired['callback_group_settings_changes_integer_values']
    category_v2: NotRequired['callback_group_settings_changes_integer_values']
    public_category: NotRequired['callback_group_settings_changes_integer_values']
    public_subcategory: NotRequired['callback_group_settings_changes_integer_values']

class callback_group_settings_changes_integer_values(TypedDict):
    old_value: NotRequired[int]
    new_value: NotRequired[int]

class callback_group_settings_changes_string_values(TypedDict):
    old_value: NotRequired[str]
    new_value: NotRequired[str]

class callback_info_for_bots(TypedDict):
    button_actions: NotRequired[List['messages_template_action_type_names']]
    keyboard: NotRequired[Flag]  # client has support keyboard
    inline_keyboard: NotRequired[Flag]  # client has support inline keyboard
    carousel: NotRequired[Flag]  # client has support carousel
    lang_id: NotRequired[int]  # client or user language id

class callback_like_add_remove(TypedDict):
    liker_id: int
    object_type: Literal['video', 'photo', 'post', 'comment', 'note', 'topic_comment', 'photo_comment', 'video_comment', 'market', 'market_comment']
    object_owner_id: int
    object_id: int
    post_id: int
    thread_reply_id: NotRequired[int]

class callback_market_comment(TypedDict):
    id: int
    from_id: int
    date: int
    text: NotRequired[str]
    market_owner_id: NotRequired[int]
    photo_id: NotRequired[int]

class callback_market_comment_delete(TypedDict):
    owner_id: int
    id: int
    user_id: int
    item_id: int

class callback_message_allow_object(TypedDict):
    user_id: int
    key: str

class callback_message_deny(TypedDict):
    user_id: int

class callback_message_object(TypedDict):
    client_info: NotRequired['callback_info_for_bots']
    message: NotRequired['messages_message']

class callback_photo_comment_delete(TypedDict):
    id: int
    owner_id: int
    user_id: int
    photo_id: int
    deleter_id: int

class callback_poll_vote_new(TypedDict):
    owner_id: int
    poll_id: int
    option_id: int
    user_id: int

class callback_user_block(TypedDict):
    admin_id: int
    user_id: int
    unblock_date: int
    reason: int
    comment: NotRequired[str]

class callback_user_unblock(TypedDict):
    admin_id: int
    user_id: int
    by_end_date: int

class callback_video_comment_delete(TypedDict):
    id: int
    owner_id: int
    deleter_id: int
    video_id: int

class callback_vkpay_transaction(TypedDict):
    amount: int
    from_id: int
    description: str
    date: int
    payload: NotRequired[str]

class callback_wall_comment_delete(TypedDict):
    owner_id: int
    id: int
    user_id: int
    post_id: int

class calls_call(TypedDict):
    duration: NotRequired[int]  # Call duration
    initiator_id: int  # Caller initiator
    receiver_id: int  # Caller receiver
    state: 'calls_end_state'
    time: int  # Timestamp for call
    video: NotRequired[Flag]  # Was this call initiated as video call
    participants: NotRequired['calls_participants']

class calls_participants(TypedDict):
    list: NotRequired[List[int]]
    count: NotRequired[int]  # Participants count

class client_info_for_bots(TypedDict):
    button_actions: NotRequired[List['messages_template_action_type_names']]
    keyboard: NotRequired[Flag]  # client has support keyboard
    inline_keyboard: NotRequired[Flag]  # client has support inline keyboard
    carousel: NotRequired[Flag]  # client has support carousel
    lang_id: NotRequired[int]  # client or user language id

class comment_thread(TypedDict):
    count: int  # Comments number
    items: NotRequired[List['wall_wall_comment']]
    can_post: NotRequired[Flag]  # Information whether current user can comment the post
    show_reply_button: NotRequired[Flag]  # Information whether recommended to display reply button
    groups_can_post: NotRequired[Flag]  # Information whether groups can comment the post
    author_replied: NotRequired[Flag]  # Information whether author commented the thread

class database_faculty(TypedDict):
    id: NotRequired[int]  # Faculty ID
    title: NotRequired[str]  # Faculty title

class database_language_full(TypedDict):
    id: int  # Language ID
    native_name: str  # Language native name

class database_region(TypedDict):
    id: NotRequired[int]  # Region ID
    title: NotRequired[str]  # Region title

class database_school(TypedDict):
    id: NotRequired[int]  # School ID
    title: NotRequired[str]  # School title

class database_station(TypedDict):
    city_id: NotRequired[int]  # City ID
    color: NotRequired[str]  # Hex color code without #
    id: int  # Station ID
    name: str  # Station name

class database_university(TypedDict):
    id: NotRequired[int]  # University ID
    title: NotRequired[str]  # University title

class docs_doc(TypedDict):
    id: int  # Document ID
    owner_id: int  # Document owner ID
    title: str  # Document title
    size: int  # File size in bites
    ext: str  # File extension
    url: NotRequired[str]  # File URL
    date: int  # Date when file has been uploaded in Unixtime
    type: int  # Document type
    preview: NotRequired['docs_doc_preview']
    is_licensed: NotRequired['base_bool_int']
    access_key: NotRequired[str]  # Access key for the document
    tags: NotRequired[List[str]]  # Document tags

class docs_doc_preview(TypedDict):
    audio_msg: NotRequired['docs_doc_preview_audio_msg']
    graffiti: NotRequired['docs_doc_preview_graffiti']
    photo: NotRequired['docs_doc_preview_photo']
    video: NotRequired['docs_doc_preview_video']

class docs_doc_preview_audio_msg(TypedDict):
    duration: int  # Audio message duration in seconds
    link_mp3: str  # MP3 file URL
    link_ogg: str  # OGG file URL
    waveform: List[int]

class docs_doc_preview_graffiti(TypedDict):
    src: str  # Graffiti file URL
    width: int  # Graffiti width
    height: int  # Graffiti height

class docs_doc_preview_photo(TypedDict):
    sizes: NotRequired[List['docs_doc_preview_photo_sizes']]

class docs_doc_preview_photo_sizes(TypedDict):
    src: str  # URL of the image
    width: int  # Width in px
    height: int  # Height in px
    type: 'photos_photo_sizes_type'

class docs_doc_preview_video(TypedDict):
    src: str  # Video URL
    width: int  # Video's width in pixels
    height: int  # Video's height in pixels
    file_size: int  # Video file size in bites

class docs_doc_types(TypedDict):
    id: int  # Doc type ID
    name: str  # Doc type title
    count: int  # Number of docs

class donut_donator_subscription_info(TypedDict):
    '''Info about user VK Donut subscription'''
    owner_id: int
    next_payment_date: int
    amount: int
    status: Literal['active', 'expiring']

class events_event_attach(TypedDict):
    address: NotRequired[str]  # address of event
    button_text: str  # text of attach
    friends: List[int]  # array of friends ids
    id: int  # event ID
    is_favorite: Flag  # is favorite
    member_status: NotRequired['groups_group_full_member_status']  # Current user's member status
    text: str  # text of attach
    time: NotRequired[int]  # event start time

class fave_bookmark(TypedDict):
    added_date: int  # Timestamp, when this item was bookmarked
    link: NotRequired['base_link']
    post: NotRequired['wall_wallpost_full']
    product: NotRequired['market_market_item']
    seen: Flag  # Has user seen this item
    tags: List['fave_tag']
    type: 'fave_bookmark_type'  # Item type
    video: NotRequired['video_video_full']

class fave_page(TypedDict):
    description: str  # Some info about user or group
    group: NotRequired['groups_group_full']
    tags: List['fave_tag']
    type: 'fave_page_type'  # Item type
    updated_date: NotRequired[int]  # Timestamp, when this page was bookmarked
    user: NotRequired['users_user_full']

class fave_tag(TypedDict):
    id: NotRequired[int]  # Tag id
    name: NotRequired[str]  # Tag name

class friends_friend_status(TypedDict):
    friend_status: 'friends_friend_status_status'
    sign: NotRequired[str]  # MD5 hash for the result validation
    user_id: int  # User ID

class friends_friends_list(TypedDict):
    id: int  # List ID
    name: str  # List title

class friends_mutual_friend(TypedDict):
    common_count: NotRequired[int]  # Total mutual friends number
    common_friends: NotRequired[List[int]]
    id: NotRequired[int]  # User ID

class friends_online_users(TypedDict):
    online: List[int]
    total_count: NotRequired[int]  # Total online friends number

class friends_online_users_with_mobile(TypedDict):
    online: List[int]
    online_mobile: List[int]
    total_count: NotRequired[int]  # Total online friends number

class friends_requests_mutual(TypedDict):
    count: NotRequired[int]  # Total mutual friends number
    users: NotRequired[List[int]]

class gifts_gift(TypedDict):
    date: NotRequired[int]  # Date when gist has been sent in Unixtime
    from_id: NotRequired[int]  # Gift sender ID
    gift: NotRequired['gifts_layout']
    gift_hash: NotRequired[str]  # Hash
    id: NotRequired[int]  # Gift ID
    message: NotRequired[str]  # Comment text
    privacy: NotRequired['gifts_gift_privacy']

class gifts_layout(TypedDict):
    id: NotRequired[int]  # Gift ID
    thumb_512: NotRequired[str]  # URL of the preview image with 512 px in width
    thumb_256: NotRequired[str]  # URL of the preview image with 256 px in width
    thumb_48: NotRequired[str]  # URL of the preview image with 48 px in width
    thumb_96: NotRequired[str]  # URL of the preview image with 96 px in width
    stickers_product_id: NotRequired[int]  # ID of the sticker pack, if the gift is representing one
    is_stickers_style: NotRequired[Flag]  # Information whether gift represents a stickers style
    build_id: NotRequired[str]  # ID of the build of constructor gift
    keywords: NotRequired[str]  # Keywords used for search

class groups_address(TypedDict):
    additional_address: NotRequired[str]  # Additional address to the place (6 floor, left door)
    address: NotRequired[str]  # String address to the place (Nevsky, 28)
    city_id: NotRequired[int]  # City id of address
    city: NotRequired['database_city_by_id']  # City for address
    metro_station: NotRequired['database_station']  # Metro for address
    country: NotRequired['base_country']  # Country for address
    distance: NotRequired[int]  # Distance from the point
    id: int  # Address id
    latitude: NotRequired[float]  # Address latitude
    longitude: NotRequired[float]  # Address longitude
    metro_station_id: NotRequired[int]  # Metro id of address
    phone: NotRequired[str]  # Address phone
    time_offset: NotRequired[int]  # Time offset int minutes from utc time
    timetable: NotRequired['groups_address_timetable']  # Week timetable for the address
    title: NotRequired[str]  # Title of the place (Zinger, etc)
    work_info_status: NotRequired['groups_address_work_info_status']  # Status of information about timetable
    place_id: NotRequired[int]

class groups_address_timetable(TypedDict):
    '''Timetable for a week'''
    fri: NotRequired['groups_address_timetable_day']  # Timetable for friday
    mon: NotRequired['groups_address_timetable_day']  # Timetable for monday
    sat: NotRequired['groups_address_timetable_day']  # Timetable for saturday
    sun: NotRequired['groups_address_timetable_day']  # Timetable for sunday
    thu: NotRequired['groups_address_timetable_day']  # Timetable for thursday
    tue: NotRequired['groups_address_timetable_day']  # Timetable for tuesday
    wed: NotRequired['groups_address_timetable_day']  # Timetable for wednesday

class groups_address_timetable_day(TypedDict):
    '''Timetable for one day'''
    break_close_time: NotRequired[int]  # Close time of the break in minutes
    break_open_time: NotRequired[int]  # Start time of the break in minutes
    close_time: int  # Close time in minutes
    open_time: int  # Open time in minutes

class groups_addresses_info(TypedDict):
    is_enabled: Flag  # Information whether addresses is enabled
    main_address_id: NotRequired[int]  # Main address id for group
    main_address: NotRequired['groups_address']  # Main address
    count: NotRequired[int]  # Count of addresses

class groups_ban_info(TypedDict):
    admin_id: NotRequired[int]  # Administrator ID
    comment: NotRequired[str]  # Comment for a ban
    comment_visible: NotRequired[Flag]  # Show comment for user
    is_closed: NotRequired[Flag]
    date: NotRequired[int]  # Date when user has been added to blacklist in Unixtime
    end_date: NotRequired[int]  # Date when user will be removed from blacklist in Unixtime
    reason: NotRequired['groups_ban_info_reason']

class groups_callback_server(TypedDict):
    id: int
    title: str
    creator_id: int
    url: str
    secret_key: str
    status: Literal['unconfigured', 'failed', 'wait', 'ok']

class groups_callback_settings(TypedDict):
    api_version: NotRequired[str]  # API version used for the events
    events: NotRequired['groups_long_poll_events']

class groups_contacts_item(TypedDict):
    user_id: NotRequired[int]  # User ID
    desc: NotRequired[str]  # Contact description
    phone: NotRequired[str]  # Contact phone
    email: NotRequired[str]  # Contact email

class groups_counters_group(TypedDict):
    addresses: NotRequired[int]  # Addresses number
    albums: NotRequired[int]  # Photo albums number
    audios: NotRequired[int]  # Audios number
    audio_playlists: NotRequired[int]  # Audio playlists number
    docs: NotRequired[int]  # Docs number
    market: NotRequired[int]  # Market items number
    photos: NotRequired[int]  # Photos number
    topics: NotRequired[int]  # Topics number
    videos: NotRequired[int]  # Videos number
    video_playlists: NotRequired[int]  # Playlists number
    market_services: NotRequired[int]  # Market services number
    podcasts: NotRequired[int]  # Podcasts number
    articles: NotRequired[int]  # Articles number
    narratives: NotRequired[int]  # Narratives number
    clips: NotRequired[int]  # Clips number
    clips_followers: NotRequired[int]  # Clips followers number
    videos_followers: NotRequired[int]  # Videos followers number
    clips_views: NotRequired[int]  # Clips views number
    clips_likes: NotRequired[int]  # Clips likes number

class groups_group(TypedDict):
    id: int  # Community ID
    name: NotRequired[str]  # Community name
    screen_name: NotRequired[str]  # Domain of the community page
    is_closed: NotRequired['groups_group_is_closed']
    type: NotRequired['groups_group_type']
    is_admin: NotRequired['base_bool_int']  # Information whether current user is administrator
    admin_level: NotRequired['groups_group_admin_level']
    is_member: NotRequired['base_bool_int']  # Information whether current user is member
    is_advertiser: NotRequired['base_bool_int']  # Information whether current user is advertiser
    start_date: NotRequired[int]  # Start date in Unixtime format
    finish_date: NotRequired[int]  # Finish date in Unixtime format
    verified: NotRequired['base_bool_int']  # Information whether community is verified
    deactivated: NotRequired[str]  # Information whether community is banned
    photo_50: NotRequired[str]  # URL of square photo of the community with 50 pixels in width
    photo_100: NotRequired[str]  # URL of square photo of the community with 100 pixels in width
    photo_200: NotRequired[str]  # URL of square photo of the community with 200 pixels in width
    photo_200_orig: NotRequired[str]  # URL of square photo of the community with 200 pixels in width original
    photo_400: NotRequired[str]  # URL of square photo of the community with 400 pixels in width
    photo_400_orig: NotRequired[str]  # URL of square photo of the community with 400 pixels in width original
    photo_max: NotRequired[str]  # URL of square photo of the community with max pixels in width
    photo_max_orig: NotRequired[str]  # URL of square photo of the community with max pixels in width original
    est_date: NotRequired[str]  # Established date
    public_date_label: NotRequired[str]  # Public date label
    photo_max_size: NotRequired['groups_photo_size']
    is_video_live_notifications_blocked: NotRequired['base_bool_int']
    video_live: NotRequired['video_live_info']

class groups_group_attach(TypedDict):
    id: int  # group ID
    text: str  # text of attach
    status: str  # activity or category of group
    size: int  # size of group
    is_favorite: Flag  # is favorite

class groups_group_ban_info(TypedDict):
    comment: NotRequired[str]  # Ban comment
    end_date: NotRequired[int]  # End date of ban in Unixtime
    reason: NotRequired['groups_ban_info_reason']

class groups_group_category(TypedDict):
    id: int  # Category ID
    name: str  # Category name
    subcategories: NotRequired[List['groups_group_subcategory']]

class groups_group_category_full(TypedDict):
    id: int  # Category ID
    name: str  # Category name
    page_count: int  # Pages number
    page_previews: List['groups_group']
    subcategories: NotRequired[List['groups_group_category']]

class groups_group_category_type(TypedDict):
    id: int
    name: str

class groups_group_public_category_list(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    subcategories: NotRequired[List['groups_group_category_type']]

class groups_group_subcategory(TypedDict):
    id: int  # Object ID
    name: str  # Object name
    genders: NotRequired[List['base_object_with_name']]

class groups_group_tag(TypedDict):
    id: int
    name: str
    color: Literal['454647', '45678f', '4bb34b', '5181b8', '539b9c', '5c9ce6', '63b9ba', '6bc76b', '76787a', '792ec0', '7a6c4f', '7ececf', '9e8d6b', 'a162de', 'aaaeb3', 'bbaa84', 'e64646', 'ff5c5c', 'ffa000', 'ffc107']
    uses: NotRequired[int]

class groups_groups_array(TypedDict):
    count: int  # Communities number
    items: List[int]

class groups_links_item(TypedDict):
    name: NotRequired[str]  # Link title
    desc: NotRequired[str]  # Link description
    edit_title: NotRequired['base_bool_int']  # Information whether the link title can be edited
    id: NotRequired[int]  # Link ID
    photo_100: NotRequired[str]  # URL of square image of the link with 100 pixels in width
    photo_50: NotRequired[str]  # URL of square image of the link with 50 pixels in width
    url: NotRequired[str]  # Link URL
    image_processing: NotRequired['base_bool_int']  # Information whether the image on processing

class groups_live_covers(TypedDict):
    is_enabled: Flag  # Information whether live covers is enabled
    is_scalable: NotRequired[Flag]  # Information whether live covers photo scaling is enabled
    story_ids: NotRequired[List[str]]

class groups_long_poll_events(TypedDict):
    audio_new: 'base_bool_int'
    board_post_delete: 'base_bool_int'
    board_post_edit: 'base_bool_int'
    board_post_new: 'base_bool_int'
    board_post_restore: 'base_bool_int'
    group_change_photo: 'base_bool_int'
    group_change_settings: 'base_bool_int'
    group_join: 'base_bool_int'
    group_leave: 'base_bool_int'
    group_officers_edit: 'base_bool_int'
    lead_forms_new: NotRequired['base_bool_int']
    market_comment_delete: 'base_bool_int'
    market_comment_edit: 'base_bool_int'
    market_comment_new: 'base_bool_int'
    market_comment_restore: 'base_bool_int'
    market_order_new: NotRequired['base_bool_int']
    market_order_edit: NotRequired['base_bool_int']
    message_allow: 'base_bool_int'
    message_deny: 'base_bool_int'
    message_new: 'base_bool_int'
    message_read: 'base_bool_int'
    message_reply: 'base_bool_int'
    message_typing_state: 'base_bool_int'
    message_edit: 'base_bool_int'
    photo_comment_delete: 'base_bool_int'
    photo_comment_edit: 'base_bool_int'
    photo_comment_new: 'base_bool_int'
    photo_comment_restore: 'base_bool_int'
    photo_new: 'base_bool_int'
    poll_vote_new: 'base_bool_int'
    user_block: 'base_bool_int'
    user_unblock: 'base_bool_int'
    video_comment_delete: 'base_bool_int'
    video_comment_edit: 'base_bool_int'
    video_comment_new: 'base_bool_int'
    video_comment_restore: 'base_bool_int'
    video_new: 'base_bool_int'
    message_reaction_event: 'base_bool_int'
    wall_post_new: 'base_bool_int'
    wall_reply_delete: 'base_bool_int'
    wall_reply_edit: 'base_bool_int'
    wall_reply_new: 'base_bool_int'
    wall_reply_restore: 'base_bool_int'
    wall_repost: 'base_bool_int'
    wall_schedule_post_new: 'base_bool_int'
    wall_schedule_post_delete: 'base_bool_int'
    donut_subscription_create: 'base_bool_int'
    donut_subscription_prolonged: 'base_bool_int'
    donut_subscription_cancelled: 'base_bool_int'
    donut_subscription_expired: 'base_bool_int'
    donut_subscription_price_changed: 'base_bool_int'
    donut_money_withdraw: 'base_bool_int'
    donut_money_withdraw_error: 'base_bool_int'

class groups_long_poll_server(TypedDict):
    key: str  # Long Poll key
    server: str  # Long Poll server address
    ts: str  # Number of the last event

class groups_long_poll_settings(TypedDict):
    api_version: NotRequired[str]  # API version used for the events
    events: 'groups_long_poll_events'
    is_enabled: Flag  # Shows whether Long Poll is enabled

class groups_market_info(TypedDict):
    type: NotRequired[str]  # Market type
    contact_id: NotRequired[int]  # Contact person ID
    currency: NotRequired['market_currency']
    currency_text: NotRequired[str]  # Currency name
    is_show_header_items_link: NotRequired['base_bool_int']  # Shop header items link is enabled
    enabled: NotRequired['base_bool_int']  # Information whether the market is enabled
    main_album_id: NotRequired[int]  # Main market album ID
    price_max: NotRequired[str]  # Maximum price
    price_min: NotRequired[str]  # Minimum price
    min_order_price: NotRequired['market_price']

class groups_market_properties(TypedDict):
    market: NotRequired['groups_market_info']
    has_market_app: NotRequired[Flag]  # Information whether community has installed market app
    using_vkpay_market_app: NotRequired[Flag]

class groups_member_role(TypedDict):
    id: int  # User ID
    is_call_operator: NotRequired[Flag]  # Allow the manager to accept community calls.
    permissions: NotRequired[List['groups_member_role_permission']]
    role: NotRequired['groups_member_role_status']

class groups_member_status(TypedDict):
    member: 'base_bool_int'  # Information whether user is a member of the group
    user_id: int  # User ID

class groups_member_status_full(TypedDict):
    can_invite: NotRequired['base_bool_int']  # Information whether user can be invited
    can_recall: NotRequired['base_bool_int']  # Information whether user's invite to the group can be recalled
    invitation: NotRequired['base_bool_int']  # Information whether user has been invited to the group
    member: 'base_bool_int'  # Information whether user is a member of the group
    request: NotRequired['base_bool_int']  # Information whether user has send request to the group
    user_id: int  # User ID

class groups_online_status(TypedDict):
    '''Online status of group'''
    minutes: NotRequired[int]  # Estimated time of answer (for status = answer_mark)
    status: 'groups_online_status_type'

class groups_owner_xtr_ban_info(TypedDict):
    ban_info: NotRequired['groups_ban_info']
    group: NotRequired['groups_group']  # Information about group if type = group
    profile: NotRequired['users_user']  # Information about group if type = profile
    type: NotRequired[Literal['group', 'profile']]

class groups_photo_size(TypedDict):
    height: int  # Image height
    width: int  # Image width

class groups_profile_item(TypedDict):
    id: int  # User id
    photo_50: str  # Url for user photo
    photo_100: str  # Url for user photo
    first_name: str  # User first name

class groups_settings_twitter(TypedDict):
    status: Literal['loading', 'sync']
    name: NotRequired[str]

class groups_subject_item(TypedDict):
    id: int  # Subject ID
    name: str  # Subject title

class groups_token_permission_setting(TypedDict):
    name: str
    setting: int

class leadForms_answer(TypedDict):
    key: str
    answer: 'leadForms_answer_one_of'

class leadForms_answer_item(TypedDict):
    key: NotRequired[str]
    value: str

class leadForms_form(TypedDict):
    form_id: int
    group_id: int
    photo: NotRequired[str]
    name: NotRequired[str]
    title: NotRequired[str]
    description: NotRequired[str]
    confirmation: NotRequired[str]
    site_link_url: NotRequired[str]
    policy_link_url: NotRequired[str]
    questions: NotRequired[List['leadForms_question_item']]
    active: NotRequired['base_bool_int']
    leads_count: int
    pixel_code: NotRequired[str]
    once_per_user: NotRequired[int]
    notify_admins: NotRequired[str]
    notify_emails: NotRequired[str]
    url: str

class leadForms_lead(TypedDict):
    lead_id: int
    user_id: int
    date: int
    answers: List['leadForms_answer']
    ad_id: NotRequired[int]

class leadForms_question_item(TypedDict):
    key: str
    type: Literal['input', 'textarea', 'radio', 'checkbox', 'select']
    label: NotRequired[str]
    options: NotRequired[List['leadForms_question_item_option']]  # Опции выбора для типов radio, checkbox, select

class leadForms_question_item_option(TypedDict):
    key: NotRequired[str]
    label: str

class link_target_object(TypedDict):
    type: NotRequired[str]  # Object type
    owner_id: NotRequired[int]  # Owner ID
    item_id: NotRequired[int]  # Item ID

class market_currency(TypedDict):
    id: int  # Currency ID
    name: str  # Currency sign
    title: str  # Currency title

class market_global_search_filters(TypedDict):
    city: NotRequired['base_city']
    country: NotRequired['base_country']

class market_item_owner_info(TypedDict):
    '''Information about the group where the item is placed'''
    avatar: NotRequired[List['base_image']]  # Avatar of the group
    name: NotRequired[str]  # Name of the group
    category: NotRequired[str]  # Category of the item or description of the group
    category_url: NotRequired[str]  # Link to the section of the group
    is_corporated_market: NotRequired[Flag]  # Is the group is VK corporated market
    market_type: NotRequired['market_owner_type']  # Type of the market group

class market_item_promotion_info(TypedDict):
    '''Information about promotion of the market item'''
    is_available: NotRequired[Flag]  # Can the item be promoted?

class market_market_album(TypedDict):
    id: int  # Market album ID
    owner_id: int  # Market album owner's ID
    title: str  # Market album title
    count: int  # Items number
    is_main: NotRequired[Flag]  # Is album main for owner
    is_hidden: NotRequired[Flag]  # Is album hidden
    photo: NotRequired['photos_photo']
    updated_time: int  # Date when album has been updated last time in Unixtime
    type: NotRequired[Literal[0, 1]]  # Type of album
    is_blur_enabled: NotRequired[Flag]  # Is album needed to be blurred (18+) or not

class market_market_category_nested(TypedDict):
    inner_type: Literal['market_market_category_nested']
    id: int  # Category ID
    name: str  # Category name
    is_v2: NotRequired[Flag]  # Is v2 category
    parent: NotRequired['market_market_category_nested']

class market_market_category_tree(TypedDict):
    id: int  # Category ID
    name: str  # Category name
    icon_name: NotRequired[str]  # Icon name
    children: NotRequired[List['market_market_category_tree']]
    view: NotRequired['market_market_category_tree_view']
    url: NotRequired[str]  # SEO-friendly URL to page with category's items
    seo_name: NotRequired[str]  # SEO-friendly variant of category's name
    page_title: NotRequired[str]  # Title for category's page. Used for SEO
    page_description: NotRequired[str]  # Description for category's page. Used for SEO

class market_market_category_tree_view(TypedDict):
    type: NotRequired[Literal['tab_root']]
    selected: NotRequired[Flag]
    root_path: NotRequired[List[str]]

class market_market_item(TypedDict):
    access_key: NotRequired[str]  # Access key for the market item
    availability: 'market_market_item_availability'
    button_title: NotRequired[str]  # Title for button for url
    category: 'market_market_category'
    category_v2: NotRequired['market_market_category']
    date: NotRequired[int]  # Date when the item has been created in Unixtime
    description: str  # Item description
    external_id: NotRequired[str]
    id: int  # Item ID
    is_favorite: NotRequired[Flag]
    owner_id: int  # Item owner's ID
    is_owner: NotRequired[Flag]
    is_adult: NotRequired[Flag]
    price: 'market_price'
    thumb_photo: NotRequired[str]  # URL of the preview image
    title: str  # Item title
    url: NotRequired[str]  # URL to item
    variants_grouping_id: NotRequired[int]
    is_main_variant: NotRequired[Flag]
    sku: NotRequired[str]
    stock_amount: NotRequired[int]  # Inventory balances
    post_id: NotRequired[int]  # Attach for post id
    post_owner_id: NotRequired[int]  # Attach for post owner id

class market_market_item_basic(TypedDict):
    id: int  # Item ID
    owner_id: int  # Item owner's ID
    title: str  # Item title
    price: 'market_price'
    thumb_photo: NotRequired[str]  # URL of the preview image
    is_favorite: NotRequired[Flag]

class market_order(TypedDict):
    id: int
    group_id: int
    user_id: int
    display_order_id: NotRequired[str]
    date: int
    status: int
    items_count: int
    track_number: NotRequired[str]
    track_link: NotRequired[str]
    comment: NotRequired[str]
    address: NotRequired[str]
    merchant_comment: NotRequired[str]
    weight: NotRequired[int]
    total_price: 'market_price'
    discount: NotRequired['market_price']
    preview_order_items: NotRequired[List['market_order_item']]  # Several order items for preview
    cancel_info: NotRequired['base_link']  # Information for cancel and revert order
    comment_for_user: NotRequired[str]  # Seller comment for user
    is_viewed_by_admin: NotRequired[Flag]
    date_viewed: NotRequired[int]
    can_add_review: NotRequired[Flag]  # Extended field. Can current viewer add review for at least one item in this order

class market_order_item(TypedDict):
    owner_id: int
    item_id: int
    price: 'market_price'
    quantity: int
    item: 'market_market_item'
    title: NotRequired[str]
    photo: NotRequired['photos_photo']
    variants: NotRequired[List[str]]
    can_add_review: NotRequired[Flag]  # Extended field. Can current viewer add review for this ordered item

class market_price(TypedDict):
    amount: str  # Amount
    amount_to: NotRequired[str]  # Amount to for price_type=2
    price_type: NotRequired[Literal[0, 2, 3]]
    price_unit: NotRequired[Literal[0, 2, 3, 4]]
    currency: 'market_currency'
    discount_rate: NotRequired[int]
    old_amount: NotRequired[str]
    text: str  # Text
    old_amount_text: NotRequired[str]  # Textual representation of old price

class market_property(TypedDict):
    id: int
    title: str  # Property name
    type: NotRequired[Literal['text', 'color']]  # Property type
    variants: List['market_property_variant']

class market_property_variant(TypedDict):
    id: int
    title: str  # Property name
    value: NotRequired[str]  # Property value corresponding to property type

class messages_audio_message(TypedDict):
    access_key: NotRequired[str]  # Access key for audio message
    transcript_error: NotRequired[int]
    duration: int  # Audio message duration in seconds
    id: int  # Audio message ID
    link_mp3: str  # MP3 file URL
    link_ogg: str  # OGG file URL
    owner_id: int  # Audio message owner ID
    waveform: List[int]

class messages_chat(TypedDict):
    admin_id: int  # Chat creator ID
    id: int  # Chat ID
    kicked: NotRequired['base_bool_int']  # Shows that user has been kicked from the chat
    left: NotRequired['base_bool_int']  # Shows that user has been left the chat
    photo_100: NotRequired[str]  # URL of the preview image with 100 px in width
    photo_200: NotRequired[str]  # URL of the preview image with 200 px in width
    photo_50: NotRequired[str]  # URL of the preview image with 50 px in width
    push_settings: NotRequired['messages_chat_push_settings']
    title: NotRequired[str]  # Chat title
    type: str  # Chat type
    users: List[int]
    is_default_photo: NotRequired[Flag]  # If provided photo is default
    members_count: int  # Count members in a chat
    is_group_channel: NotRequired[Flag]  # If chat is group channel

class messages_chat_full(TypedDict):
    admin_id: int  # Chat creator ID
    id: int  # Chat ID
    kicked: NotRequired['base_bool_int']  # Shows that user has been kicked from the chat
    left: NotRequired['base_bool_int']  # Shows that user has been left the chat
    photo_100: NotRequired[str]  # URL of the preview image with 100 px in width
    photo_200: NotRequired[str]  # URL of the preview image with 200 px in width
    photo_50: NotRequired[str]  # URL of the preview image with 50 px in width
    push_settings: NotRequired['messages_chat_push_settings']
    title: NotRequired[str]  # Chat title
    type: str  # Chat type
    users: List['messages_user_xtr_invited_by']
    is_default_photo: NotRequired[Flag]  # If provided photo is default
    members_count: int  # Count members in a chat
    is_group_channel: NotRequired[Flag]  # If chat is group channel

class messages_chat_preview(TypedDict):
    admin_id: NotRequired[int]
    joined: NotRequired[Flag]
    local_id: NotRequired[int]
    members: NotRequired[List[int]]
    members_count: NotRequired[int]
    title: NotRequired[str]
    is_member: NotRequired[Flag]
    photo: NotRequired['messages_chat_settings_photo']
    is_don: NotRequired[Flag]
    is_nft: NotRequired[Flag]
    is_group_channel: NotRequired[Flag]
    button: NotRequired['base_link_button']

class messages_chat_push_settings(TypedDict):
    disabled_until: NotRequired[int]  # Time until that notifications are disabled
    sound: NotRequired['base_bool_int']  # Information whether the sound is on

class messages_chat_restrictions(TypedDict):
    admins_promote_users: NotRequired[Flag]  # Only admins can promote users to admins
    only_admins_edit_info: NotRequired[Flag]  # Only admins can change chat info
    only_admins_edit_pin: NotRequired[Flag]  # Only admins can edit pinned message
    only_admins_invite: NotRequired[Flag]  # Only admins can invite users to this chat
    only_admins_kick: NotRequired[Flag]  # Only admins can kick users from this chat

class messages_chat_settings(TypedDict):
    members_count: NotRequired[int]
    friends_count: NotRequired[int]
    owner_id: int
    title: str  # Chat title
    pinned_messages_count: NotRequired[int]
    pinned_message: NotRequired['messages_pinned_message']
    state: 'messages_chat_settings_state'
    photo: NotRequired['messages_chat_settings_photo']
    admin_ids: NotRequired[List[int]]  # Ids of chat admins
    active_ids: NotRequired[List[int]]
    is_group_channel: NotRequired[Flag]
    acl: 'messages_chat_settings_acl'
    permissions: NotRequired['messages_chat_settings_permissions']
    is_disappearing: NotRequired[Flag]
    theme: NotRequired[str]
    disappearing_chat_link: NotRequired[str]
    is_service: NotRequired[Flag]

class messages_chat_settings_acl(TypedDict):
    can_change_info: Flag  # Can you change photo, description and name
    can_change_invite_link: Flag  # Can you change invite link for this chat
    can_change_pin: Flag  # Can you pin/unpin message for this chat
    can_invite: Flag  # Can you invite other peers in chat
    can_promote_users: Flag  # Can you promote simple users to chat admins
    can_see_invite_link: Flag  # Can you see invite link for this chat
    can_moderate: Flag  # Can you moderate (delete) other users' messages
    can_copy_chat: Flag  # Can you copy chat
    can_call: Flag  # Can you init group call in the chat
    can_use_mass_mentions: Flag  # Can you use mass mentions
    can_change_service_type: NotRequired[Flag]  # Can you change chat service type

class messages_chat_settings_permissions(TypedDict):
    invite: NotRequired[Literal['owner', 'owner_and_admins', 'all']]  # Who can invite users to chat
    change_info: NotRequired[Literal['owner', 'owner_and_admins', 'all']]  # Who can change chat info
    change_pin: NotRequired[Literal['owner', 'owner_and_admins', 'all']]  # Who can change pinned message
    use_mass_mentions: NotRequired[Literal['owner', 'owner_and_admins', 'all']]  # Who can use mass mentions
    see_invite_link: NotRequired[Literal['owner', 'owner_and_admins', 'all']]  # Who can see invite link
    call: NotRequired[Literal['owner', 'owner_and_admins', 'all']]  # Who can make calls
    change_admins: NotRequired[Literal['owner', 'owner_and_admins']]  # Who can change admins

class messages_chat_settings_photo(TypedDict):
    photo_50: NotRequired[str]  # URL of the preview image with 50px in width
    photo_100: NotRequired[str]  # URL of the preview image with 100px in width
    photo_200: NotRequired[str]  # URL of the preview image with 200px in width
    is_default_photo: NotRequired[Flag]  # If provided photo is default
    is_default_call_photo: NotRequired[Flag]  # If provided photo is default call photo

class messages_conversation(TypedDict):
    peer: 'messages_conversation_peer'
    sort_id: NotRequired['messages_conversation_sort_id']
    last_message_id: int  # ID of the last message in conversation
    last_conversation_message_id: int  # Conversation message ID of the last message in conversation
    in_read: int  # Last message user have read
    out_read: int  # Last outcoming message have been read by the opponent
    unread_count: NotRequired[int]  # Unread messages number
    is_marked_unread: NotRequired[Flag]  # Is this conversation unread
    out_read_by: NotRequired['messages_out_read_by']
    important: NotRequired[Flag]
    unanswered: NotRequired[Flag]
    special_service_type: NotRequired[Literal['business_notify']]
    message_request_data: NotRequired['messages_message_request_data']
    mentions: NotRequired[List[int]]  # Ids of messages with mentions
    current_keyboard: NotRequired['messages_keyboard']
    push_settings: NotRequired['messages_push_settings']
    can_write: NotRequired['messages_conversation_can_write']
    chat_settings: NotRequired['messages_chat_settings']
    version: int

class messages_conversation_can_write(TypedDict):
    allowed: Flag
    reason: NotRequired[int]
    until: NotRequired[int]

class messages_conversation_member(TypedDict):
    can_kick: NotRequired[Flag]  # Is it possible for user to kick this member
    is_restricted_to_write: NotRequired[Flag]  # Does this member have write permission
    invited_by: NotRequired[int]
    is_admin: NotRequired[Flag]
    is_owner: NotRequired[Flag]
    is_message_request: NotRequired[Flag]
    join_date: NotRequired[int]
    request_date: NotRequired[int]  # Message request date
    member_id: int

class messages_conversation_peer(TypedDict):
    id: int
    local_id: NotRequired[int]
    type: 'messages_conversation_peer_type'

class messages_conversation_sort_id(TypedDict):
    major_id: int  # Major id for sorting conversations
    minor_id: int  # Minor id for sorting conversations

class messages_conversation_with_message(TypedDict):
    conversation: 'messages_conversation'
    last_message: NotRequired['messages_message']

class messages_delete_full_response_item(TypedDict):
    peer_id: NotRequired[int]
    message_id: NotRequired[int]
    conversation_message_id: NotRequired[int]
    response: NotRequired['base_bool_int']
    error: NotRequired['base_message_error']

class messages_foreign_message(TypedDict):
    attachments: NotRequired[List['messages_message_attachment']]
    conversation_message_id: int  # Conversation message ID
    date: int  # Date when the message was created
    from_id: int  # Message author's ID
    fwd_messages: NotRequired[List['messages_foreign_message']]
    geo: NotRequired['base_geo']
    id: NotRequired[int]  # Message ID
    peer_id: NotRequired[int]  # Peer ID
    reply_message: NotRequired['messages_foreign_message']
    text: str  # Message text
    update_time: NotRequired[int]  # Date when the message has been updated in Unixtime
    was_listened: NotRequired[Flag]  # Was the audio message inside already listened by you
    payload: NotRequired[str]  # Additional data sent along with message for developer convenience

class messages_forward(TypedDict):
    owner_id: NotRequired[int]  # Messages owner_id
    peer_id: NotRequired[int]  # Messages peer_id
    conversation_message_ids: NotRequired[List[int]]
    cmids: NotRequired[List[int]]
    message_ids: NotRequired[List[int]]
    is_reply: NotRequired[Flag]  # If you need to reply to a message

class messages_getConversationById(TypedDict):
    count: int  # Total number
    items: List['messages_conversation']

class messages_getConversationMembers(TypedDict):
    items: List['messages_conversation_member']
    count: int  # Chat members count
    chat_restrictions: NotRequired['messages_chat_restrictions']
    profiles: NotRequired[List['users_user_full']]
    groups: NotRequired[List['groups_group_full']]

class messages_getInviteLink_by_owner_response_item(TypedDict):
    owner_id: int
    link: NotRequired[str]
    error: NotRequired['base_message_error']

class messages_graffiti(TypedDict):
    access_key: NotRequired[str]  # Access key for graffiti
    id: int  # Graffiti ID
    owner_id: int  # Graffiti owner ID
    url: str  # Graffiti URL
    width: int  # Graffiti width
    height: int  # Graffiti height

class messages_history_attachment(TypedDict):
    attachment: 'messages_history_message_attachment'
    date: int  # Message sending time
    message_id: int  # Message ID
    message_expire_ttl: NotRequired[int]  # Message Exipire ttl
    cmid: int  # Conversation Message ID
    from_id: int  # Message author's ID
    forward_level: NotRequired[int]  # Forward level (optional)
    was_listened: NotRequired[Flag]
    position: NotRequired[int]  # Attachment position in the Message

class messages_history_message_attachment(TypedDict):
    audio: NotRequired['audio_audio']
    audio_message: NotRequired['messages_audio_message']
    doc: NotRequired['docs_doc']
    graffiti: NotRequired['messages_graffiti']
    market: NotRequired['market_market_item']
    photo: NotRequired['photos_photo']
    type: 'messages_history_message_attachment_type'

class messages_keyboard(TypedDict):
    one_time: Flag  # Should this keyboard disappear on first use
    buttons: 'messages_keyboard_button'
    author_id: NotRequired[int]  # Community or bot, which set this keyboard
    inline: NotRequired[Flag]

class messages_keyboard_button(TypedDict):
    action: 'messages_keyboard_button_property_action'
    color: NotRequired[Literal['default', 'positive', 'negative', 'primary']]  # Button color

class messages_keyboard_button_action_callback(TypedDict):
    '''Description of the action, that should be performed on button click'''
    label: str  # Label for button
    payload: NotRequired[str]  # Additional data sent along with message for developer convenience
    type: Literal['callback']

class messages_keyboard_button_action_location(TypedDict):
    '''Description of the action, that should be performed on button click'''
    payload: NotRequired[str]  # Additional data sent along with message for developer convenience
    type: Literal['location']

class messages_keyboard_button_action_open_app(TypedDict):
    '''Description of the action, that should be performed on button click'''
    app_id: int  # Fragment value in app link like vk.ru/app{app_id}_-654321#hash
    hash: NotRequired[str]  # Fragment value in app link like vk.ru/app123456_-654321#{hash}
    label: str  # Label for button
    owner_id: int  # Fragment value in app link like vk.ru/app123456_{owner_id}#hash
    payload: NotRequired[str]  # Additional data sent along with message for developer convenience
    type: Literal['open_app']

class messages_keyboard_button_action_open_link(TypedDict):
    '''Description of the action, that should be performed on button click'''
    label: str  # Label for button
    link: str  # link for button
    payload: NotRequired[str]  # Additional data sent along with message for developer convenience
    type: Literal['open_link']

class messages_keyboard_button_action_open_photo(TypedDict):
    '''Description of the action, that should be performed on button click'''
    type: Literal['open_photo']

class messages_keyboard_button_action_text(TypedDict):
    '''Description of the action, that should be performed on button click'''
    label: str  # Label for button
    payload: NotRequired[str]  # Additional data sent along with message for developer convenience
    type: Literal['text']

class messages_keyboard_button_action_vkpay(TypedDict):
    '''Description of the action, that should be performed on button click'''
    hash: str  # Fragment value in app link like vk.ru/app123456_-654321#{hash}
    payload: NotRequired[str]  # Additional data sent along with message for developer convenience
    type: Literal['vkpay']

class messages_last_activity(TypedDict):
    online: 'base_bool_int'  # Information whether user is online
    time: int  # Time when user was online in Unixtime

class messages_longpoll_messages(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['messages_message']]

class messages_longpoll_params(TypedDict):
    server: str  # Server URL
    key: str  # Key
    ts: int  # Timestamp
    pts: NotRequired[int]  # Persistent timestamp

class messages_message(TypedDict):
    action: NotRequired['messages_action_one_of']
    admin_author_id: NotRequired[int]  # Only for messages from community. Contains user ID of community admin, who sent this message.
    attachments: NotRequired[List['messages_message_attachment']]
    conversation_message_id: int  # Unique auto-incremented number for all messages with this peer
    date: int  # Date when the message has been sent in Unixtime
    deleted: NotRequired['base_bool_int']  # Is it an deleted message
    from_id: int  # Message author's ID
    fwd_messages: NotRequired['messages_fwd_messages']
    geo: NotRequired['base_geo']
    id: int  # Message ID
    important: NotRequired[Flag]  # Is it an important message
    is_hidden: NotRequired[Flag]
    is_cropped: NotRequired[Flag]  # this message is cropped for bot
    keyboard: NotRequired['messages_keyboard']
    members_count: NotRequired[int]  # Members number
    out: 'base_bool_int'  # Information whether the message is outcoming
    payload: NotRequired[str]
    peer_id: int  # Peer ID
    random_id: NotRequired[int]  # ID used for sending messages. It returned only for outgoing messages
    ref: NotRequired[str]
    ref_source: NotRequired[str]
    reply_message: NotRequired['messages_foreign_message']
    reaction_id: NotRequired[int]  # Reaction id set on message
    reactions: NotRequired[List['messages_reaction_counter_response_item']]  # Actual reactions counters on this message
    last_reaction_id: NotRequired[int]  # Last reaction id set on this message
    is_pinned: NotRequired[Flag]  # Is message pinned in its conversation
    text: str  # Message text
    update_time: NotRequired[int]  # Date when the message has been updated in Unixtime
    was_listened: NotRequired[Flag]  # Was the audio message inside already listened by you
    pinned_at: NotRequired[int]  # Date when the message has been pinned in Unixtime
    is_silent: NotRequired[Flag]  # Is silent message, push without sound
    is_unavailable: NotRequired[Flag]  # Is message unavailable for some reason, including its id equals 0
    version: int

class messages_message_action(TypedDict):
    conversation_message_id: NotRequired[int]  # Message ID
    email: NotRequired[str]  # Email address for chat_invite_user or chat_kick_user actions
    member_id: NotRequired[int]  # User or email peer ID
    message: NotRequired[str]  # Message body of related message
    photo: NotRequired['messages_message_action_photo']
    text: NotRequired[str]  # New chat title for chat_create and chat_title_update actions
    type: 'messages_message_action_status'

class messages_message_action_photo(TypedDict):
    photo_50: str  # URL of the preview image with 50px in width
    photo_100: str  # URL of the preview image with 100px in width
    photo_200: str  # URL of the preview image with 200px in width

class messages_message_attachment(TypedDict):
    audio: NotRequired['audio_audio']
    audio_message: NotRequired['messages_audio_message']
    call: NotRequired['calls_call']
    doc: NotRequired['docs_doc']
    gift: NotRequired['gifts_layout']
    graffiti: NotRequired['messages_graffiti']
    market: NotRequired['market_market_item']
    market_market_album: NotRequired['market_market_album']
    photo: NotRequired['photos_photo']
    sticker: NotRequired['base_sticker']
    story: NotRequired['stories_story']
    type: 'messages_message_attachment_type'
    wall_reply: NotRequired['wall_wall_comment']
    poll: NotRequired['polls_poll']

class messages_message_request_data(TypedDict):
    status: NotRequired[str]  # Status of message request
    inviter_id: NotRequired[int]  # Message request sender id
    request_date: NotRequired[int]  # Message request date

class messages_messages_array(TypedDict):
    count: NotRequired[int]
    items: NotRequired[List['messages_message']]

class messages_out_read_by(TypedDict):
    count: NotRequired[int]
    member_ids: NotRequired[List[int]]

class messages_pinned_message(TypedDict):
    attachments: NotRequired[List['messages_message_attachment']]
    conversation_message_id: int  # Unique auto-incremented number for all messages with this peer
    id: int  # Message ID
    date: int  # Date when the message has been sent in Unixtime
    from_id: int  # Message author's ID
    fwd_messages: NotRequired[List['messages_foreign_message']]  # Forwarded messages
    geo: NotRequired['base_geo']
    peer_id: int  # Peer ID
    reply_message: NotRequired['messages_foreign_message']
    text: str  # Message text
    keyboard: NotRequired['messages_keyboard']
    out: NotRequired[Flag]  # Information whether the message is outcoming
    important: NotRequired[Flag]  # Is it an important message

class messages_push_settings(TypedDict):
    disabled_forever: Flag  # Information whether push notifications are disabled forever
    disabled_until: NotRequired[int]  # Time until what notifications are disabled
    no_sound: Flag  # Information whether the sound is on
    disabled_mentions: NotRequired[Flag]  # Information whether the mentions are disabled
    disabled_mass_mentions: NotRequired[Flag]  # Information whether the mass mentions (like '@all', '@online') are disabled

class messages_reaction_asset_item(TypedDict):
    reaction_id: int
    links: 'messages_reaction_asset_item_links'  # Liks to reactions assets for each asset type

class messages_reaction_asset_item_links(TypedDict):
    big_animation: str  # Big reaction animation json file
    small_animation: str  # Small reaction animation json file
    static: str  # Reaction image file

class messages_reaction_counter_response_item(TypedDict):
    reaction_id: int
    count: int
    user_ids: List[int]

class messages_reaction_counters_response_item(TypedDict):
    cmid: int
    counters: List['messages_reaction_counter_response_item']

class messages_reaction_response_item(TypedDict):
    user_id: int
    reaction_id: int

class messages_send_user_ids_response_item(TypedDict):
    peer_id: int
    message_id: int
    conversation_message_id: int
    error: NotRequired['base_message_error']

class newsfeed_comments_item_base(TypedDict):
    type: 'newsfeed_newsfeed_item_type'
    source_id: NotRequired[int]
    date: NotRequired[int]
    post_id: NotRequired[int]

class newsfeed_item_audio_audio(TypedDict):
    count: NotRequired[int]  # Audios number
    items: NotRequired[List['audio_audio']]

class newsfeed_item_base(TypedDict):
    type: 'newsfeed_newsfeed_item_type'
    source_id: int  # Item source ID
    date: int  # Date when item has been added in Unixtime
    short_text_rate: NotRequired[float]  # Preview length control parameter
    feedback: NotRequired['newsfeed_item_wallpost_feedback']

class newsfeed_item_digest_button(TypedDict):
    title: str
    style: NotRequired[Literal['primary']]

class newsfeed_item_digest_footer(TypedDict):
    style: Literal['text', 'button']
    text: str  # text for invite to enable smart feed
    button: NotRequired['newsfeed_item_digest_button']
    feed_id: NotRequired[str]

class newsfeed_item_digest_header(TypedDict):
    title: str  # Title of the header
    subtitle: NotRequired[str]  # Subtitle of the header, when title have two strings
    badge_text: NotRequired[str]  # Optional field for red badge in Trends feed blocks
    style: Literal['singleline', 'multiline']
    button: NotRequired['newsfeed_item_digest_button']

class newsfeed_item_friend_friends(TypedDict):
    count: NotRequired[int]  # Number of friends has been added
    items: NotRequired[List['base_user_id']]

class newsfeed_item_holiday_recommendations_block_header(TypedDict):
    title: NotRequired[str]  # Title of the header
    subtitle: NotRequired[str]  # Subtitle of the header
    image: NotRequired[List['base_image']]
    action: NotRequired['base_link_button_action']

class newsfeed_item_photo_photos(TypedDict):
    count: NotRequired[int]  # Photos number
    items: NotRequired[List['photos_photo']]

class newsfeed_item_photo_tag_photo_tags(TypedDict):
    count: NotRequired[int]  # Tags number
    items: NotRequired[List['photos_photo']]

class newsfeed_item_promo_button_action(TypedDict):
    url: NotRequired[str]
    type: NotRequired[str]
    target: NotRequired[str]

class newsfeed_item_promo_button_image(TypedDict):
    width: NotRequired[int]
    height: NotRequired[int]
    url: NotRequired[str]

class newsfeed_item_video_video(TypedDict):
    count: NotRequired[int]  # Tags number
    items: NotRequired[List['video_video_full']]

class newsfeed_item_wallpost_feedback(TypedDict):
    type: 'newsfeed_item_wallpost_feedback_type'
    question: str
    answers: NotRequired[List['newsfeed_item_wallpost_feedback_answer']]
    stars_count: NotRequired[int]
    descriptions: NotRequired[List[str]]
    gratitude: NotRequired[str]
    track_code: NotRequired[str]

class newsfeed_item_wallpost_feedback_answer(TypedDict):
    title: str
    id: str

class newsfeed_list(TypedDict):
    id: int  # List ID
    title: str  # List title

class notes_note(TypedDict):
    read_comments: NotRequired[int]
    can_comment: NotRequired['base_bool_int']  # Information whether current user can comment the note
    comments: int  # Comments number
    date: int  # Date when the note has been created in Unixtime
    id: int  # Note ID
    owner_id: int  # Note owner's ID
    text: NotRequired[str]  # Note text
    text_wiki: NotRequired[str]  # Note text in wiki format
    title: str  # Note title
    view_url: str  # URL of the page with note preview
    privacy_view: NotRequired[List[str]]
    privacy_comment: NotRequired[List[str]]

class notes_note_comment(TypedDict):
    date: int  # Date when the comment has beed added in Unixtime
    id: int  # Comment ID
    message: str  # Comment text
    nid: int  # Note ID
    oid: int  # Note ID
    reply_to: NotRequired[int]  # ID of replied comment
    uid: int  # Comment author's ID

class notifications_feedback(TypedDict):
    attachments: NotRequired[List['wall_wallpost_attachment']]
    from_id: NotRequired[int]  # Reply author's ID
    geo: NotRequired['base_geo']
    id: NotRequired[int]  # Item ID
    likes: NotRequired['base_likes_info']
    text: NotRequired[str]  # Reply text
    to_id: NotRequired[int]  # Wall owner's ID

class notifications_notification(TypedDict):
    inner_type: Literal['notifications_notification']
    date: NotRequired[int]  # Date when the event has been occurred
    feedback: NotRequired['notifications_feedback']
    parent: NotRequired['notifications_notification']
    reply: NotRequired['notifications_reply']
    type: NotRequired[str]  # Notification type

class notifications_reply(TypedDict):
    date: NotRequired[int]  # Date when the reply has been created in Unixtime
    id: NotRequired[int]  # Reply ID
    text: NotRequired[int]  # Reply text

class notifications_send_message_error(TypedDict):
    code: NotRequired[Literal[1, 2, 3, 4]]  # Error code
    description: NotRequired[str]  # Error description

class notifications_send_message_item(TypedDict):
    user_id: NotRequired[int]  # User ID
    status: NotRequired[Flag]  # Notification status
    error: NotRequired['notifications_send_message_error']

class oauth_error(TypedDict):
    error: str  # Error type
    error_description: str  # Error description
    redirect_uri: NotRequired[str]  # URI for validation

class orders_amount(TypedDict):
    amounts: NotRequired[List['orders_amount_item']]
    currency: NotRequired[str]  # Currency name

class orders_amount_item(TypedDict):
    amount: NotRequired[float]  # Votes amount in user's currency
    description: NotRequired[str]  # Amount description
    votes: NotRequired[str]  # Votes number

class orders_order(TypedDict):
    amount: str  # Amount
    app_order_id: str  # App order ID
    cancel_transaction_id: NotRequired[str]  # Cancel transaction ID
    date: str  # Date of creation in Unixtime
    id: str  # Order ID
    item: str  # Order item
    receiver_id: str  # Receiver ID
    status: Literal['created', 'charged', 'refunded', 'chargeable', 'cancelled', 'declined']  # Order status
    transaction_id: NotRequired[str]  # Transaction ID
    user_id: str  # User ID

class orders_subscription(TypedDict):
    cancel_reason: NotRequired[str]  # Cancel reason
    create_time: int  # Date of creation in Unixtime
    id: int  # Subscription ID
    item_id: str  # Subscription order item
    next_bill_time: NotRequired[int]  # Date of next bill in Unixtime
    expire_time: NotRequired[int]  # Subscription expiration time in Unixtime
    pending_cancel: NotRequired[Flag]  # Pending cancel state
    period: int  # Subscription period
    period_start_time: int  # Date of last period start in Unixtime
    price: int  # Subscription price
    title: NotRequired[str]  # Subscription name
    app_id: NotRequired[int]  # Subscription's application id
    application_name: NotRequired[str]  # Subscription's application name
    photo_url: NotRequired[str]  # Item photo image url
    status: str  # Subscription status
    test_mode: NotRequired[Flag]  # Is test subscription
    trial_expire_time: NotRequired[int]  # Date of trial expire in Unixtime
    update_time: int  # Date of last change in Unixtime
    is_game: NotRequired[Flag]  # Is game (not miniapp) subscription

class owner_state(TypedDict):
    state: NotRequired[Literal[1, 2, 3, 4, 5]]
    description: NotRequired[str]  # wiki text to describe user state

class pages_wikipage(TypedDict):
    creator_id: NotRequired[int]  # Page creator ID
    creator_name: NotRequired[str]  # Page creator name
    editor_id: NotRequired[int]  # Last editor ID
    editor_name: NotRequired[str]  # Last editor name
    group_id: int  # Community ID
    id: int  # Page ID
    title: str  # Page title
    views: int  # Views number
    who_can_edit: 'pages_privacy_settings'  # Edit settings of the page
    who_can_view: 'pages_privacy_settings'  # View settings of the page

class pages_wikipage_full(TypedDict):
    created: int  # Date when the page has been created in Unixtime
    creator_id: NotRequired[int]  # Page creator ID
    current_user_can_edit: NotRequired['base_bool_int']  # Information whether current user can edit the page
    current_user_can_edit_access: NotRequired['base_bool_int']  # Information whether current user can edit the page access settings
    edited: int  # Date when the page has been edited in Unixtime
    editor_id: NotRequired[int]  # Last editor ID
    group_id: int  # Community ID
    html: NotRequired[str]  # Page content, HTML
    id: int  # Page ID
    source: NotRequired[str]  # Page content, wiki
    title: str  # Page title
    view_url: str  # URL of the page preview
    views: int  # Views number
    who_can_edit: 'pages_privacy_settings'  # Edit settings of the page
    who_can_view: 'pages_privacy_settings'  # View settings of the page
    url: NotRequired[str]  # URL
    parent: NotRequired[str]  # Parent
    parent2: NotRequired[str]  # Parent2
    owner_id: NotRequired[int]  # Owner ID

class pages_wikipage_history(TypedDict):
    id: int  # Version ID
    length: int  # Page size in bytes
    date: int  # Date when the page has been edited in Unixtime
    editor_id: int  # Last editor ID
    editor_name: str  # Last editor name

class photos_image(TypedDict):
    height: NotRequired[int]  # Height of the photo in px.
    type: NotRequired['photos_image_type']
    url: NotRequired[str]  # Photo URL.
    width: NotRequired[int]  # Width of the photo in px.

class photos_photo(TypedDict):
    access_key: NotRequired[str]  # Access key for the photo
    album_id: int  # Album ID
    date: int  # Date when uploaded
    height: NotRequired[int]  # Original photo height
    id: int  # Photo ID
    images: NotRequired[List['photos_image']]
    lat: NotRequired[float]  # Latitude
    long: NotRequired[float]  # Longitude
    owner_id: int  # Photo owner's ID
    photo_256: NotRequired[str]  # URL of image with 2560 px width
    thumb_hash: NotRequired[str]  # Thumb Hash
    can_comment: NotRequired['base_bool_int']  # Information whether current user can comment the photo
    place: NotRequired[str]
    post_id: NotRequired[int]  # Post ID
    sizes: NotRequired[List['photos_photo_sizes']]
    square_crop: NotRequired[str]
    text: NotRequired[str]  # Photo caption
    user_id: NotRequired[int]  # ID of the user who have uploaded the photo
    width: NotRequired[int]  # Original photo width
    has_tags: Flag  # Whether photo has attached tag links
    likes: NotRequired['base_likes']
    comments: NotRequired['base_object_count']
    reposts: NotRequired['base_reposts_info']
    tags: NotRequired['base_object_count']
    hidden: NotRequired['base_property_exists']  # Returns if the photo is hidden above the wall
    real_offset: NotRequired[int]  # Real position of the photo
    vertical_align: NotRequired[Literal['top', 'middle', 'bottom']]  # Sets vertical alignment of a photo

class photos_photo_album(TypedDict):
    created: int  # Date when the album has been created in Unixtime
    description: NotRequired[str]  # Photo album description
    id: int  # Photo album ID
    owner_id: int  # Album owner's ID
    size: int  # Photos number
    thumb: NotRequired['photos_photo']
    title: str  # Photo album title
    updated: int  # Date when the album has been updated last time in Unixtime

class photos_photo_album_full(TypedDict):
    can_upload: NotRequired['base_bool_int']  # Information whether current user can upload photo to the album
    comments_disabled: NotRequired['base_bool_int']  # Information whether album comments are disabled
    created: NotRequired[int]  # Date when the album has been created in Unixtime, not set for system albums
    description: NotRequired[str]  # Photo album description
    can_delete: NotRequired[Flag]  # album can delete
    id: int  # Photo album ID
    can_include_to_feed: NotRequired[Flag]  # album can be selected to feed
    is_locked: NotRequired[Flag]  # Need show privacy lock at album
    owner_id: int  # Album owner's ID
    size: int  # Photos number
    sizes: NotRequired[List['photos_photo_sizes']]
    thumb_id: NotRequired[int]  # Thumb photo ID
    thumb_is_last: NotRequired['base_bool_int']  # Information whether the album thumb is last photo
    thumb_src: NotRequired[str]  # URL of the thumb image
    title: str  # Photo album title
    updated: NotRequired[int]  # Date when the album has been updated last time in Unixtime, not set for system albums
    upload_by_admins_only: NotRequired['base_bool_int']  # Information whether only community administrators can upload photos

class photos_photo_sizes(TypedDict):
    height: int  # Height in px
    url: NotRequired[str]  # URL of the image
    src: NotRequired[str]  # URL of the image
    type: 'photos_photo_sizes_type'
    width: int  # Width in px

class photos_photo_tag(TypedDict):
    date: int  # Date when tag has been added in Unixtime
    id: int  # Tag ID
    placer_id: int  # ID of the tag creator
    tagged_name: str  # Tag description
    description: NotRequired[str]  # Tagged description.
    user_id: int  # Tagged user ID
    viewed: 'base_bool_int'  # Information whether the tag is reviewed
    x: float  # Coordinate X of the left upper corner
    x2: float  # Coordinate X of the right lower corner
    y: float  # Coordinate Y of the left upper corner
    y2: float  # Coordinate Y of the right lower corner

class photos_photo_upload(TypedDict):
    album_id: int  # Album ID
    upload_url: str  # URL to upload photo
    fallback_upload_url: NotRequired[str]  # Fallback URL if upload_url returned error
    user_id: int  # User ID
    group_id: NotRequired[int]  # Group ID

class photos_photo_xtr_tag_info(TypedDict):
    access_key: NotRequired[str]  # Access key for the photo
    album_id: int  # Album ID
    date: int  # Date when uploaded
    height: NotRequired[int]  # Original photo height
    id: int  # Photo ID
    lat: NotRequired[float]  # Latitude
    long: NotRequired[float]  # Longitude
    owner_id: int  # Photo owner's ID
    photo_1280: NotRequired[str]  # URL of image with 1280 px width
    photo_130: NotRequired[str]  # URL of image with 130 px width
    photo_2560: NotRequired[str]  # URL of image with 2560 px width
    photo_604: NotRequired[str]  # URL of image with 604 px width
    photo_75: NotRequired[str]  # URL of image with 75 px width
    photo_807: NotRequired[str]  # URL of image with 807 px width
    placer_id: NotRequired[int]  # ID of the tag creator
    post_id: NotRequired[int]  # Post ID
    sizes: NotRequired[List['photos_photo_sizes']]
    tag_created: NotRequired[int]  # Date when tag has been added in Unixtime
    tag_id: NotRequired[int]  # Tag ID
    text: NotRequired[str]  # Photo caption
    user_id: NotRequired[int]  # ID of the user who have uploaded the photo
    width: NotRequired[int]  # Original photo width
    has_tags: NotRequired[Flag]  # Whether photo has attached tag links

class photos_tags_suggestion_item(TypedDict):
    title: NotRequired[str]
    caption: NotRequired[str]
    type: NotRequired[str]
    buttons: NotRequired[List['photos_tags_suggestion_item_button']]
    photo: NotRequired['photos_photo']
    tags: NotRequired[List['photos_photo_tag']]
    track_code: NotRequired[str]

class photos_tags_suggestion_item_button(TypedDict):
    title: NotRequired[str]
    action: NotRequired[Literal['confirm', 'decline', 'show_tags']]
    style: NotRequired[Literal['primary', 'secondary']]

class podcast_cover(TypedDict):
    sizes: NotRequired[List['photos_photo_sizes']]

class podcast_external_data(TypedDict):
    url: NotRequired[str]  # Url of the podcast page
    owner_url: NotRequired[str]  # Url of the podcasts owner community
    title: NotRequired[str]  # Podcast title
    owner_name: NotRequired[str]  # Name of the podcasts owner community
    cover: NotRequired['podcast_cover']  # Podcast cover

class polls_answer(TypedDict):
    id: int  # Answer ID
    rate: float  # Answer rate in percents
    text: str  # Answer text
    votes: int  # Votes number

class polls_background(TypedDict):
    angle: NotRequired[int]  # Gradient angle with 0 on positive X axis
    color: NotRequired[str]  # Hex color code without #
    height: NotRequired[int]  # Original height of pattern tile
    id: NotRequired[int]
    name: NotRequired[str]
    images: NotRequired[List['base_image']]  # Pattern tiles
    points: NotRequired[List['base_gradient_point']]  # Gradient points
    type: NotRequired[Literal['gradient', 'tile']]
    width: NotRequired[int]  # Original with of pattern tile

class polls_fields_voters(TypedDict):
    answer_id: NotRequired[int]  # Answer ID
    users: NotRequired['polls_voters_fields_users']
    answer_offset: NotRequired[str]  # Answer offset

class polls_friend(TypedDict):
    id: int

class polls_poll(TypedDict):
    anonymous: NotRequired['polls_poll_anonymous']
    friends: NotRequired[List['polls_friend']]
    multiple: Flag  # Information whether the poll with multiple choices
    answer_id: NotRequired[int]  # Current user's answer ID
    end_date: int
    answer_ids: NotRequired[List[int]]  # Current user's answer IDs
    closed: Flag
    is_board: Flag
    can_edit: Flag
    can_vote: Flag
    can_report: Flag
    can_share: Flag
    embed_hash: NotRequired[str]
    photo: NotRequired['polls_background']
    answers: List['polls_answer']
    created: int  # Date when poll has been created in Unixtime
    id: int  # Poll ID
    owner_id: int  # Poll owner's ID
    author_id: NotRequired[int]  # Poll author's ID
    question: str  # Poll question
    background: NotRequired['polls_background']
    votes: int  # Votes number
    disable_unvote: Flag

class polls_voters(TypedDict):
    answer_id: NotRequired[int]  # Answer ID
    users: NotRequired['polls_voters_users']
    answer_offset: NotRequired[str]  # Answer offset

class polls_voters_fields_users(TypedDict):
    count: NotRequired[int]  # Votes number
    items: NotRequired[List['users_user_full']]

class polls_voters_users(TypedDict):
    count: NotRequired[int]  # Votes number
    items: NotRequired[List[int]]

class prettyCards_prettyCard(TypedDict):
    inner_type: Literal['prettyCards_prettyCard']
    button: NotRequired['prettyCards_button_one_of']  # Button key
    button_text: NotRequired[str]  # Button text in current language
    card_id: str  # Card ID (long int returned as string)
    images: NotRequired[List['base_image']]
    link_url: str  # Link URL
    photo: str  # Photo ID (format "<owner_id>_<media_id>")
    price: NotRequired[str]  # Price if set (decimal number returned as string)
    price_old: NotRequired[str]  # Old price if set (decimal number returned as string)
    title: str  # Title

class search_hint(TypedDict):
    app: NotRequired['apps_app']
    description: str  # Object description
    # global: NotRequired['base_bool_int']  # Information whether the object has been found globally
    group: NotRequired['groups_group']
    profile: NotRequired['users_user_min']
    section: NotRequired['search_hint_section']
    type: 'search_hint_type'
    link: NotRequired['base_link']

class secure_giveEventSticker_item(TypedDict):
    user_id: NotRequired[int]
    status: NotRequired[str]

class secure_level(TypedDict):
    level: NotRequired[int]  # Level
    uid: NotRequired[int]  # User ID

class secure_setCounter_item(TypedDict):
    id: int  # User ID
    result: 'base_bool_int'

class secure_sms_notification(TypedDict):
    app_id: NotRequired[str]  # Application ID
    date: NotRequired[str]  # Date when message has been sent in Unixtime
    id: NotRequired[str]  # Notification ID
    message: NotRequired[str]  # Messsage text
    user_id: NotRequired[str]  # User ID

class secure_token_checked(TypedDict):
    date: NotRequired[int]  # Date when access_token has been generated in Unixtime
    expire: NotRequired[int]  # Date when access_token will expire in Unixtime
    success: NotRequired[int]  # Returns if successfully processed
    user_id: NotRequired[int]  # User ID

class secure_transaction(TypedDict):
    date: NotRequired[int]  # Transaction date in Unixtime
    id: NotRequired[int]  # Transaction ID
    uid_from: NotRequired[int]  # From ID
    uid_to: NotRequired[int]  # To ID
    votes: NotRequired[int]  # Votes number

class stats_activity(TypedDict):
    '''Activity stats'''
    comments: NotRequired[int]  # Comments number
    copies: NotRequired[int]  # Reposts number
    hidden: NotRequired[int]  # Hidden from news count
    likes: NotRequired[int]  # Likes number
    subscribed: NotRequired[int]  # New subscribers count
    unsubscribed: NotRequired[int]  # Unsubscribed count

class stats_city(TypedDict):
    count: NotRequired[int]  # Visitors number
    name: NotRequired[str]  # City name
    value: NotRequired[int]  # City ID

class stats_country(TypedDict):
    code: NotRequired[str]  # Country code
    count: NotRequired[int]  # Visitors number
    name: NotRequired[str]  # Country name
    value: NotRequired[int]  # Country ID

class stats_period(TypedDict):
    activity: NotRequired['stats_activity']
    period_from: NotRequired['stats_period_from_one_of']
    period_to: NotRequired['stats_period_to_one_of']
    reach: NotRequired['stats_reach']
    visitors: NotRequired['stats_views']

class stats_reach(TypedDict):
    '''Reach stats'''
    age: NotRequired[List['stats_sex_age']]
    cities: NotRequired[List['stats_city']]
    countries: NotRequired[List['stats_country']]
    mobile_reach: NotRequired[int]  # Reach count from mobile devices
    reach: NotRequired[int]  # Reach count
    reach_subscribers: NotRequired[int]  # Subscribers reach count
    sex: NotRequired[List['stats_sex_age']]
    sex_age: NotRequired[List['stats_sex_age']]

class stats_sex_age(TypedDict):
    count: NotRequired[int]  # Visitors number
    value: str  # Sex/age value
    reach: NotRequired[int]
    reach_subscribers: NotRequired[int]
    count_subscribers: NotRequired[int]

class stats_views(TypedDict):
    '''Views stats'''
    age: NotRequired[List['stats_sex_age']]
    cities: NotRequired[List['stats_city']]
    countries: NotRequired[List['stats_country']]
    mobile_views: NotRequired[int]  # Number of views from mobile devices
    sex: NotRequired[List['stats_sex_age']]
    sex_age: NotRequired[List['stats_sex_age']]
    views: NotRequired[int]  # Views number
    visitors: NotRequired[int]  # Visitors number

class stats_wallpost_stat(TypedDict):
    post_id: NotRequired[int]
    hide: NotRequired[int]  # Hidings number
    join_group: NotRequired[int]  # People have joined the group
    links: NotRequired[int]  # Link clickthrough
    reach_subscribers: NotRequired[int]  # Subscribers reach
    reach_subscribers_count: NotRequired[int]
    reach_total: NotRequired[int]  # Total reach
    reach_total_count: NotRequired[int]
    reach_viral: NotRequired[int]
    reach_ads: NotRequired[int]
    report: NotRequired[int]  # Reports number
    to_group: NotRequired[int]  # Clickthrough to community
    unsubscribe: NotRequired[int]  # Unsubscribed members
    sex_age: NotRequired[List['stats_sex_age']]

class status_status(TypedDict):
    text: str  # Status text
    audio: NotRequired['audio_audio']

class stickers_image_set(TypedDict):
    base_url: str  # Base URL for images in set
    version: NotRequired[int]  # Version number to be appended to the image URL
    images: NotRequired[List['base_image']]

class storage_value(TypedDict):
    key: str
    value: str

class store_product(TypedDict):
    id: int  # Id of the product
    type: Literal['stickers']  # Product type
    is_new: NotRequired[Flag]  # Information whether sticker product wasn't used after being purchased
    copyright: NotRequired[str]  # Product copyright information
    base_id: NotRequired[int]  # Id of the base pack (for sticker pack styles)
    style_ids: NotRequired[List[int]]  # Array of style ids available for the sticker pack
    purchased: NotRequired['base_bool_int']  # Information whether the product is purchased (1 - yes, 0 - no)
    active: NotRequired['base_bool_int']  # Information whether the product is active (1 - yes, 0 - no)
    promoted: NotRequired['base_bool_int']  # Information whether the product is promoted (1 - yes, 0 - no)
    purchase_date: NotRequired[int]  # Date (Unix time) when the product was purchased
    title: NotRequired[str]  # Title of the product
    stickers: NotRequired[List['base_sticker_new']]
    style_sticker_ids: NotRequired[List[int]]  # Array of style sticker ids (for sticker pack styles)
    icon: NotRequired['store_product_icon']  # Array of icon images or icon set object of the product (for stickers product type)
    previews: NotRequired[List['base_image']]  # Array of preview images of the product (for stickers product type)
    has_animation: NotRequired[Flag]  # Information whether the product is an animated sticker pack (for stickers product type)
    subtitle: NotRequired[str]  # Subtitle of the product
    payment_region: NotRequired[str]
    is_vmoji: NotRequired[Flag]  # Information whether sticker pack is a vmoji pack
    title_lang_key: NotRequired[str]
    description_lang_key: NotRequired[str]
    url: NotRequired[str]
    is_popup: NotRequired[Flag]  # Information whether the product is a sticker pack with popup stickers (for stickers product type)

class store_stickers_keyword(TypedDict):
    words: List[str]
    user_stickers: NotRequired[List['base_sticker_new']]
    promoted_stickers: NotRequired[List['base_sticker_new']]
    stickers: NotRequired[List['store_stickers_keyword_sticker']]

class store_stickers_keyword_sticker(TypedDict):
    pack_id: int  # Pack id
    sticker_id: int  # Sticker id

class stories_clickable_area(TypedDict):
    x: int
    y: int

class stories_clickable_sticker(TypedDict):
    clickable_area: List['stories_clickable_area']
    id: int  # Clickable sticker ID
    hashtag: NotRequired[str]
    link_object: NotRequired['base_link']
    mention: NotRequired[str]
    tooltip_text: NotRequired[str]
    owner_id: NotRequired[int]
    story_id: NotRequired[int]
    clip_id: NotRequired[int]
    question: NotRequired[str]
    question_button: NotRequired[str]
    place_id: NotRequired[int]
    market_item: NotRequired['market_market_item']
    audio: NotRequired['audio_audio']
    audio_start_time: NotRequired[int]
    style: NotRequired[Literal['transparent', 'blue_gradient', 'red_gradient', 'underline', 'blue', 'green', 'white', 'question_reply', 'light', 'impressive', 'dark', 'accent_background', 'accent_text', 'dark_unique', 'light_unique', 'light_text', 'dark_text', 'black', 'dark_without_bg', 'light_without_bg', 'rectangle', 'circle', 'poop', 'heart', 'star']]
    type: Literal['hashtag', 'mention', 'link', 'question', 'place', 'market_item', 'music', 'story_reply', 'owner', 'post', 'poll', 'sticker', 'app', 'situational_theme', 'playlist', 'clip', 'situational_template']
    subtype: NotRequired[Literal['market_item', 'aliexpress_product']]
    post_owner_id: NotRequired[int]
    post_id: NotRequired[int]
    poll: NotRequired['polls_poll']
    color: NotRequired[str]  # Color, hex format
    sticker_id: NotRequired[int]  # Sticker ID
    sticker_pack_id: NotRequired[int]  # Sticker pack ID
    app: NotRequired['apps_app_min']
    app_context: NotRequired[str]  # Additional context for app sticker
    has_new_interactions: NotRequired[Flag]  # Whether current user has unread interaction with this app
    is_broadcast_notify_allowed: NotRequired[Flag]  # Whether current user allowed broadcast notify from this app
    situational_theme_id: NotRequired[int]
    situational_app_url: NotRequired[str]

class stories_clickable_stickers(TypedDict):
    clickable_stickers: List['stories_clickable_sticker']
    original_height: int
    original_width: int

class stories_feed_item(TypedDict):
    type: Literal['promo_stories', 'stories', 'live_active', 'live_finished', 'app_grouped_stories', 'discover']  # Type of Feed Item
    id: NotRequired[str]
    owner_id: NotRequired[int]
    stories: NotRequired[List['stories_story']]  # Author stories
    grouped: NotRequired[List['stories_feed_item']]  # Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)
    app: NotRequired['apps_app_min']  # App, which stories has been grouped (for type app_grouped_stories)
    promo_data: NotRequired['stories_promo_block']  # Additional data for promo stories (for type promo_stories)
    track_code: NotRequired[str]
    has_unseen: NotRequired[Flag]
    name: NotRequired[str]

class stories_promo_block(TypedDict):
    '''Additional data for promo stories'''
    name: str  # Promo story title
    photo_50: str  # RL of square photo of the story with 50 pixels in width
    photo_100: str  # RL of square photo of the story with 100 pixels in width
    not_animated: Flag  # Hide animation for promo story
    is_advice: Flag  # Promo story from advice

class stories_replies(TypedDict):
    count: int  # Replies number.
    new: NotRequired[int]  # New replies number.

class stories_stat_category(TypedDict):
    header: str
    lines: List['stories_stat_line']

class stories_stat_line(TypedDict):
    name: str
    counter: NotRequired[int]
    is_unavailable: NotRequired[Flag]

class stories_story(TypedDict):
    access_key: NotRequired[str]  # Access key for private object.
    can_comment: NotRequired['base_bool_int']  # Information whether current user can comment the story (0 - no, 1 - yes).
    can_reply: NotRequired['base_bool_int']  # Information whether current user can reply to the story (0 - no, 1 - yes).
    can_see: NotRequired['base_bool_int']  # Information whether current user can see the story (0 - no, 1 - yes).
    can_like: NotRequired[Flag]  # Information whether current user can like the story.
    can_share: NotRequired['base_bool_int']  # Information whether current user can share the story (0 - no, 1 - yes).
    can_hide: NotRequired['base_bool_int']  # Information whether current user can hide the story (0 - no, 1 - yes).
    date: NotRequired[int]  # Date when story has been added in Unixtime.
    expires_at: NotRequired[int]  # Story expiration time. Unixtime.
    id: int  # Story ID.
    is_deleted: NotRequired[Flag]  # Information whether the story is deleted (false - no, true - yes).
    is_expired: NotRequired[Flag]  # Information whether the story is expired (false - no, true - yes).
    link: NotRequired['stories_story_link']
    owner_id: int  # Story owner's ID.
    parent_story: NotRequired['stories_story']
    parent_story_access_key: NotRequired[str]  # Access key for private object.
    parent_story_id: NotRequired[int]  # Parent story ID.
    parent_story_owner_id: NotRequired[int]  # Parent story owner's ID.
    photo: NotRequired['photos_photo']
    replies: NotRequired['stories_replies']  # Replies counters to current story.
    seen: NotRequired['base_bool_int']  # Information whether current user has seen the story or not (0 - no, 1 - yes).
    type: NotRequired['stories_story_type']
    clickable_stickers: NotRequired['stories_clickable_stickers']
    video: NotRequired['video_video_full']
    views: NotRequired[int]  # Views number.
    can_ask: NotRequired['base_bool_int']  # Information whether story has question sticker and current user can send question to the author
    can_ask_anonymous: NotRequired['base_bool_int']  # Information whether story has question sticker and current user can send anonymous question to the author
    narratives_count: NotRequired[int]
    first_narrative_title: NotRequired[str]
    can_use_in_narrative: NotRequired[Flag]

class stories_story_link(TypedDict):
    text: str  # Link text
    url: str  # Link URL
    link_url_target: NotRequired[str]  # How to open url

class stories_story_stats(TypedDict):
    answer: 'stories_story_stats_stat'
    bans: 'stories_story_stats_stat'
    open_link: 'stories_story_stats_stat'
    replies: 'stories_story_stats_stat'
    shares: 'stories_story_stats_stat'
    subscribers: 'stories_story_stats_stat'
    views: 'stories_story_stats_stat'
    likes: 'stories_story_stats_stat'

class stories_story_stats_stat(TypedDict):
    count: NotRequired[int]  # Stat value
    state: 'stories_story_stats_state'

class stories_upload_result(TypedDict):
    upload_result: NotRequired[str]

class stories_viewers_item(TypedDict):
    is_liked: Flag  # user has like for this object
    user_id: int  # user id
    user: NotRequired['users_user_full']

class streaming_stats(TypedDict):
    event_type: Literal['post', 'comment', 'share']  # Events type
    stats: List['streaming_stats_point']  # Statistics

class streaming_stats_point(TypedDict):
    timestamp: int
    value: int

class support_unblock_screen_buttonFields(TypedDict):
    id: NotRequired[float]
    type: Literal['button']
    text: NotRequired[str]  # Надпись на кнопке

class support_unblock_screen_buttonSubmitFields(TypedDict):
    type: Literal['button_submit']
    id: NotRequired[float]
    disabled: NotRequired[Flag]
    text: NotRequired[str]  # Надпись на кнопке
    target_screen: NotRequired[str]  # Индекс экрана для перехода

class support_unblock_screen_buttonSupportFields(TypedDict):
    type: Literal['support_button']
    id: NotRequired[float]
    text: NotRequired[str]

class support_unblock_screen_buttonUnblockFields(TypedDict):
    type: Literal['unblock_button']
    id: NotRequired[float]
    text: NotRequired[str]  # Надпись на кнопке

class support_unblock_screen_contentBlockFields(TypedDict):
    type: Literal['ban_reason_content']
    content_type: NotRequired[Literal['post', 'message']]  # Тип контента

class support_unblock_screen_eventsListFields(TypedDict):
    type: Literal['events_list']
    header: NotRequired[str]  # Заголовок над пунктами
    items: NotRequired[List['support_unblock_screen_eventsListFields_item']]

class support_unblock_screen_eventsListFields_item(TypedDict):
    date: NotRequired[str]  # Дата блокировки
    reason: NotRequired[str]  # Причина блокировки

class support_unblock_screen_headerFields(TypedDict):
    type: Literal['header']
    text: NotRequired[str]  # Текст заголовка
    subheader: NotRequired[str]  # Текст подзаголовка
    image: NotRequired[str]  # Картинка над текстом
    gradient: NotRequired[Flag]  # Нужен ли градиент  на фоне заголовка
    exit_btn: NotRequired[Flag]  # Нужна ли кнопка выхода

class support_unblock_screen_modalButtonFields(TypedDict):
    id: NotRequired[float]
    type: Literal['modal_button']
    label: NotRequired[str]  # Надпись на кнопке
    modal: NotRequired['support_unblock_screen_modalButton_modalContent']

class support_unblock_screen_modalButton_modalContent(TypedDict):
    title: NotRequired[str]
    text: NotRequired[str]

class support_unblock_screen_slidersFields(TypedDict):
    type: Literal['sliders']
    items: NotRequired[List['support_unblock_screen_slidersFields_item']]

class support_unblock_screen_slidersFields_item(TypedDict):
    title: NotRequired[str]
    short_desc: NotRequired[str]  # Краткое описание, выпадающее при нажатии
    target_screen: NotRequired[str]  # Экран, на который происходит переход; обычно содержимое другого экрана - просто заголовок с текстом и кнопкой

class support_unblock_screen_stepperFields(TypedDict):
    type: Literal['stepper']
    target: NotRequired[str]  # Экран, на который происходит переход после ответа на все вопросы
    questions: NotRequired[List['support_unblock_screen_stepperQuestions']]

class support_unblock_screen_stepperQuestions(TypedDict):
    title: str  # Текст вопроса
    yes_desc: NotRequired[str]  # Текст, отображаемый при нажатии на да
    no_desc: NotRequired[str]  # Текст, отображаемый при нажатии на нет
    target_screen: str  # Экран, на который происходит переход; обычно содержимое другого экрана - просто заголовок с текстом и кнопкой
    step: NotRequired[float]

class support_unblock_screen_textBackgroundFields(TypedDict):
    type: Literal['text_background']
    text: NotRequired[str]  # Текст
    bg_image: NotRequired[str]  # Полный URL фонового изображения

class support_unblock_screen_textBorderedFields(TypedDict):
    type: Literal['text_bordered']
    text: NotRequired[str]  # Текст
    notify_btn: NotRequired[Flag]  # Нужна ли кнопка 'Получить уведомление'

class support_unblock_screen_tutorialAnswers(TypedDict):
    id: NotRequired[str]
    title: NotRequired[str]  # Текст ответа
    is_right: NotRequired[Flag]  # Является ли вариант ответа правильным
    explanation: NotRequired[str]  # Текст, который отображается при выборе этого варианта

class support_unblock_screen_tutorialFields(TypedDict):
    type: Literal['tutorial']
    target: NotRequired[str]  # Экран, на который происходит переход после ответа на все вопросы
    questions: NotRequired[List['support_unblock_screen_tutorialQuestions']]

class support_unblock_screen_tutorialQuestions(TypedDict):
    id: NotRequired[str]
    title: NotRequired[str]  # Текст вопроса
    answers: NotRequired[List['support_unblock_screen_tutorialAnswers']]

class users_career(TypedDict):
    city_id: NotRequired[int]  # City ID
    city_name: NotRequired[str]  # City name
    company: NotRequired[str]  # Company name
    # from: NotRequired[int]  # From year
    group_id: NotRequired[int]  # Community ID
    id: NotRequired[int]  # Career ID
    position: NotRequired[str]  # Position
    until: NotRequired[int]  # Till year

class users_exports(TypedDict):
    facebook: NotRequired[int]
    livejournal: NotRequired[int]
    twitter: NotRequired[int]

class users_last_seen(TypedDict):
    platform: NotRequired[int]  # Type of the platform that used for the last authorization
    time: NotRequired[int]  # Last visit date (in Unix time)

class users_military(TypedDict):
    # from: NotRequired[int]  # From year
    id: NotRequired[int]  # Military ID
    unit: str  # Unit name
    unit_id: int  # Unit ID
    until: NotRequired[int]  # Till year

class users_occupation(TypedDict):
    id: NotRequired[int]  # ID of school, university, company group
    name: NotRequired[str]  # Name of occupation
    type: NotRequired[Literal['school', 'university', 'work']]  # Type of occupation
    graduate_year: NotRequired[int]
    city_id: NotRequired[int]

class users_online_info(TypedDict):
    visible: Flag  # Whether you can see real online status of user or not
    last_seen: NotRequired[int]  # Last time we saw user being active
    is_online: NotRequired[Flag]  # Whether user is currently online or not
    app_id: NotRequired[int]  # Application id from which user is currently online or was last seen online
    is_mobile: NotRequired[Flag]  # Is user online from desktop app or mobile app
    status: NotRequired[Literal['recently', 'last_week', 'last_month', 'long_ago', 'not_show']]  # In case user online is not visible, it indicates approximate timeframe of user online

class users_personal(TypedDict):
    alcohol: NotRequired[int]  # User's views on alcohol
    inspired_by: NotRequired[str]  # User's inspired by
    langs: NotRequired[List[str]]
    langs_full: NotRequired[List['database_language_full']]  # User's languages with full info
    life_main: NotRequired[int]  # User's personal priority in life
    people_main: NotRequired[int]  # User's personal priority in people
    political: NotRequired[int]  # User's political views
    religion: NotRequired[str]  # User's religion
    religion_id: NotRequired[int]  # User's religion id
    smoking: NotRequired[int]  # User's views on smoking

class users_relative(TypedDict):
    birth_date: NotRequired[str]  # Date of child birthday (format dd.mm.yyyy)
    id: NotRequired[int]  # Relative ID
    name: NotRequired[str]  # Name of relative
    type: Literal['parent', 'child', 'grandparent', 'grandchild', 'sibling']  # Relative type

class users_school(TypedDict):
    city: NotRequired[int]  # City ID
    # class: NotRequired[str]  # School class letter
    class_id: NotRequired[int]  # School class id
    id: NotRequired[str]  # School ID
    name: NotRequired[str]  # School name
    type: NotRequired[int]  # School type ID
    type_str: NotRequired[str]  # School type name
    year_from: NotRequired[int]  # Year the user started to study
    year_graduated: NotRequired[int]  # Graduation year
    year_to: NotRequired[int]  # Year the user finished to study
    speciality: NotRequired[str]

class users_university(TypedDict):
    chair: NotRequired[int]  # Chair ID
    chair_name: NotRequired[str]  # Chair name
    city: NotRequired[int]  # City ID
    education_form: NotRequired[str]  # Education form
    education_form_id: NotRequired[int]  # Education form id
    education_status: NotRequired[str]  # Education status
    education_status_id: NotRequired[int]  # Education status id
    faculty: NotRequired[int]  # Faculty ID
    faculty_name: NotRequired[str]  # Faculty name
    graduation: NotRequired[int]  # Graduation year
    id: NotRequired[int]  # University ID
    name: NotRequired[str]  # University name
    university_group_id: NotRequired[int]

class users_user_connections(TypedDict):
    skype: str  # User's Skype nickname
    facebook: str  # User's Facebook account
    facebook_name: NotRequired[str]  # User's Facebook name
    twitter: str  # User's Twitter account
    livejournal: NotRequired[str]  # User's Livejournal account
    instagram: str  # User's Instagram account

class users_user_counters(TypedDict):
    albums: NotRequired[int]  # Albums number
    badges: NotRequired[int]  # Badges number
    audios: NotRequired[int]  # Audios number
    followers: NotRequired[int]  # Followers number
    friends: NotRequired[int]  # Friends number
    gifts: NotRequired[int]  # Gifts number
    groups: NotRequired[int]  # Communities number
    notes: NotRequired[int]  # Notes number
    online_friends: NotRequired[int]  # Online friends number
    pages: NotRequired[int]  # Public pages number
    photos: NotRequired[int]  # Photos number
    subscriptions: NotRequired[int]  # Subscriptions number
    user_photos: NotRequired[int]  # Number of photos with user
    user_videos: NotRequired[int]  # Number of videos with user
    videos: NotRequired[int]  # Videos number
    video_playlists: NotRequired[int]  # Playlists number
    new_photo_tags: NotRequired[int]
    new_recognition_tags: NotRequired[int]
    mutual_friends: NotRequired[int]
    friends_followers: NotRequired[int]
    posts: NotRequired[int]
    articles: NotRequired[int]
    wishes: NotRequired[int]
    podcasts: NotRequired[int]
    clips: NotRequired[int]
    clips_followers: NotRequired[int]
    videos_followers: NotRequired[int]  # Videos followers number
    clips_views: NotRequired[int]
    clips_likes: NotRequired[int]

class users_user_min(TypedDict):
    deactivated: NotRequired[str]  # Returns if a profile is deleted or blocked
    first_name: NotRequired[str]  # User first name
    hidden: NotRequired[int]  # Returns if a profile is hidden.
    id: int  # User ID
    last_name: NotRequired[str]  # User last name
    can_access_closed: NotRequired[Flag]
    is_closed: NotRequired[Flag]

class users_user_settings_xtr(TypedDict):
    connections: NotRequired['users_user_connections']
    bdate: NotRequired[str]  # User's date of birth
    bdate_visibility: NotRequired[int]  # Information whether user's birthdate are hidden
    city: NotRequired['base_city']
    first_name: NotRequired[str]  # User first name
    home_town: str  # User's hometown
    last_name: NotRequired[str]  # User last name
    maiden_name: NotRequired[str]  # User maiden name
    name_request: NotRequired['account_name_request']
    personal: NotRequired['users_personal']
    phone: NotRequired[str]  # User phone number with some hidden digits
    relation: NotRequired['users_user_relation']  # User relationship status
    relation_partner: NotRequired['users_user_min']
    relation_pending: NotRequired['base_bool_int']  # Information whether relation status is pending
    relation_requests: NotRequired[List['users_user_min']]
    screen_name: NotRequired[str]  # Domain name of the user's page
    sex: NotRequired['base_sex']  # User sex
    status: str  # User status
    status_audio: NotRequired['audio_audio']
    interests: NotRequired['account_user_settings_interests']
    languages: NotRequired[List[str]]

class users_users_array(TypedDict):
    count: int  # Users number
    items: List[int]

class utils_domain_resolved(TypedDict):
    object_id: NotRequired[int]  # Object ID
    group_id: NotRequired[int]  # Group ID
    type: NotRequired['utils_domain_resolved_type']

class utils_last_shortened_link(TypedDict):
    access_key: NotRequired[str]  # Access key for private stats
    key: NotRequired[str]  # Link key (characters after vk.cc/)
    short_url: NotRequired[str]  # Short link URL
    timestamp: NotRequired[int]  # Creation time in Unixtime
    url: NotRequired[str]  # Full URL
    views: NotRequired[int]  # Total views number

class utils_link_checked(TypedDict):
    link: NotRequired[str]  # Link URL
    status: NotRequired['utils_link_checked_status']

class utils_link_stats(TypedDict):
    key: NotRequired[str]  # Link key (characters after vk.cc/)
    stats: NotRequired[List['utils_stats']]

class utils_link_stats_extended(TypedDict):
    key: NotRequired[str]  # Link key (characters after vk.cc/)
    stats: NotRequired[List['utils_stats_extended']]

class utils_short_link(TypedDict):
    access_key: NotRequired[str]  # Access key for private stats
    key: NotRequired[str]  # Link key (characters after vk.cc/)
    short_url: NotRequired[str]  # Short link URL
    url: NotRequired[str]  # Full URL

class utils_stats(TypedDict):
    timestamp: NotRequired[int]  # Start time
    views: NotRequired[int]  # Total views number

class utils_stats_city(TypedDict):
    city_id: NotRequired[int]  # City ID
    views: NotRequired[int]  # Views number

class utils_stats_country(TypedDict):
    country_id: NotRequired[int]  # Country ID
    views: NotRequired[int]  # Views number

class utils_stats_extended(TypedDict):
    cities: NotRequired[List['utils_stats_city']]
    countries: NotRequired[List['utils_stats_country']]
    sex_age: NotRequired[List['utils_stats_sex_age']]
    timestamp: NotRequired[int]  # Start time
    views: NotRequired[int]  # Total views number

class utils_stats_sex_age(TypedDict):
    age_range: NotRequired[str]  # Age denotation
    female: NotRequired[int]  #  Views by female users
    male: NotRequired[int]  #  Views by male users

class video_episode(TypedDict):
    time: NotRequired[int]  # Seconds from start of the video
    text: NotRequired[str]  # Description of episode

class video_live_category(TypedDict):
    id: int
    label: str
    sublist: NotRequired[List['video_live_category']]

class video_live_info(TypedDict):
    enabled: 'base_bool_int'
    is_notifications_blocked: NotRequired['base_bool_int']

class video_live_settings(TypedDict):
    '''Video live settings'''
    can_rewind: NotRequired['base_bool_int']  # If user car rewind live or not
    is_endless: NotRequired['base_bool_int']  # If live is endless or not
    max_duration: NotRequired[int]  # Max possible time for rewind
    is_clips_live: NotRequired['base_bool_int']  # If live in clips apps

class video_save_result(TypedDict):
    access_key: NotRequired[str]  # Video access key
    description: NotRequired[str]  # Video description
    owner_id: NotRequired[int]  # Video owner ID
    title: NotRequired[str]  # Video title
    upload_url: NotRequired[str]  # URL for the video uploading
    video_id: NotRequired[int]  # Video ID

class video_stream_input_params(TypedDict):
    url: NotRequired[str]
    key: NotRequired[str]
    okmp_url: NotRequired[str]
    webrtc_url: NotRequired[str]

class video_video(TypedDict):
    response_type: NotRequired[Literal['min', 'full']]
    access_key: NotRequired[str]  # Video access key
    adding_date: NotRequired[int]  # Date when the video has been added in Unixtime
    can_comment: NotRequired['base_bool_int']  # Information whether current user can comment the video
    can_edit: NotRequired['base_bool_int']  # Information whether current user can edit the video
    can_delete: NotRequired['base_bool_int']  # Information whether current user can delete the video
    can_like: NotRequired['base_bool_int']  # Information whether current user can like the video
    can_repost: NotRequired[int]  # Information whether current user can repost the video
    can_subscribe: NotRequired['base_bool_int']  # Information whether current user can subscribe to author of the video
    can_add_to_faves: NotRequired['base_bool_int']  # Information whether current user can add the video to favourites
    can_add: NotRequired['base_bool_int']  # Information whether current user can add the video
    can_attach_link: NotRequired['base_bool_int']  # Information whether current user can attach action button to the video
    can_edit_privacy: NotRequired['base_bool_int']  # Information whether current user can edit the video privacy
    is_private: NotRequired['base_bool_int']  # 1 if video is private
    comments: NotRequired[int]  # Number of comments
    date: NotRequired[int]  # Date when video has been uploaded in Unixtime
    description: NotRequired[str]  # Video description
    duration: NotRequired[int]  # Video duration in seconds
    image: NotRequired[List['video_video_image']]
    first_frame: NotRequired[List['video_video_image']]
    width: NotRequired[int]  # Video width
    height: NotRequired[int]  # Video height
    id: NotRequired[int]  # Video ID
    owner_id: NotRequired[int]  # Video owner ID
    user_id: NotRequired[int]  # Id of the user who uploaded the video if it was uploaded to a group by member
    title: NotRequired[str]  # Video title
    is_favorite: NotRequired[Flag]  # Whether video is added to bookmarks
    player: NotRequired[str]  # Video embed URL
    processing: NotRequired['base_property_exists']  # Returns if the video is processing
    converting: NotRequired['base_bool_int']  # 1 if  video is being converted
    added: NotRequired['base_bool_int']  # 1 if video is added to user's albums
    is_subscribed: NotRequired['base_bool_int']  # 1 if user is subscribed to author of the video
    track_code: NotRequired[str]
    repeat: NotRequired['base_property_exists']  # Information whether the video is repeated
    type: NotRequired[Literal['video', 'music_video', 'movie', 'live', 'short_video']]
    views: NotRequired[int]  # Number of views
    local_views: NotRequired[int]  # If video is external, number of views on vk
    content_restricted: NotRequired[int]  # Restriction code
    content_restricted_message: NotRequired[str]  # Restriction text
    balance: NotRequired[int]  # Live donations balance
    live: NotRequired['base_property_exists']  # 1 if the video is a live stream
    upcoming: NotRequired['base_property_exists']  # 1 if the video is an upcoming stream
    live_start_time: NotRequired[int]  # Date in Unixtime when the live stream is scheduled to start by the author
    live_notify: NotRequired['base_bool_int']  # Whether current user is subscribed to the upcoming live stream notification (if not subscribed to the author)
    spectators: NotRequired[int]  # Number of spectators of the stream
    platform: NotRequired[str]  # External platform
    likes: NotRequired['base_likes']
    reposts: NotRequired['base_reposts_info']

class video_video_album(TypedDict):
    id: int  # Album ID
    owner_id: int  # Album owner's ID
    title: str  # Album title
    track_code: NotRequired[str]  # Album trackcode
    response_type: NotRequired[Literal['min', 'full']]

class video_video_files(TypedDict):
    external: NotRequired[str]  # URL of the external player
    mp4_144: NotRequired[str]  # URL of the mpeg4 file with 144p quality
    mp4_240: NotRequired[str]  # URL of the mpeg4 file with 240p quality
    mp4_360: NotRequired[str]  # URL of the mpeg4 file with 360p quality
    mp4_480: NotRequired[str]  # URL of the mpeg4 file with 480p quality
    mp4_720: NotRequired[str]  # URL of the mpeg4 file with 720p quality
    mp4_1080: NotRequired[str]  # URL of the mpeg4 file with 1080p quality
    mp4_1440: NotRequired[str]  # URL of the mpeg4 file with 2K quality
    mp4_2160: NotRequired[str]  # URL of the mpeg4 file with 4K quality
    flv_320: NotRequired[str]  # URL of the flv file with 320p quality

class wall_app_post(TypedDict):
    id: NotRequired[int]  # Application ID
    name: NotRequired[str]  # Application name
    photo_130: NotRequired[str]  # URL of the preview image with 130 px in width
    photo_604: NotRequired[str]  # URL of the preview image with 604 px in width

class wall_attached_note(TypedDict):
    comments: int  # Comments number
    date: int  # Date when the note has been created in Unixtime
    id: int  # Note ID
    owner_id: int  # Note owner's ID
    read_comments: int  # Read comments number
    title: str  # Note title
    text: NotRequired[str]  # Note text
    privacy_view: NotRequired[List[str]]
    privacy_comment: NotRequired[List[str]]
    can_comment: NotRequired[int]
    text_wiki: NotRequired[str]  # Note wiki text
    view_url: str  # URL of the page with note preview

class wall_carousel_base(TypedDict):
    carousel_offset: NotRequired[int]  # Index of current carousel element

class wall_comment_attachment(TypedDict):
    audio: NotRequired['audio_audio']
    doc: NotRequired['docs_doc']
    link: NotRequired['base_link']
    market: NotRequired['market_market_item']
    market_market_album: NotRequired['market_market_album']
    note: NotRequired['wall_attached_note']
    page: NotRequired['pages_wikipage_full']
    photo: NotRequired['photos_photo']
    sticker: NotRequired['base_sticker']
    type: 'wall_comment_attachment_type'
    video: NotRequired['video_video']
    graffiti: NotRequired['wall_graffiti']

class wall_geo(TypedDict):
    coordinates: NotRequired[str]  # Coordinates as string. <latitude> <longtitude>
    showmap: NotRequired[int]  # Information whether a map is showed
    type: NotRequired[Literal['place', 'point']]  # Place type

class wall_graffiti(TypedDict):
    id: NotRequired[int]  # Graffiti ID
    owner_id: NotRequired[int]  # Graffiti owner's ID
    photo_200: NotRequired[str]  # URL of the preview image with 200 px in width
    photo_586: NotRequired[str]  # URL of the preview image with 586 px in width
    height: NotRequired[int]  # Graffiti height
    url: NotRequired[str]  # Graffiti URL
    width: NotRequired[int]  # Graffiti width
    access_key: NotRequired[str]  # Access key for graffiti

class wall_post_copyright(TypedDict):
    id: NotRequired[int]
    link: str
    name: str
    type: str

class wall_post_source(TypedDict):
    data: NotRequired[str]  # Additional data
    platform: NotRequired[str]  # Platform name
    type: NotRequired['wall_post_source_type']
    url: NotRequired[str]  # URL to an external site used to publish the post
    link: NotRequired['base_link']

class wall_posted_photo(TypedDict):
    id: NotRequired[int]  # Photo ID
    owner_id: NotRequired[int]  # Photo owner's ID
    photo_130: NotRequired[str]  # URL of the preview image with 130 px in width
    photo_604: NotRequired[str]  # URL of the preview image with 604 px in width

class wall_views(TypedDict):
    count: NotRequired[int]  # Count

class wall_wall_comment(TypedDict):
    id: int  # Comment ID
    from_id: int  # Author ID
    can_edit: NotRequired['base_bool_int']
    post_id: NotRequired[int]
    owner_id: NotRequired[int]
    parents_stack: NotRequired[List[int]]
    photo_id: NotRequired[int]
    video_id: NotRequired[int]
    date: int  # Date when the comment has been added in Unixtime
    text: str  # Comment text
    attachments: NotRequired[List['wall_wallpost_attachment']]
    donut: NotRequired['wall_wall_comment_donut']
    likes: NotRequired['base_likes_info']
    real_offset: NotRequired[int]  # Real position of the comment
    reply_to_user: NotRequired[int]  # Replied user ID
    reply_to_comment: NotRequired[int]  # Replied comment ID
    thread: NotRequired['comment_thread']
    is_from_post_author: NotRequired[Flag]  # Whether post is by author of the post or not
    deleted: NotRequired[Flag]
    pid: NotRequired[int]  # Photo ID

class wall_wall_comment_donut(TypedDict):
    is_don: NotRequired[Flag]  # Means commentator is donator
    placeholder: NotRequired['wall_wall_comment_donut_placeholder']

class wall_wall_comment_donut_placeholder(TypedDict):
    text: str

class wall_wallpost(TypedDict):
    inner_type: Literal['wall_wallpost']
    access_key: NotRequired[str]  # Access key to private object
    is_deleted: NotRequired[Flag]
    deleted_reason: NotRequired[str]
    deleted_details: NotRequired[str]
    donut_miniapp_url: NotRequired[str]
    attachments: NotRequired[List['wall_wallpost_attachment']]
    copyright: NotRequired['wall_post_copyright']  # Information about the source of the post
    date: NotRequired[int]  # Date of publishing in Unixtime
    edited: NotRequired[int]  # Date of editing in Unixtime
    from_id: NotRequired[int]  # Post author ID
    geo: NotRequired['wall_geo']
    id: NotRequired[int]  # Post ID
    is_archived: NotRequired[Flag]  # Is post archived, only for post owners
    is_favorite: NotRequired[Flag]  # Information whether the post in favorites list
    likes: NotRequired['base_likes_info']  # Count of likes
    owner_id: NotRequired[int]  # Wall owner's ID
    post_id: NotRequired[int]  # If post type 'reply', contains original post ID
    parents_stack: NotRequired[List[int]]  # If post type 'reply', contains original parent IDs stack
    post_source: NotRequired['wall_post_source']
    post_type: NotRequired['wall_post_type']
    reposts: NotRequired['base_reposts_info']
    signer_id: NotRequired[int]  # Post signer ID
    text: NotRequired[str]  # Post text
    views: NotRequired['wall_views']  # Count of views

class wall_wallpost_attachment(TypedDict):
    access_key: NotRequired[str]  # Access key for the audio
    album: NotRequired['photos_photo_album']
    app: NotRequired['wall_app_post']
    audio: NotRequired['audio_audio']
    doc: NotRequired['docs_doc']
    event: NotRequired['events_event_attach']
    group: NotRequired['groups_group_attach']
    graffiti: NotRequired['wall_graffiti']
    link: NotRequired['base_link']
    market: NotRequired['market_market_item']
    market_album: NotRequired['market_market_album']
    note: NotRequired['notes_note']
    page: NotRequired['pages_wikipage_full']
    photo: NotRequired['photos_photo']
    poll: NotRequired['polls_poll']
    posted_photo: NotRequired['wall_posted_photo']
    type: 'wall_wallpost_attachment_type'
    video: NotRequired['video_video_full']
    clip: NotRequired['video_video_full']
    video_playlist: NotRequired['video_video_album_full']

class wall_wallpost_comments_donut(TypedDict):
    placeholder: NotRequired['wall_wallpost_comments_donut_placeholder']

class wall_wallpost_comments_donut_placeholder(TypedDict):
    '''Info about paid comments feature'''
    text: str

class wall_wallpost_donut(TypedDict):
    '''Info about paid wall post'''
    is_donut: Flag  # Post only for dons
    paid_duration: NotRequired[int]  # Value of this field need to pass in wall.post/edit in donut_paid_duration
    placeholder: NotRequired['wall_wallpost_donut_placeholder']  # If placeholder was respond, text and all attachments will be hidden
    can_publish_free_copy: NotRequired[Flag]  # Says whether group admin can post free copy of this donut post
    edit_mode: NotRequired[Literal['all', 'duration']]  # Says what user can edit in post about donut properties

class wall_wallpost_donut_placeholder(TypedDict):
    text: str

class widgets_comment_media(TypedDict):
    item_id: NotRequired[int]  # Media item ID
    owner_id: NotRequired[int]  # Media owner's ID
    thumb_src: NotRequired[str]  # URL of the preview image (type=photo only)
    type: NotRequired['widgets_comment_media_type']

class widgets_comment_replies(TypedDict):
    can_post: NotRequired['base_bool_int']  # Information whether current user can comment the post
    count: NotRequired[int]  # Comments number
    replies: NotRequired[List['widgets_comment_replies_item']]
    groups_can_post: NotRequired['base_bool_int']  # Information whether groups can comment the post
    can_view: NotRequired['base_bool_int']  # Information whether current user can view the comments

class widgets_comment_replies_item(TypedDict):
    cid: NotRequired[int]  # Comment ID
    date: NotRequired[int]  # Date when the comment has been added in Unixtime
    likes: NotRequired['widgets_widget_likes']
    text: NotRequired[str]  # Comment text
    uid: NotRequired[int]  # User ID
    user: NotRequired['users_user_full']

class widgets_widget_comment(TypedDict):
    attachments: NotRequired[List['wall_comment_attachment']]
    owner_id: NotRequired[int]  # Wall owner's ID
    can_delete: NotRequired['base_bool_int']  # Information whether current user can delete the comment
    comments: NotRequired['widgets_comment_replies']
    date: int  # Date when the comment has been added in Unixtime
    from_id: int  # Comment author ID
    id: int  # Comment ID
    likes: NotRequired['base_likes_info']
    media: NotRequired['widgets_comment_media']
    post_source: NotRequired['wall_post_source']
    post_type: str  # Post type
    reposts: NotRequired['base_reposts_info']
    text: str  # Comment text
    to_id: int  # Wall owner
    user: NotRequired['users_user_full']
    is_favorite: NotRequired['base_bool_int']  # Information whether the post in favorites list
    short_text_rate: NotRequired[float]  # Preview length control parameter

class widgets_widget_likes(TypedDict):
    count: NotRequired[int]  # Likes number

class widgets_widget_page(TypedDict):
    comments: NotRequired['base_object_count']
    date: NotRequired[int]  # Date when widgets on the page has been initialized firstly in Unixtime
    description: NotRequired[str]  # Page description
    id: NotRequired[int]  # Page ID
    likes: NotRequired['base_object_count']
    page_id: NotRequired[str]  # page_id parameter value
    photo: NotRequired[str]  # URL of the preview image
    title: NotRequired[str]  # Page title
    url: NotRequired[str]  # Page absolute URL

class ads_stats_age(ads_demographic_stats_period_item_base):
    value: NotRequired[str]  # Age interval

class ads_stats_cities(ads_demographic_stats_period_item_base):
    name: NotRequired[str]  # City name
    value: NotRequired[Union[int, str]]  # City ID

class ads_stats_sex(ads_demographic_stats_period_item_base):
    value: NotRequired['ads_stats_sex_value']

class ads_stats_sex_age(ads_demographic_stats_period_item_base):
    value: NotRequired[str]  # Sex and age interval

class ads_targ_settings(ads_criteria):
    id: NotRequired[str]  # Ad ID
    campaign_id: NotRequired[str]  # Campaign ID

class apps_app(apps_app_min):
    author_url: NotRequired[str]  # Application author's URL
    banner_1120: NotRequired[str]  # URL of the app banner with 1120 px in width
    banner_560: NotRequired[str]  # URL of the app banner with 560 px in width
    icon_16: NotRequired[str]  # URL of the app icon with 16 px in width
    is_new: NotRequired['base_bool_int']  # Is new flag
    push_enabled: NotRequired['base_bool_int']  # Is push enabled
    friends: NotRequired[List[int]]
    catalog_position: NotRequired[int]  # Catalog position
    description: NotRequired[str]  # Application description
    genre: NotRequired[str]  # Genre name
    genre_id: NotRequired[int]  # Genre ID
    international: NotRequired[Flag]  # Information whether the application is multilanguage
    is_in_catalog: NotRequired[int]  # Information whether application is in mobile catalog
    leaderboard_type: NotRequired['apps_app_leaderboard_type']
    members_count: NotRequired[int]  # Members number
    platform_id: NotRequired[str]  # Application ID in store
    published_date: NotRequired[int]  # Date when the application has been published in Unixtime
    screen_name: NotRequired[str]  # Screen name
    section: NotRequired[str]  # Application section name

class base_link(base_link_no_product):
    text: NotRequired[str]
    product: NotRequired['base_link_product']

class callback_confirmation(callback_base):
    type: NotRequired['callback_type']

class callback_message_allow(callback_base):
    type: NotRequired['callback_type']
    object: 'callback_message_allow_object'

class callback_message_edit(callback_base):
    type: NotRequired['callback_type']
    object: 'messages_message'

class callback_message_new(callback_base):
    type: NotRequired['callback_type']
    object: 'callback_message_object'

class callback_message_reply(callback_base):
    type: NotRequired['callback_type']
    object: 'messages_message'

class callback_photo_comment(wall_wall_comment):
    photo_owner_id: int

class callback_video_comment(wall_wall_comment):
    video_owner_id: NotRequired[int]

class database_city(base_object):
    area: NotRequired[str]  # Area title
    region: NotRequired[str]  # Region title
    important: NotRequired['base_bool_int']  # Information whether the city is included in important cities list

class friends_friend_extended_status(friends_friend_status):
    is_request_unread: NotRequired[Flag]  # Is friend request from other user unread

class market_market_item_basic_with_group(market_market_item_basic):
    is_group_verified: NotRequired[Flag]
    group_name: NotRequired[str]
    group_link: NotRequired[str]
    is_owner: NotRequired[Flag]
    is_adult: NotRequired[Flag]

class market_market_item_full(market_market_item):
    albums_ids: NotRequired[List[int]]
    photos: NotRequired[List['photos_photo']]
    can_comment: NotRequired['base_bool_int']  # Information whether current use can comment the item
    can_repost: NotRequired['base_bool_int']  # Information whether current use can repost the item
    likes: NotRequired['base_likes']
    reposts: NotRequired['base_reposts_info']
    views_count: NotRequired[int]  # Views number
    wishlist_item_id: NotRequired[int]  # Object identifier in wishlist of viewer
    rating: NotRequired[float]  # Rating of product
    orders_count: NotRequired[int]  # Count of product orders
    cancel_info: NotRequired['base_link']  # Information for cancel and revert order
    user_agreement_info: NotRequired[str]  # User agreement info
    ad_id: NotRequired[int]  # Contains ad ID if it has
    owner_info: NotRequired['market_item_owner_info']  # Information about the group where the item is placed
    can_edit: NotRequired[Flag]  # Can the item be updated by current user?
    can_delete: NotRequired[Flag]  # Can item be deleted by current user?
    can_recover: NotRequired[Flag]  # Can item be restored by current user?
    can_show_convert_to_service: NotRequired[Flag]  # Can the item be converted from a product into a service?
    promotion: NotRequired['market_item_promotion_info']  # Information about promotion of the item
    vk_pay_discount: NotRequired[int]  # The amount of the discount if VK Pay is used for payment

class messages_getConversationById_extended(messages_getConversationById):
    profiles: NotRequired[List['users_user_full']]
    groups: NotRequired[List['groups_group_full']]

class newsfeed_comments_base(base_comments_info):
    list: NotRequired[List['wall_wall_comment']]

class newsfeed_comments_item_type_notes(newsfeed_comments_item_base):
    text: NotRequired[str]
    comments: NotRequired['newsfeed_comments_base']
    likes: NotRequired['base_likes']

class newsfeed_comments_item_type_topic(newsfeed_comments_item_base):
    text: NotRequired[str]
    comments: NotRequired['newsfeed_comments_base']
    likes: NotRequired['base_likes']

class newsfeed_item_audio(newsfeed_item_base):
    audio: NotRequired['newsfeed_item_audio_audio']
    post_id: NotRequired[int]  # Post ID

class newsfeed_item_digest(newsfeed_item_base):
    feed_id: NotRequired[str]  # id of feed in digest
    items: NotRequired[List['newsfeed_item_digest_item']]
    main_post_ids: NotRequired[List[str]]
    template: NotRequired[Literal['list', 'grid', 'single']]  # type of digest
    header: NotRequired['newsfeed_item_digest_header']
    footer: NotRequired['newsfeed_item_digest_footer']

class newsfeed_item_digest_full_item(newsfeed_item_base):
    inner_type: Literal['newsfeed_item_digest_full_item']
    text: NotRequired[str]
    source_name: NotRequired[str]
    attachment_index: NotRequired[int]
    attachment: NotRequired['wall_wallpost_attachment']
    style: NotRequired[Literal['default', 'inversed', 'spotlight']]
    post: 'newsfeed_item_wallpost'
    badge_text: NotRequired[str]  # Optional red badge for posts in digest block

class newsfeed_item_friend(newsfeed_item_base):
    friends: NotRequired['newsfeed_item_friend_friends']

class newsfeed_item_promo_button(newsfeed_item_base):
    text: NotRequired[str]
    title: NotRequired[str]
    action: NotRequired['newsfeed_item_promo_button_action']
    images: NotRequired[List['newsfeed_item_promo_button_image']]

class newsfeed_item_topic(newsfeed_item_base):
    comments: NotRequired['base_comments_info']
    likes: NotRequired['base_likes_info']
    post_id: int  # Topic post ID
    text: str  # Post text

class newsfeed_list_full(newsfeed_list):
    no_reposts: NotRequired['base_bool_int']  # Information whether reposts hiding is enabled
    source_ids: NotRequired[List[int]]

class polls_poll_extended(polls_poll):
    profiles: NotRequired[List['users_user_full']]

class users_user(users_user_min):
    sex: NotRequired['base_sex']  # User sex
    screen_name: NotRequired[str]  # Domain name of the user's page
    photo_50: NotRequired[str]  # URL of square photo of the user with 50 pixels in width
    photo_100: NotRequired[str]  # URL of square photo of the user with 100 pixels in width
    online_info: NotRequired['users_online_info']
    online: NotRequired['base_bool_int']  # Information whether the user is online
    online_mobile: NotRequired['base_bool_int']  # Information whether the user is online in mobile site or application
    online_app: NotRequired[int]  # Application ID
    verified: NotRequired['base_bool_int']  # Information whether the user is verified
    trending: NotRequired['base_bool_int']  # Information whether the user has a "fire" pictogram.
    friend_status: NotRequired['friends_friend_status_status']
    mutual: NotRequired['friends_requests_mutual']

class users_user_full(users_user):
    first_name_nom: NotRequired[str]  # User's first name in nominative case
    first_name_gen: NotRequired[str]  # User's first name in genitive case
    first_name_dat: NotRequired[str]  # User's first name in dative case
    first_name_acc: NotRequired[str]  # User's first name in accusative case
    first_name_ins: NotRequired[str]  # User's first name in instrumental case
    first_name_abl: NotRequired[str]  # User's first name in prepositional case
    last_name_nom: NotRequired[str]  # User's last name in nominative case
    last_name_gen: NotRequired[str]  # User's last name in genitive case
    last_name_dat: NotRequired[str]  # User's last name in dative case
    last_name_acc: NotRequired[str]  # User's last name in accusative case
    last_name_ins: NotRequired[str]  # User's last name in instrumental case
    last_name_abl: NotRequired[str]  # User's last name in prepositional case
    nickname: NotRequired[str]  # User nickname
    maiden_name: NotRequired[str]  # User maiden name
    contact_name: NotRequired[str]  # User contact name
    domain: NotRequired[str]  # Domain name of the user's page
    bdate: NotRequired[str]  # User's date of birth
    city: NotRequired['base_city']
    timezone: NotRequired[float]  # User's timezone
    owner_state: NotRequired['owner_state']
    photo_200: NotRequired[str]  # URL of square photo of the user with 200 pixels in width
    photo_max: NotRequired[str]  # URL of square photo of the user with maximum width
    photo_200_orig: NotRequired[str]  # URL of user's photo with 200 pixels in width
    photo_400_orig: NotRequired[str]  # URL of user's photo with 400 pixels in width
    photo_max_orig: NotRequired[str]  # URL of user's photo of maximum size
    photo_id: NotRequired[str]  # ID of the user's main photo
    has_photo: NotRequired['base_bool_int']  # Information whether the user has main photo
    has_mobile: NotRequired['base_bool_int']  # Information whether the user specified his phone number
    is_friend: NotRequired['base_bool_int']  # Information whether the user is a friend of current user
    is_best_friend: NotRequired[Flag]  # Information whether the user is a best friend of current user
    wall_comments: NotRequired['base_bool_int']  # Information whether current user can comment wall posts
    can_post: NotRequired['base_bool_int']  # Information whether current user can post on the user's wall
    can_see_all_posts: NotRequired['base_bool_int']  # Information whether current user can see other users' audio on the wall
    can_see_audio: NotRequired['base_bool_int']  # Information whether current user can see the user's audio
    type: NotRequired['users_user_type']
    email: NotRequired[str]
    skype: NotRequired[str]
    facebook: NotRequired[str]
    facebook_name: NotRequired[str]
    twitter: NotRequired[str]
    livejournal: NotRequired[str]
    instagram: NotRequired[str]
    test: NotRequired['base_bool_int']
    video_live: NotRequired['video_live_info']
    is_video_live_notifications_blocked: NotRequired['base_bool_int']
    is_service: NotRequired[Flag]
    service_description: NotRequired[str]
    photo_rec: NotRequired[Union[str, Flag]]
    photo_medium: NotRequired[Union[str, Flag]]
    photo_medium_rec: NotRequired[Union[str, Flag]]
    photo: NotRequired[str]
    photo_big: NotRequired[str]
    photo_400: NotRequired[str]
    photo_max_size: NotRequired['photos_photo']
    language: NotRequired[str]
    stories_archive_count: NotRequired[int]
    has_unseen_stories: NotRequired[Flag]
    wall_default: NotRequired[Literal['owner', 'all']]
    can_call: NotRequired[Flag]  # Information whether current user can call
    can_call_from_group: NotRequired[Flag]  # Information whether group can call user
    can_invite_as_voicerooms_speaker: NotRequired[Flag]  # Information whether user/group can invite user as voicerooms speakr
    can_see_wishes: NotRequired[Flag]  # Information whether current user can see the user's wishes
    can_see_gifts: NotRequired['base_bool_int']  # Information whether current user can see the user's gifts
    interests: NotRequired[str]
    books: NotRequired[str]
    tv: NotRequired[str]
    quotes: NotRequired[str]
    about: NotRequired[str]
    games: NotRequired[str]
    movies: NotRequired[str]
    activities: NotRequired[str]
    music: NotRequired[str]
    can_write_private_message: NotRequired['base_bool_int']  # Information whether current user can write private message
    can_send_friend_request: NotRequired['base_bool_int']  # Information whether current user can send a friend request
    can_be_invited_group: NotRequired[Flag]  # Information whether current user can be invited to the community
    mobile_phone: NotRequired[str]  # User's mobile phone number
    home_phone: NotRequired[str]  # User's additional phone number
    site: NotRequired[str]  # User's website
    status_audio: NotRequired['audio_audio']
    status: NotRequired[str]  # User's status
    activity: NotRequired[str]  # User's status
    status_app: NotRequired['apps_app_min']
    last_seen: NotRequired['users_last_seen']
    exports: NotRequired['users_exports']
    crop_photo: NotRequired['base_crop_photo']
    followers_count: NotRequired[int]  # Number of user's followers and friends
    video_live_level: NotRequired[int]  # User level in live streams achievements
    video_live_count: NotRequired[int]  # Number of user's live streams
    clips_count: NotRequired[int]  # Number of user's clips
    blacklisted: NotRequired['base_bool_int']  # Information whether current user is in the requested user's blacklist.
    blacklisted_by_me: NotRequired['base_bool_int']  # Information whether the requested user is in current user's blacklist
    is_favorite: NotRequired['base_bool_int']  # Information whether the requested user is in faves of current user
    is_hidden_from_feed: NotRequired['base_bool_int']  # Information whether the requested user is hidden from current user's newsfeed
    common_count: NotRequired[int]  # Number of common friends with current user
    occupation: NotRequired['users_occupation']
    career: NotRequired[List['users_career']]
    military: NotRequired[List['users_military']]
    university: NotRequired[int]  # University ID
    university_name: NotRequired[str]  # University name
    university_group_id: NotRequired[int]
    faculty: NotRequired[int]  # Faculty ID
    faculty_name: NotRequired[str]  # Faculty name
    graduation: NotRequired[int]  # Graduation year
    education_form: NotRequired[str]  # Education form
    education_status: NotRequired[str]  # User's education status
    home_town: NotRequired[str]  # User hometown
    relation: NotRequired['users_user_relation']  # User relationship status
    relation_partner: NotRequired['users_user_min']
    personal: NotRequired['users_personal']
    universities: NotRequired[List['users_university']]
    schools: NotRequired[List['users_school']]
    relatives: NotRequired[List['users_relative']]
    is_subscribed_podcasts: NotRequired[Flag]  # Information whether current user is subscribed to podcasts
    can_subscribe_podcasts: NotRequired[Flag]  # Owner in whitelist or not
    can_subscribe_posts: NotRequired[Flag]  # Can subscribe to wall
    counters: NotRequired['users_user_counters']
    access_key: NotRequired[str]
    can_upload_doc: NotRequired['base_bool_int']
    can_ban: NotRequired[Flag]  # Information whether the user can be baned (added to black list) by me
    hash: NotRequired[str]
    is_no_index: NotRequired[Flag]  # Access to user profile is restricted for search engines
    contact_id: NotRequired[int]  # Contact person ID
    is_message_request: NotRequired[Flag]
    descriptions: NotRequired[List[str]]
    lists: NotRequired[List[int]]

class friends_requests_xtr_mutual(users_user_full):
    id: NotRequired[int]  # User ID
    user_id: int  # User ID
    # from: NotRequired[str]  # ID of the user by whom friend has been suggested
    mutual: NotRequired['friends_requests_mutual']
    track_code: NotRequired[str]
    message: NotRequired[str]  # Message sent with a request
    timestamp: NotRequired[int]  # Request timestamp
    descriptions: NotRequired[List[str]]

class groups_user_xtr_role(users_user_full):
    permissions: NotRequired[List['groups_member_role_permission']]
    role: NotRequired['groups_role_options']

class users_user_xtr_type(users_user_full):
    type: NotRequired['users_user_type']

class friends_requests_xtr_message(friends_requests_xtr_mutual):
    message: NotRequired[str]  # Message sent with a request

class messages_user_xtr_invited_by(users_user_xtr_type):
    invited_by: NotRequired[int]  # ID of the inviter
    name: NotRequired[str]  # Name of group
    type: NotRequired['messages_user_type_for_xtr_invited_by']

class video_video_album_full(video_video_album):
    count: int  # Total number of videos in album
    image: NotRequired[List['video_video_image']]  # Album cover image in different sizes
    image_blur: NotRequired['base_property_exists']  # Need blur album thumb or not
    is_system: NotRequired['base_property_exists']  # Information whether album is system
    updated_time: int  # Date when the album has been updated last time in Unixtime
    can_edit: NotRequired['base_bool_int']  # Is user can edit playlist
    can_delete: NotRequired['base_bool_int']  # Is user can delete playlist
    can_upload: NotRequired['base_bool_int']  # Is user can upload video to playlist

class video_video_full(video_video):
    files: NotRequired['video_video_files']
    trailer: NotRequired['video_video_files']
    episodes: NotRequired[List['video_episode']]  # List of video episodes with timecodes
    live_settings: NotRequired['video_live_settings']  # Settings for live stream

class video_video_image(base_image):
    with_padding: NotRequired['base_property_exists']
    size: NotRequired[str]

class account_user_settings(users_user_min, users_user_settings_xtr):
    photo_200: NotRequired[str]  # URL of square photo of the user with 200 pixels in width
    is_service_account: NotRequired[Flag]  # flag about service account

class groups_group_full(groups_group, groups_market_properties):
    member_status: NotRequired['groups_group_full_member_status']  # Current user's member status
    is_adult: NotRequired['base_bool_int']  # Information whether community is adult
    is_hidden_from_feed: NotRequired['base_bool_int']  # Information whether community is hidden from current user's newsfeed
    is_favorite: NotRequired['base_bool_int']  # Information whether community is in faves
    is_subscribed: NotRequired['base_bool_int']  # Information whether current user is subscribed
    city: NotRequired['base_object']
    description: NotRequired[str]  # Community description
    wiki_page: NotRequired[str]  # Community's main wiki page title
    members_count: NotRequired[int]  # Community members number
    members_count_text: NotRequired[str]  # Info about number of users in group
    requests_count: NotRequired[int]  # The number of incoming requests to the community
    video_live_level: NotRequired[int]  # Community level live streams achievements
    video_live_count: NotRequired[int]  # Number of community's live streams
    clips_count: NotRequired[int]  # Number of community's clips
    counters: NotRequired['groups_counters_group']
    textlives_count: NotRequired[int]  # Textlives number
    cover: NotRequired['base_owner_cover']
    video_cover: NotRequired['base_owner_cover']
    can_post: NotRequired['base_bool_int']  # Information whether current user can post on community's wall
    can_suggest: NotRequired['base_bool_int']
    can_upload_story: NotRequired['base_bool_int']  # Information whether current user can upload story
    can_call_to_community: NotRequired[Flag]  # Information whether current user can call to community
    can_upload_doc: NotRequired['base_bool_int']  # Information whether current user can upload doc
    can_upload_video: NotRequired['base_bool_int']  # Information whether current user can upload video
    can_upload_clip: NotRequired['base_bool_int']  # Information whether current user can upload clip
    can_see_all_posts: NotRequired['base_bool_int']  # Information whether current user can see all posts on community's wall
    can_create_topic: NotRequired['base_bool_int']  # Information whether current user can create topic
    activity: NotRequired[str]  # Type of group, start date of event or category of public page
    fixed_post: NotRequired[int]  # Fixed post ID
    has_photo: NotRequired['base_bool_int']  # Information whether community has photo
    crop_photo: NotRequired['base_crop_photo']  # Данные о точках, по которым вырезаны профильная и миниатюрная фотографии сообщества
    status: NotRequired[str]  # Community status
    status_audio: NotRequired['audio_audio']
    main_album_id: NotRequired[int]  # Community's main photo album ID
    links: NotRequired[List['groups_links_item']]
    contacts: NotRequired[List['groups_contacts_item']]
    wall: NotRequired[Literal[0, 1, 2, 3]]  # Information about wall status in community
    site: NotRequired[str]  # Community's website
    main_section: NotRequired['groups_group_full_section']
    secondary_section: NotRequired['groups_group_full_section']
    trending: NotRequired['base_bool_int']  # Information whether the community has a "fire" pictogram.
    can_message: NotRequired['base_bool_int']  # Information whether current user can send a message to community
    is_messages_blocked: NotRequired['base_bool_int']  # Information whether community can send a message to current user
    can_send_notify: NotRequired['base_bool_int']  # Information whether community can send notifications by phone number to current user
    online_status: NotRequired['groups_online_status']  # Status of replies in community messages
    invited_by: NotRequired[int]  # Inviter ID
    age_limits: NotRequired['groups_group_full_age_limits']  # Information whether age limit
    ban_info: NotRequired['groups_group_ban_info']  # User ban info
    has_group_channel: NotRequired[Flag]
    addresses: NotRequired['groups_addresses_info']  # Info about addresses in groups
    is_subscribed_podcasts: NotRequired[Flag]  # Information whether current user is subscribed to podcasts
    can_subscribe_podcasts: NotRequired[Flag]  # Owner in whitelist or not
    can_subscribe_posts: NotRequired[Flag]  # Can subscribe to wall
    live_covers: NotRequired['groups_live_covers']  # Live covers state
    stories_archive_count: NotRequired[int]
    has_unseen_stories: NotRequired[Flag]
    video_notifications_status: NotRequired[Literal['none', 'all', 'preferred']]  # Information about the status of video notifications for the current user.

class newsfeed_comments_item_type_market(market_market_item, newsfeed_comments_item_base):
    comments: NotRequired['newsfeed_comments_base']
    likes: NotRequired['base_likes']

class newsfeed_comments_item_type_photo(photos_photo, newsfeed_comments_item_base):
    comments: NotRequired['newsfeed_comments_base']
    likes: NotRequired['base_likes']

class newsfeed_comments_item_type_video(video_video, newsfeed_comments_item_base):
    text: NotRequired[str]
    comments: NotRequired['newsfeed_comments_base']
    likes: NotRequired['base_likes']
    type: NotRequired[Literal['video', 'music_video', 'movie', 'live', 'short_video']]

class newsfeed_item_photo(wall_carousel_base, newsfeed_item_base):
    photos: NotRequired['newsfeed_item_photo_photos']
    post_id: NotRequired[int]  # Post ID

class newsfeed_item_photo_tag(wall_carousel_base, newsfeed_item_base):
    photo_tags: NotRequired['newsfeed_item_photo_tag_photo_tags']
    post_id: NotRequired[int]  # Post ID

class newsfeed_item_video(wall_carousel_base, newsfeed_item_base):
    video: NotRequired['newsfeed_item_video_video']
    post_id: NotRequired[int]  # Post ID

class wall_wallpost_full(wall_carousel_base, wall_wallpost):
    copy_history: NotRequired[List['wall_wallpost_full']]
    can_edit: NotRequired['base_bool_int']  # Information whether current user can edit the post
    created_by: NotRequired[int]  # Post creator ID (if post still can be edited)
    can_delete: NotRequired['base_bool_int']  # Information whether current user can delete the post
    can_pin: NotRequired['base_bool_int']  # Information whether current user can pin the post
    donut: NotRequired['wall_wallpost_donut']
    is_pinned: NotRequired['base_bool_int']  # Information whether the post is pinned
    comments: NotRequired['base_comments_info']
    marked_as_ads: NotRequired['base_bool_int']  # Information whether the post is marked as ads
    topic_id: NotRequired[Literal[0, 1, 7, 12, 16, 19, 21, 23, 25, 26, 32, 43]]  # Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method
    short_text_rate: NotRequired[float]  # Preview length control parameter
    hash: NotRequired[str]  # Hash for sharing
    type: NotRequired['wall_post_type']
    feedback: NotRequired['newsfeed_item_wallpost_feedback']
    to_id: NotRequired[int]

class newsfeed_comments_item_type_post(wall_wallpost_full, newsfeed_comments_item_base):
    from_id: NotRequired[int]
    comments: NotRequired['newsfeed_comments_base']

class newsfeed_item_wallpost(wall_carousel_base, newsfeed_item_base, wall_wallpost_full): ...  # type: ignore

