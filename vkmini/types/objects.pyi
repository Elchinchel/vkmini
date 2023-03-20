from typing import TYPE_CHECKING, Any, Dict, List, Union, Literal, TypeAlias
from typing_extensions import TypedDict, NotRequired

if TYPE_CHECKING:
    from . import objects, methods, responses  # type: ignore


class account_account_counters(TypedDict):
    app_requests: NotRequired[int]  # New app requests number
    events: NotRequired[int]  # New events number
    faves: NotRequired[int]  # New faves number
    friends: NotRequired[int]  # New friends requests number
    friends_suggestions: NotRequired[int]  # New friends suggestions number
    friends_recommendations: NotRequired[int]  # New friends recommendations number
    gifts: NotRequired[int]  # New gifts number
    groups: NotRequired[int]  # New groups number
    menu_discover_badge: NotRequired[int]
    menu_clips_badge: NotRequired[int]
    messages: NotRequired[int]  # New messages number
    memories: NotRequired[int]  # New memories number
    notes: NotRequired[int]  # New notes number
    notifications: NotRequired[int]  # New notifications number
    photos: NotRequired[int]  # New photo tags number
    sdk: NotRequired[int]  # New sdk number

class account_info(TypedDict):
    wishlists_ae_promo_banner_show: NotRequired['objects.base_bool_int']
    # 2fa_required: NotRequired['objects.base_bool_int']  # Two factor authentication is enabled
    country: NotRequired[str]  # Country code
    https_required: NotRequired['objects.base_bool_int']  # Information whether HTTPS-only is enabled
    intro: NotRequired['objects.base_bool_int']  # Information whether user has been processed intro
    show_vk_apps_intro: NotRequired[bool]
    mini_apps_ads_slot_id: NotRequired[int]  # Ads slot id for MyTarget
    qr_promotion: NotRequired[int]
    link_redirects: NotRequired[Dict[str, Any]]
    lang: NotRequired[int]  # Language ID
    no_wall_replies: NotRequired['objects.base_bool_int']  # Information whether wall comments should be hidden
    own_posts_default: NotRequired['objects.base_bool_int']  # Information whether only owners posts should be shown
    subscriptions: NotRequired[List[int]]

class account_name_request(TypedDict):
    first_name: NotRequired[str]  # First name in request
    id: NotRequired[int]  # Request ID needed to cancel the request
    last_name: NotRequired[str]  # Last name in request
    status: NotRequired['objects.account_name_request_status']
    lang: NotRequired[str]  # Text to display to user
    link_href: NotRequired[str]  # href for link in lang field
    link_label: NotRequired[str]  # label to display for link in lang field

account_name_request_status: TypeAlias = Literal['success', 'processing', 'declined', 'was_accepted', 'was_declined', 'declined_with_link', 'response', 'response_with_link']  # Request status

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
    items: NotRequired[List['objects.account_push_conversations_item']]

class account_push_conversations_item(TypedDict):
    disabled_until: int  # Time until that notifications are disabled in seconds
    peer_id: int  # Peer ID
    sound: 'objects.base_bool_int'  # Information whether the sound are enabled

class account_push_params(TypedDict):
    msg: NotRequired[List['objects.account_push_params_mode']]
    chat: NotRequired[List['objects.account_push_params_mode']]
    like: NotRequired[List['objects.account_push_params_settings']]
    repost: NotRequired[List['objects.account_push_params_settings']]
    comment: NotRequired[List['objects.account_push_params_settings']]
    mention: NotRequired[List['objects.account_push_params_settings']]
    reply: NotRequired[List['objects.account_push_params_onoff']]
    new_post: NotRequired[List['objects.account_push_params_onoff']]
    wall_post: NotRequired[List['objects.account_push_params_onoff']]
    wall_publish: NotRequired[List['objects.account_push_params_onoff']]
    friend: NotRequired[List['objects.account_push_params_onoff']]
    friend_found: NotRequired[List['objects.account_push_params_onoff']]
    friend_accepted: NotRequired[List['objects.account_push_params_onoff']]
    group_invite: NotRequired[List['objects.account_push_params_onoff']]
    group_accepted: NotRequired[List['objects.account_push_params_onoff']]
    birthday: NotRequired[List['objects.account_push_params_onoff']]
    event_soon: NotRequired[List['objects.account_push_params_onoff']]
    app_request: NotRequired[List['objects.account_push_params_onoff']]
    sdk_open: NotRequired[List['objects.account_push_params_onoff']]

account_push_params_mode: TypeAlias = Literal['on', 'off', 'no_sound', 'no_text']  # Settings parameters

account_push_params_onoff: TypeAlias = Literal['on', 'off']  # Settings parameters

account_push_params_settings: TypeAlias = Literal['on', 'off', 'fr_of_fr']  # Settings parameters

class account_push_settings(TypedDict):
    disabled: NotRequired['objects.base_bool_int']  # Information whether notifications are disabled
    disabled_until: NotRequired[int]  # Time until that notifications are disabled in Unixtime
    settings: NotRequired['objects.account_push_params']
    conversations: NotRequired['objects.account_push_conversations']

class account_user_settings(objects.users_user_min, objects.users_user_settings_xtr):
    photo_200: NotRequired[str]  # URL of square photo of the user with 200 pixels in width
    is_service_account: NotRequired[bool]  # flag about service account

class account_user_settings_interest(TypedDict):
    title: str
    value: str

class account_user_settings_interests(TypedDict):
    activities: NotRequired['objects.account_user_settings_interest']
    interests: NotRequired['objects.account_user_settings_interest']
    music: NotRequired['objects.account_user_settings_interest']
    tv: NotRequired['objects.account_user_settings_interest']
    movies: NotRequired['objects.account_user_settings_interest']
    books: NotRequired['objects.account_user_settings_interest']
    games: NotRequired['objects.account_user_settings_interest']
    quotes: NotRequired['objects.account_user_settings_interest']
    about: NotRequired['objects.account_user_settings_interest']

addresses_fields: TypeAlias = Literal['id', 'title', 'address', 'additional_address', 'country_id', 'city_id', 'metro_station_id', 'latitude', 'longitude', 'distance', 'work_info_status', 'timetable', 'phone', 'time_offset']

ads_access_role: TypeAlias = Literal['admin', 'manager', 'reports']  # Current user's role

ads_access_role_public: TypeAlias = Literal['manager', 'reports']  # Current user's role

class ads_accesses(TypedDict):
    client_id: NotRequired[str]  # Client ID
    role: NotRequired['objects.ads_access_role']

class ads_account(TypedDict):
    access_role: 'objects.ads_access_role'
    account_id: int  # Account ID
    account_status: 'objects.base_bool_int'  # Information whether account is active
    account_type: 'objects.ads_account_type'
    account_name: str  # Account name

ads_account_type: TypeAlias = Literal['general', 'agency']  # Account type

class ads_ad(TypedDict):
    ad_format: int  # Ad format
    ad_platform: NotRequired[Union[int, str]]  # Ad platform
    all_limit: int  # Total limit
    approved: 'objects.ads_ad_approved'
    campaign_id: int  # Campaign ID
    category1_id: NotRequired[int]  # Category ID
    category2_id: NotRequired[int]  # Additional category ID
    cost_type: 'objects.ads_ad_cost_type'
    cpc: NotRequired[int]  # Cost of a click, kopecks
    cpm: NotRequired[int]  # Cost of 1000 impressions, kopecks
    cpa: NotRequired[int]  # Cost of an action, kopecks
    ocpm: NotRequired[int]  # Cost of 1000 impressions optimized, kopecks
    autobidding_max_cost: NotRequired[int]  # Max cost of target actions for autobidding, kopecks
    disclaimer_medical: NotRequired['objects.base_bool_int']  # Information whether disclaimer is enabled
    disclaimer_specialist: NotRequired['objects.base_bool_int']  # Information whether disclaimer is enabled
    disclaimer_supplements: NotRequired['objects.base_bool_int']  # Information whether disclaimer is enabled
    id: int  # Ad ID
    impressions_limit: NotRequired[int]  # Impressions limit
    impressions_limited: NotRequired['objects.base_bool_int']  # Information whether impressions are limited
    name: str  # Ad title
    status: 'objects.ads_ad_status'
    video: NotRequired['objects.base_bool_int']  # Information whether the ad is a video

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

class ads_ad_layout(TypedDict):
    ad_format: int  # Ad format
    campaign_id: int  # Campaign ID
    cost_type: 'objects.ads_ad_cost_type'
    description: str  # Ad description
    id: int  # Ad ID
    image_src: str  # Image URL
    image_src_2x: NotRequired[str]  # URL of the preview image in double size
    link_domain: NotRequired[str]  # Domain of advertised object
    link_url: str  # URL of advertised object
    preview_link: NotRequired[Union[int, str]]  # link to preview an ad as it is shown on the website
    title: str  # Ad title
    video: NotRequired['objects.base_bool_int']  # Information whether the ad is a video

ads_ad_status = Literal[
    0,  # stopped
    1,  # started
    2  # deleted
]

class ads_campaign(TypedDict):
    all_limit: str  # Campaign's total limit, rubles
    day_limit: str  # Campaign's day limit, rubles
    id: int  # Campaign ID
    name: str  # Campaign title
    start_time: int  # Campaign start time, as Unixtime
    status: 'objects.ads_campaign_status'
    stop_time: int  # Campaign stop time, as Unixtime
    type: 'objects.ads_campaign_type'

ads_campaign_status = Literal[
    0,  # stopped
    1,  # started
    2  # deleted
]

ads_campaign_type: TypeAlias = Literal['normal', 'vk_apps_managed', 'mobile_apps', 'promoted_posts']  # Campaign type

class ads_category(TypedDict):
    id: int  # Category ID
    name: str  # Category name
    subcategories: NotRequired[List['objects.base_object_with_name']]

class ads_client(TypedDict):
    all_limit: str  # Client's total limit, rubles
    day_limit: str  # Client's day limit, rubles
    id: int  # Client ID
    name: str  # Client name

class ads_criteria(TypedDict):
    age_from: NotRequired[int]  # Age from
    age_to: NotRequired[int]  # Age to
    apps: NotRequired[str]  # Apps IDs
    apps_not: NotRequired[str]  # Apps IDs to except
    birthday: NotRequired[int]  # Days to birthday
    cities: NotRequired[str]  # Cities IDs
    cities_not: NotRequired[str]  # Cities IDs to except
    country: NotRequired[int]  # Country ID
    districts: NotRequired[str]  # Districts IDs
    groups: NotRequired[str]  # Communities IDs
    interest_categories: NotRequired[str]  # Interests categories IDs
    interests: NotRequired[str]  # Interests
    paying: NotRequired['objects.base_bool_int']  # Information whether the user has proceeded VK payments before
    positions: NotRequired[str]  # Positions IDs
    religions: NotRequired[str]  # Religions IDs
    retargeting_groups: NotRequired[str]  # Retargeting groups IDs
    retargeting_groups_not: NotRequired[str]  # Retargeting groups IDs to except
    school_from: NotRequired[int]  # School graduation year from
    school_to: NotRequired[int]  # School graduation year to
    schools: NotRequired[str]  # Schools IDs
    sex: NotRequired['objects.ads_criteria_sex']
    stations: NotRequired[str]  # Stations IDs
    statuses: NotRequired[str]  # Relationship statuses
    streets: NotRequired[str]  # Streets IDs
    travellers: NotRequired['objects.base_property_exists']  # Travellers only
    uni_from: NotRequired[int]  # University graduation year from
    uni_to: NotRequired[int]  # University graduation year to
    user_browsers: NotRequired[str]  # Browsers
    user_devices: NotRequired[str]  # Devices
    user_os: NotRequired[str]  # Operating systems

ads_criteria_sex = Literal[
    0,  # any
    1,  # male
    2  # female
]

class ads_demo_stats(TypedDict):
    id: NotRequired[int]  # Object ID
    stats: NotRequired['objects.ads_demostats_format']
    type: NotRequired['objects.ads_object_type']

class ads_demostats_format(TypedDict):
    age: NotRequired[List['objects.ads_stats_age']]
    cities: NotRequired[List['objects.ads_stats_cities']]
    day: NotRequired[str]  # Day as YYYY-MM-DD
    month: NotRequired[str]  # Month as YYYY-MM
    overall: NotRequired[int]  # 1 if period=overall
    sex: NotRequired[List['objects.ads_stats_sex']]
    sex_age: NotRequired[List['objects.ads_stats_sex_age']]

class ads_flood_stats(TypedDict):
    left: int  # Requests left
    refresh: int  # Time to refresh in seconds

class ads_link_status(TypedDict):
    description: str  # Reject reason
    redirect_url: str  # URL
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
    save_audience_levels: NotRequired[List['objects.ads_lookalike_request_save_audience_level']]

class ads_lookalike_request_save_audience_level(TypedDict):
    level: NotRequired[int]  # Save audience level id, which is used in save audience queries
    audience_count: NotRequired[int]  # Saved audience audience size for according level

class ads_musician(TypedDict):
    id: int  # Targeting music artist ID
    name: str  # Music artist name

ads_object_type: TypeAlias = Literal['ad', 'campaign', 'client', 'office']  # Object type

class ads_paragraphs(TypedDict):
    paragraph: NotRequired[str]  # Rules paragraph

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
    video_views_50p: NotRequired[int]  # Video views for 50 percent
    video_views_75p: NotRequired[int]  # Video views for 75 percent
    video_views_start: NotRequired[int]  # Video starts

class ads_reject_reason(TypedDict):
    comment: NotRequired[str]  # Comment text
    rules: NotRequired[List['objects.ads_rules']]

class ads_rules(TypedDict):
    paragraphs: NotRequired[List['objects.ads_paragraphs']]
    title: NotRequired[str]  # Comment

class ads_stats(TypedDict):
    id: NotRequired[int]  # Object ID
    stats: NotRequired['objects.ads_stats_format']
    type: NotRequired['objects.ads_object_type']
    views_times: NotRequired['objects.ads_stats_views_times']

class ads_stats_age(TypedDict):
    clicks_rate: NotRequired[float]  # Clicks rate
    impressions_rate: NotRequired[float]  # Impressions rate
    value: NotRequired[str]  # Age interval

class ads_stats_cities(TypedDict):
    clicks_rate: NotRequired[float]  # Clicks rate
    impressions_rate: NotRequired[float]  # Impressions rate
    name: NotRequired[str]  # City name
    value: NotRequired[int]  # City ID

class ads_stats_format(TypedDict):
    clicks: NotRequired[int]  # Clicks number
    day: NotRequired[str]  # Day as YYYY-MM-DD
    impressions: NotRequired[int]  # Impressions number
    join_rate: NotRequired[int]  # Events number
    month: NotRequired[str]  # Month as YYYY-MM
    overall: NotRequired[int]  # 1 if period=overall
    reach: NotRequired[int]  # Reach
    spent: NotRequired[int]  # Spent funds
    video_clicks_site: NotRequired[int]  # Clickthoughs to the advertised site
    video_views: NotRequired[int]  # Video views number
    video_views_full: NotRequired[int]  # Video views (full video)
    video_views_half: NotRequired[int]  # Video views (half of video)

class ads_stats_sex(TypedDict):
    clicks_rate: NotRequired[float]  # Clicks rate
    impressions_rate: NotRequired[float]  # Impressions rate
    value: NotRequired['objects.ads_stats_sex_value']

class ads_stats_sex_age(TypedDict):
    clicks_rate: NotRequired[float]  # Clicks rate
    impressions_rate: NotRequired[float]  # Impressions rate
    value: NotRequired[str]  # Sex and age interval

ads_stats_sex_value = Literal[
    'f',  # female
    'm'  # male
]

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

class ads_targ_settings(objects.ads_criteria):
    id: NotRequired[int]  # Ad ID
    campaign_id: NotRequired[int]  # Campaign ID

class ads_targ_stats(TypedDict):
    audience_count: int  # Audience
    recommended_cpc: NotRequired[float]  # Recommended CPC value for 50% reach (old format)
    recommended_cpm: NotRequired[float]  # Recommended CPM value for 50% reach (old format)
    recommended_cpc_50: NotRequired[float]  # Recommended CPC value for 50% reach
    recommended_cpm_50: NotRequired[float]  # Recommended CPM value for 50% reach
    recommended_cpc_70: NotRequired[float]  # Recommended CPC value for 70% reach
    recommended_cpm_70: NotRequired[float]  # Recommended CPM value for 70% reach
    recommended_cpc_90: NotRequired[float]  # Recommended CPC value for 90% reach
    recommended_cpm_90: NotRequired[float]  # Recommended CPM value for 90% reach

class ads_targ_suggestions(TypedDict):
    id: NotRequired[int]  # Object ID
    name: NotRequired[str]  # Object name

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
    type: NotRequired['objects.ads_targ_suggestions_schools_type']

ads_targ_suggestions_schools_type: TypeAlias = Literal['school', 'university', 'faculty', 'chair']  # School type

class ads_target_group(TypedDict):
    audience_count: NotRequired[int]  # Audience
    domain: NotRequired[str]  # Site domain
    id: NotRequired[int]  # Group ID
    lifetime: NotRequired[int]  # Number of days for user to be in group
    name: NotRequired[str]  # Group name
    pixel: NotRequired[str]  # Pixel code

class ads_updateOfficeUsers_result(TypedDict):
    user_id: int
    is_success: bool
    error: NotRequired['objects.base_error']

class ads_user_specification(TypedDict):
    user_id: int
    role: 'objects.ads_access_role_public'
    grant_access_to_all_clients: NotRequired[bool]
    client_ids: NotRequired[List[int]]
    view_budget: NotRequired[bool]

class ads_user_specification_cutted(TypedDict):
    user_id: int
    role: 'objects.ads_access_role_public'
    client_id: NotRequired[int]
    view_budget: NotRequired[bool]

class ads_users(TypedDict):
    accesses: List['objects.ads_accesses']
    user_id: int  # User ID

class adsweb_getAdCategories_response_categories_category(TypedDict):
    id: int
    name: str

class adsweb_getAdUnits_response_ad_units_ad_unit(TypedDict):
    id: int
    site_id: int
    name: NotRequired[str]
    params: NotRequired['adsweb_getAdUnits_response_ad_units_ad_unit_params']

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
    stats: NotRequired[List['adsweb_getStatistics_response_items_item_stats_period']]

class appWidgets_photo(TypedDict):
    id: str  # Image ID
    images: List['objects.base_image']
    type: 'objects.appWidgets_photo_type'

class appWidgets_photos(TypedDict):
    count: NotRequired[int]
    items: NotRequired[List['objects.appWidgets_photo']]

class apps_app(objects.apps_app_min):
    author_url: NotRequired[str]  # Application author's URL
    banner_1120: NotRequired[str]  # URL of the app banner with 1120 px in width
    banner_560: NotRequired[str]  # URL of the app banner with 560 px in width
    icon_16: NotRequired[str]  # URL of the app icon with 16 px in width
    is_new: NotRequired['objects.base_bool_int']  # Is new flag
    push_enabled: NotRequired['objects.base_bool_int']  # Is push enabled
    screen_orientation: NotRequired[int]  # Screen orientation
    friends: NotRequired[List[int]]
    catalog_position: NotRequired[int]  # Catalog position
    description: NotRequired[str]  # Application description
    genre: NotRequired[str]  # Genre name
    genre_id: NotRequired[int]  # Genre ID
    international: NotRequired[bool]  # Information whether the application is multilanguage
    is_in_catalog: NotRequired[int]  # Information whether application is in mobile catalog
    leaderboard_type: NotRequired['objects.apps_app_leaderboard_type']
    members_count: NotRequired[int]  # Members number
    platform_id: NotRequired[str]  # Application ID in store
    published_date: NotRequired[int]  # Date when the application has been published in Unixtime
    screen_name: NotRequired[str]  # Screen name
    section: NotRequired[str]  # Application section name

apps_app_leaderboard_type = Literal[
    0,  # not supported
    1,  # levels
    2  # points
]

class apps_app_min(TypedDict):
    type: 'objects.apps_app_type'
    id: int  # Application ID
    title: str  # Application title
    author_owner_id: NotRequired[int]  # Application author's ID
    is_installed: NotRequired[bool]  # Is application installed
    icon_139: NotRequired[str]  # URL of the app icon with 139 px in width
    icon_150: NotRequired[str]  # URL of the app icon with 150 px in width
    icon_278: NotRequired[str]  # URL of the app icon with 278 px in width
    icon_576: NotRequired[str]  # URL of the app icon with 576 px in width
    background_loader_color: NotRequired[str]  # Hex color code without hash sign
    loader_icon: NotRequired[str]  # SVG data
    icon_75: NotRequired[str]  # URL of the app icon with 75 px in width

apps_app_type: TypeAlias = Literal['app', 'game', 'site', 'standalone', 'vk_app', 'community_app', 'html5_game', 'mini_app']  # Application type

class apps_leaderboard(TypedDict):
    level: NotRequired[int]  # Level
    points: NotRequired[int]  # Points number
    score: NotRequired[int]  # Score number
    user_id: int  # User ID

class apps_scope(TypedDict):
    '''Scope description'''
    name: Literal['friends', 'photos', 'video', 'pages', 'status', 'notes', 'wall', 'docs', 'groups', 'stats', 'market']  # Scope name
    title: NotRequired[str]  # Scope title

class audio_audio(TypedDict):
    artist: str  # Artist name
    id: int  # Audio ID
    title: str  # Title
    url: NotRequired[str]  # URL of mp3 file
    duration: int  # Duration in seconds
    date: NotRequired[int]  # Date when uploaded
    album_id: NotRequired[int]  # Album ID
    genre_id: NotRequired[int]  # Genre ID
    performer: NotRequired[str]  # Performer name

base_bool_int = Literal[
    0,  # no
    1  # yes
]

class base_city(TypedDict):
    id: int  # City ID
    title: str  # City title

class base_comments_info(TypedDict):
    can_post: NotRequired['objects.base_bool_int']  # Information whether current user can comment the post
    count: NotRequired[int]  # Comments number
    groups_can_post: NotRequired[bool]  # Information whether groups can comment the post

class base_country(TypedDict):
    id: int  # Country ID
    title: str  # Country title

class base_crop_photo(TypedDict):
    photo: 'objects.photos_photo'
    crop: 'objects.base_crop_photo_crop'
    rect: 'objects.base_crop_photo_rect'

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
    error_code: NotRequired[int]  # Error code
    error_subcode: NotRequired[int]  # Error subcode
    error_msg: NotRequired[str]  # Error message
    error_text: NotRequired[str]  # Localized error message
    request_params: NotRequired[List['objects.base_request_param']]

class base_geo(TypedDict):
    coordinates: NotRequired['objects.base_geo_coordinates']
    place: NotRequired['objects.base_place']
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
    height: int  # Image height
    url: str  # Image url
    width: int  # Image width

class base_likes(TypedDict):
    count: NotRequired[int]  # Likes number
    user_likes: NotRequired['objects.base_bool_int']  # Information whether current user likes the photo

class base_likes_info(TypedDict):
    can_like: 'objects.base_bool_int'  # Information whether current user can like the post
    can_publish: NotRequired['objects.base_bool_int']  # Information whether current user can repost
    count: int  # Likes number
    user_likes: int  # Information whether current uer has liked the post

class base_link(TypedDict):
    application: NotRequired['objects.base_link_application']
    button: NotRequired['objects.base_link_button']
    caption: NotRequired[str]  # Link caption
    description: NotRequired[str]  # Link description
    id: NotRequired[str]  # Link ID
    is_favorite: NotRequired[bool]
    photo: NotRequired['objects.photos_photo']
    preview_page: NotRequired[str]  # String ID of the page with article preview
    preview_url: NotRequired[str]  # URL of the page with article preview
    product: NotRequired['objects.base_link_product']
    rating: NotRequired['objects.base_link_rating']
    title: NotRequired[str]  # Link title
    url: str  # Link URL
    target_object: NotRequired['objects.link_target_object']
    is_external: NotRequired[bool]  # Information whether the current link is external
    video: NotRequired['objects.video_video']  # Video from link

class base_link_application(TypedDict):
    app_id: NotRequired[float]  # Application Id
    store: NotRequired['objects.base_link_application_store']

class base_link_application_store(TypedDict):
    id: NotRequired[float]  # Store Id
    name: NotRequired[str]  # Store name

class base_link_button(TypedDict):
    action: NotRequired['objects.base_link_button_action']  # Button action
    title: NotRequired[str]  # Button title
    block_id: NotRequired[str]  # Target block id
    section_id: NotRequired[str]  # Target section id
    owner_id: NotRequired[int]  # Owner id
    icon: NotRequired[str]  # Button icon name, e.g. 'phone' or 'gift'
    style: NotRequired['objects.base_link_button_style']

class base_link_button_action(TypedDict):
    type: NotRequired['objects.base_link_button_action_type']
    url: NotRequired[str]  # Action URL
    consume_reason: NotRequired[str]

base_link_button_action_type = Literal[
    'open_url'  # open_url
]

base_link_button_style: TypeAlias = str  # Button style

class base_link_product(TypedDict):
    price: 'objects.market_price'
    merchant: NotRequired[str]
    orders_count: NotRequired[int]

base_link_product_status: TypeAlias = Literal['active', 'blocked', 'sold', 'deleted', 'archived']  # Status representation

class base_link_rating(TypedDict):
    reviews_count: NotRequired[int]  # Count of reviews
    stars: NotRequired[float]  # Count of stars

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

class base_place(TypedDict):
    address: NotRequired[str]  # Place address
    checkins: NotRequired[int]  # Checkins number
    city: NotRequired[str]  # City name
    country: NotRequired[str]  # Country name
    created: NotRequired[int]  # Date of the place creation in Unixtime
    icon: NotRequired[str]  # URL of the place's icon
    id: NotRequired[int]  # Place ID
    latitude: NotRequired[float]  # Place latitude
    longitude: NotRequired[float]  # Place longitude
    title: NotRequired[str]  # Place title
    type: NotRequired[str]  # Place type

base_property_exists = Literal[
    1  # Property exists
]

class base_reposts_info(TypedDict):
    '''Count of views'''
    count: NotRequired[int]  # Total reposts counter. Sum of wall and mail reposts counters
    wall_count: NotRequired[int]  # Wall reposts counter
    mail_count: NotRequired[int]  # Mail reposts counter
    user_reposted: NotRequired[int]  # Information whether current user has reposted the post

class base_request_param(TypedDict):
    key: NotRequired[str]  # Parameter name
    value: NotRequired[str]  # Parameter value

base_sex = Literal[
    0,  # unknown
    1,  # female
    2  # male
]

class base_sticker(TypedDict):
    sticker_id: NotRequired[int]  # Sticker ID
    product_id: NotRequired[int]  # Pack ID
    images: NotRequired[List['objects.base_image']]
    images_with_background: NotRequired[List['objects.base_image']]
    animation_url: NotRequired[str]  # URL of sticker animation script
    animations: NotRequired[List['objects.base_sticker_animation']]  # Array of sticker animation script objects
    is_allowed: NotRequired[bool]  # Information whether the sticker is allowed

class base_sticker_animation(TypedDict):
    type: NotRequired[Literal['light', 'dark']]  # Type of animation script
    url: NotRequired[str]  # URL of animation script

class base_upload_server(TypedDict):
    upload_url: str  # Upload URL

base_user_group_fields: TypeAlias = Literal['about', 'action_button', 'activities', 'activity', 'addresses', 'admin_level', 'age_limits', 'author_id', 'ban_info', 'bdate', 'blacklisted', 'blacklisted_by_me', 'books', 'can_create_topic', 'can_message', 'can_post', 'can_see_all_posts', 'can_see_audio', 'can_send_friend_request', 'can_upload_video', 'can_write_private_message', 'career', 'city', 'common_count', 'connections', 'contacts', 'counters', 'country', 'cover', 'crop_photo', 'deactivated', 'description', 'domain', 'education', 'exports', 'finish_date', 'fixed_post', 'followers_count', 'friend_status', 'games', 'has_market_app', 'has_mobile', 'has_photo', 'home_town', 'id', 'interests', 'is_admin', 'is_closed', 'is_favorite', 'is_friend', 'is_hidden_from_feed', 'is_member', 'is_messages_blocked', 'can_send_notify', 'is_subscribed', 'last_seen', 'links', 'lists', 'maiden_name', 'main_album_id', 'main_section', 'market', 'member_status', 'members_count', 'military', 'movies', 'music', 'name', 'nickname', 'occupation', 'online', 'online_status', 'personal', 'phone', 'photo_100', 'photo_200', 'photo_200_orig', 'photo_400_orig', 'photo_50', 'photo_id', 'photo_max', 'photo_max_orig', 'quotes', 'relation', 'relatives', 'schools', 'screen_name', 'sex', 'site', 'start_date', 'status', 'timezone', 'trending', 'tv', 'type', 'universities', 'verified', 'wall_comments', 'wiki_page', 'vk_admin_status']

class base_user_id(TypedDict):
    user_id: NotRequired[int]  # User ID

board_default_order = Literal[
    1,  # desc_updated
    2,  # desc_created
    -1,  # asc_updated
    -2  # asc_created
]

class board_topic(TypedDict):
    comments: NotRequired[int]  # Comments number
    created: NotRequired[int]  # Date when the topic has been created in Unixtime
    created_by: NotRequired[int]  # Creator ID
    id: NotRequired[int]  # Topic ID
    is_closed: NotRequired['objects.base_bool_int']  # Information whether the topic is closed
    is_fixed: NotRequired['objects.base_bool_int']  # Information whether the topic is fixed
    title: NotRequired[str]  # Topic title
    updated: NotRequired[int]  # Date when the topic has been updated in Unixtime
    updated_by: NotRequired[int]  # ID of user who updated the topic

class board_topic_comment(TypedDict):
    attachments: NotRequired[List['objects.wall_comment_attachment']]
    date: int  # Date when the comment has been added in Unixtime
    from_id: int  # Author ID
    id: int  # Comment ID
    real_offset: NotRequired[int]  # Real position of the comment
    text: str  # Comment text
    can_edit: NotRequired['objects.base_bool_int']  # Information whether current user can edit the comment
    likes: NotRequired['objects.base_likes_info']

class board_topic_poll(TypedDict):
    answer_id: int  # Current user's answer ID
    answers: List['objects.polls_answer']
    created: int  # Date when poll has been created in Unixtime
    is_closed: NotRequired['objects.base_bool_int']  # Information whether the poll is closed
    owner_id: int  # Poll owner's ID
    poll_id: int  # Poll ID
    question: str  # Poll question
    votes: str  # Votes number

class callback_board_post_delete(TypedDict):
    topic_owner_id: int
    topic_id: int
    id: int

class callback_confirmation_message(TypedDict):
    type: 'objects.callback_message_type'
    group_id: int
    secret: str

class callback_group_change_photo(TypedDict):
    user_id: int
    photo: 'objects.photos_photo'

class callback_group_change_settings(TypedDict):
    user_id: int
    self: 'objects.base_bool_int'

class callback_group_join(TypedDict):
    user_id: int
    join_type: 'objects.callback_group_join_type'

callback_group_join_type: TypeAlias = Literal['join', 'unsure', 'accepted', 'approved', 'request']

class callback_group_leave(TypedDict):
    user_id: NotRequired[int]
    self: NotRequired['objects.base_bool_int']

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

class callback_group_officers_edit(TypedDict):
    admin_id: int
    user_id: int
    level_old: 'objects.callback_group_officer_role'
    level_new: 'objects.callback_group_officer_role'

class callback_group_settings_changes(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    access: NotRequired['objects.groups_group_is_closed']
    screen_name: NotRequired[str]
    public_category: NotRequired[int]
    public_subcategory: NotRequired[int]
    age_limits: NotRequired['objects.groups_group_full_age_limits']
    website: NotRequired[str]
    enable_status_default: NotRequired['objects.groups_group_wall']
    enable_audio: NotRequired['objects.groups_group_audio']
    enable_video: NotRequired['objects.groups_group_video']
    enable_photo: NotRequired['objects.groups_group_photos']
    enable_market: NotRequired['objects.callback_group_market']

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
    market_owner_od: NotRequired[int]
    photo_id: NotRequired[int]

class callback_market_comment_delete(TypedDict):
    owner_id: int
    id: int
    user_id: int
    item_id: int

class callback_message_allow(TypedDict):
    user_id: int
    key: str

class callback_message_base(TypedDict):
    type: 'objects.callback_message_type'
    object: Dict[str, Any]
    group_id: int

class callback_message_deny(TypedDict):
    user_id: int

callback_message_type: TypeAlias = Literal['confirmation', 'group_change_photo', 'group_change_settings', 'group_officers_edit', 'lead_forms_new', 'market_comment_delete', 'market_comment_edit', 'market_comment_restore', 'message_allow', 'message_deny', 'message_read', 'message_reply', 'message_typing_state', 'messages_edit', 'photo_comment_delete', 'photo_comment_edit', 'photo_comment_restore', 'poll_vote_new', 'user_block', 'user_unblock', 'video_comment_delete', 'video_comment_edit', 'video_comment_restore', 'wall_reply_delete', 'wall_reply_restore', 'wall_repost']

class callback_photo_comment(TypedDict):
    id: int
    from_id: int
    date: int
    text: str
    photo_owner_od: int

class callback_photo_comment_delete(TypedDict):
    id: int
    owner_id: int
    user_id: int
    photo_id: int

class callback_poll_vote_new(TypedDict):
    owner_id: int
    poll_id: int
    option_id: int
    user_id: int

class callback_qr_scan(TypedDict):
    user_id: int
    data: str
    type: str
    subtype: str
    reread: bool

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

class callback_video_comment(TypedDict):
    id: int
    from_id: int
    date: int
    text: str
    video_owner_od: int

class callback_video_comment_delete(TypedDict):
    id: int
    owner_id: int
    user_id: int
    video_id: int

class callback_wall_comment_delete(TypedDict):
    owner_id: int
    id: int
    user_id: int
    post_id: int

class comment_thread(TypedDict):
    can_post: NotRequired[bool]  # Information whether current user can comment the post
    count: int  # Comments number
    groups_can_post: NotRequired[bool]  # Information whether groups can comment the post
    items: NotRequired[List['objects.wall_wall_comment']]
    show_reply_button: NotRequired[bool]  # Information whether recommended to display reply button

class database_city(objects.base_object):
    area: NotRequired[str]  # Area title
    region: NotRequired[str]  # Region title
    important: NotRequired['objects.base_bool_int']  # Information whether the city is included in important cities list

class database_faculty(TypedDict):
    id: NotRequired[int]  # Faculty ID
    title: NotRequired[str]  # Faculty title

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
    preview: NotRequired['objects.docs_doc_preview']
    is_licensed: NotRequired['objects.base_bool_int']
    access_key: NotRequired[str]  # Access key for the document
    tags: NotRequired[List[str]]  # Document tags

docs_doc_attachment_type: TypeAlias = Literal['doc', 'graffiti', 'audio_message']  # Doc attachment type

class docs_doc_preview(TypedDict):
    audio_msg: NotRequired['objects.docs_doc_preview_audio_msg']
    graffiti: NotRequired['objects.docs_doc_preview_graffiti']
    photo: NotRequired['objects.docs_doc_preview_photo']
    video: NotRequired['objects.docs_doc_preview_video']

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
    sizes: NotRequired[List['objects.docs_doc_preview_photo_sizes']]

class docs_doc_preview_photo_sizes(TypedDict):
    src: str  # URL of the image
    width: int  # Width in px
    height: int  # Height in px
    type: 'objects.photos_photo_sizes_type'

class docs_doc_preview_video(TypedDict):
    src: str  # Video URL
    width: int  # Video's width in pixels
    height: int  # Video's height in pixels
    file_size: int  # Video file size in bites

class docs_doc_types(TypedDict):
    id: int  # Doc type ID
    name: str  # Doc type title
    count: int  # Number of docs

class docs_doc_upload_response(TypedDict):
    file: NotRequired[str]  # Uploaded file data

class events_event_attach(TypedDict):
    address: NotRequired[str]  # address of event
    button_text: str  # text of attach
    friends: List[int]  # array of friends ids
    id: int  # event ID
    is_favorite: bool  # is favorite
    member_status: NotRequired['objects.groups_group_full_member_status']  # Current user's member status
    text: str  # text of attach
    time: NotRequired[int]  # event start time

class fave_bookmark(TypedDict):
    added_date: int  # Timestamp, when this item was bookmarked
    link: NotRequired['objects.base_link']
    post: NotRequired['objects.wall_wallpost_full']
    product: NotRequired['objects.market_market_item']
    seen: bool  # Has user seen this item
    tags: List['objects.fave_tag']
    type: 'objects.fave_bookmark_type'  # Item type
    video: NotRequired['objects.video_video']

fave_bookmark_type: TypeAlias = Literal['post', 'video', 'product', 'article', 'link']

class fave_page(TypedDict):
    description: str  # Some info about user or group
    group: NotRequired['objects.groups_group_full']
    tags: List['objects.fave_tag']
    type: 'objects.fave_page_type'  # Item type
    updated_date: NotRequired[int]  # Timestamp, when this page was bookmarked
    user: NotRequired['objects.users_user_full']

fave_page_type: TypeAlias = Literal['user', 'group', 'hints']

class fave_tag(TypedDict):
    id: NotRequired[int]  # Tag id
    name: NotRequired[str]  # Tag name

class friends_friend_extended_status(objects.friends_friend_status):
    is_request_unread: NotRequired[bool]  # Is friend request from other user unread

class friends_friend_status(TypedDict):
    friend_status: 'objects.friends_friend_status_status'
    sign: NotRequired[str]  # MD5 hash for the result validation
    user_id: int  # User ID

friends_friend_status_status = Literal[
    0,  # not a friend
    1,  # outcoming request
    2,  # incoming request
    3  # is friend
]

class friends_friends_list(TypedDict):
    id: int  # List ID
    name: str  # List title

class friends_mutual_friend(TypedDict):
    common_count: NotRequired[int]  # Total mutual friends number
    common_friends: NotRequired[List[int]]
    id: NotRequired[int]  # User ID

class friends_requests(TypedDict):
    # from: NotRequired[str]  # ID of the user by whom friend has been suggested
    mutual: NotRequired['objects.friends_requests_mutual']
    user_id: NotRequired[int]  # User ID

class friends_requests_mutual(TypedDict):
    count: NotRequired[int]  # Total mutual friends number
    users: NotRequired[List[int]]

class friends_requests_xtr_message(TypedDict):
    # from: NotRequired[str]  # ID of the user by whom friend has been suggested
    message: NotRequired[str]  # Message sent with a request
    mutual: NotRequired['objects.friends_requests_mutual']
    user_id: NotRequired[int]  # User ID

class friends_user_xtr_lists(objects.users_user_full):
    lists: NotRequired[List[int]]

class friends_user_xtr_phone(objects.users_user_full):
    phone: NotRequired[str]  # User phone

class gifts_gift(TypedDict):
    date: NotRequired[int]  # Date when gist has been sent in Unixtime
    from_id: NotRequired[int]  # Gift sender ID
    gift: NotRequired['objects.gifts_layout']
    gift_hash: NotRequired[str]  # Hash
    id: NotRequired[int]  # Gift ID
    message: NotRequired[str]  # Comment text
    privacy: NotRequired['objects.gifts_gift_privacy']

gifts_gift_privacy = Literal[
    0,  # name and message for all
    1,  # name for all
    2  # name and message for recipient only
]

class gifts_layout(TypedDict):
    id: NotRequired[int]  # Gift ID
    thumb_512: NotRequired[str]  # URL of the preview image with 512 px in width
    thumb_256: NotRequired[str]  # URL of the preview image with 256 px in width
    thumb_48: NotRequired[str]  # URL of the preview image with 48 px in width
    thumb_96: NotRequired[str]  # URL of the preview image with 96 px in width
    stickers_product_id: NotRequired[int]  # ID of the sticker pack, if the gift is representing one
    build_id: NotRequired[str]  # ID of the build of constructor gift
    keywords: NotRequired[str]  # Keywords used for search

class groups_address(TypedDict):
    additional_address: NotRequired[str]  # Additional address to the place (6 floor, left door)
    address: NotRequired[str]  # String address to the place (Nevsky, 28)
    city_id: NotRequired[int]  # City id of address
    country_id: NotRequired[int]  # Country id of address
    distance: NotRequired[int]  # Distance from the point
    id: int  # Address id
    latitude: NotRequired[float]  # Address latitude
    longitude: NotRequired[float]  # Address longitude
    metro_station_id: NotRequired[int]  # Metro id of address
    phone: NotRequired[str]  # Address phone
    time_offset: NotRequired[int]  # Time offset int minutes from utc time
    timetable: NotRequired['objects.groups_address_timetable']  # Week timetable for the address
    title: NotRequired[str]  # Title of the place (Zinger, etc)
    work_info_status: NotRequired['objects.groups_address_work_info_status']  # Status of information about timetable

class groups_address_timetable(TypedDict):
    '''Timetable for a week'''
    fri: NotRequired['objects.groups_address_timetable_day']  # Timetable for friday
    mon: NotRequired['objects.groups_address_timetable_day']  # Timetable for monday
    sat: NotRequired['objects.groups_address_timetable_day']  # Timetable for saturday
    sun: NotRequired['objects.groups_address_timetable_day']  # Timetable for sunday
    thu: NotRequired['objects.groups_address_timetable_day']  # Timetable for thursday
    tue: NotRequired['objects.groups_address_timetable_day']  # Timetable for tuesday
    wed: NotRequired['objects.groups_address_timetable_day']  # Timetable for wednesday

class groups_address_timetable_day(TypedDict):
    '''Timetable for one day'''
    break_close_time: NotRequired[int]  # Close time of the break in minutes
    break_open_time: NotRequired[int]  # Start time of the break in minutes
    close_time: int  # Close time in minutes
    open_time: int  # Open time in minutes

groups_address_work_info_status: TypeAlias = Literal['no_information', 'temporarily_closed', 'always_opened', 'timetable', 'forever_closed']  # Status of information about timetable

class groups_addresses_info(TypedDict):
    is_enabled: bool  # Information whether addresses is enabled
    main_address_id: NotRequired[int]  # Main address id for group

class groups_ban_info(TypedDict):
    admin_id: NotRequired[int]  # Administrator ID
    comment: NotRequired[str]  # Comment for a ban
    comment_visible: NotRequired[bool]  # Show comment for user
    is_closed: NotRequired[bool]
    date: NotRequired[int]  # Date when user has been added to blacklist in Unixtime
    end_date: NotRequired[int]  # Date when user will be removed from blacklist in Unixtime
    reason: NotRequired['objects.groups_ban_info_reason']

groups_ban_info_reason = Literal[
    0,  # other
    1,  # spam
    2,  # verbal abuse
    3,  # strong language
    4  # flood
]

groups_banned_item: TypeAlias = 'objects.groups_owner_xtr_ban_info'

class groups_callback_server(TypedDict):
    id: int
    title: str
    creator_id: int
    url: str
    secret_key: str
    status: Literal['unconfigured', 'failed', 'wait', 'ok']

class groups_callback_settings(TypedDict):
    api_version: NotRequired[str]  # API version used for the events
    events: NotRequired['objects.groups_long_poll_events']

class groups_contacts_item(TypedDict):
    desc: NotRequired[str]  # Contact description
    email: NotRequired[str]  # Contact email
    phone: NotRequired[str]  # Contact phone
    user_id: NotRequired[int]  # User ID

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

class groups_cover(TypedDict):
    enabled: 'objects.base_bool_int'  # Information whether cover is enabled
    images: NotRequired[List['objects.base_image']]

groups_fields: TypeAlias = Literal['market', 'member_status', 'is_favorite', 'is_subscribed', 'city', 'country', 'verified', 'description', 'wiki_page', 'members_count', 'counters', 'cover', 'can_post', 'can_see_all_posts', 'activity', 'fixed_post', 'can_create_topic', 'can_upload_video', 'has_photo', 'status', 'main_album_id', 'links', 'contacts', 'site', 'main_section', 'trending', 'can_message', 'is_market_cart_enabled', 'is_messages_blocked', 'can_send_notify', 'online_status', 'start_date', 'finish_date', 'age_limits', 'ban_info', 'action_button', 'author_id', 'phone', 'has_market_app', 'addresses', 'live_covers', 'is_adult', 'can_subscribe_posts', 'warning_notification', 'msg_push_allowed', 'stories_archive_count', 'video_live_level', 'video_live_count', 'clips_count']

groups_filter: TypeAlias = Literal['admin', 'editor', 'moder', 'advertiser', 'groups', 'publics', 'events', 'has_addresses']

class groups_group(TypedDict):
    admin_level: NotRequired['objects.groups_group_admin_level']
    deactivated: NotRequired[str]  # Information whether community is banned
    finish_date: NotRequired[int]  # Finish date in Unixtime format
    id: NotRequired[int]  # Community ID
    is_admin: NotRequired['objects.base_bool_int']  # Information whether current user is administrator
    is_advertiser: NotRequired['objects.base_bool_int']  # Information whether current user is advertiser
    is_closed: NotRequired['objects.groups_group_is_closed']
    is_member: NotRequired['objects.base_bool_int']  # Information whether current user is member
    name: NotRequired[str]  # Community name
    photo_100: NotRequired[str]  # URL of square photo of the community with 100 pixels in width
    photo_200: NotRequired[str]  # URL of square photo of the community with 200 pixels in width
    photo_50: NotRequired[str]  # URL of square photo of the community with 50 pixels in width
    screen_name: NotRequired[str]  # Domain of the community page
    start_date: NotRequired[int]  # Start date in Unixtime format
    type: NotRequired['objects.groups_group_type']

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

class groups_group_attach(TypedDict):
    id: int  # group ID
    text: str  # text of attach
    status: str  # activity or category of group
    size: int  # size of group
    is_favorite: bool  # is favorite

groups_group_audio = Literal[
    0,  # disabled
    1,  # open
    2  # limited
]

class groups_group_ban_info(TypedDict):
    comment: NotRequired[str]  # Ban comment
    end_date: NotRequired[int]  # End date of ban in Unixtime
    reason: NotRequired['objects.groups_ban_info_reason']

class groups_group_category(TypedDict):
    id: int  # Category ID
    name: str  # Category name
    subcategories: NotRequired[List['objects.base_object_with_name']]

class groups_group_category_full(TypedDict):
    id: int  # Category ID
    name: str  # Category name
    page_count: int  # Pages number
    page_previews: List['objects.groups_group']
    subcategories: NotRequired[List['objects.groups_group_category']]

class groups_group_category_type(TypedDict):
    id: int
    name: str

groups_group_docs = Literal[
    0,  # disabled
    1,  # open
    2  # limited
]

class groups_group_full(objects.groups_group):
    market: NotRequired['objects.groups_market_info']
    member_status: NotRequired['objects.groups_group_full_member_status']  # Current user's member status
    is_adult: NotRequired['objects.base_bool_int']  # Information whether community is adult
    is_hidden_from_feed: NotRequired['objects.base_bool_int']  # Information whether community is hidden from current user's newsfeed
    is_favorite: NotRequired['objects.base_bool_int']  # Information whether community is in faves
    is_subscribed: NotRequired['objects.base_bool_int']  # Information whether current user is subscribed
    city: NotRequired['objects.base_object']
    country: NotRequired['objects.base_country']
    verified: NotRequired['objects.base_bool_int']  # Information whether community is verified
    description: NotRequired[str]  # Community description
    wiki_page: NotRequired[str]  # Community's main wiki page title
    members_count: NotRequired[int]  # Community members number
    video_live_level: NotRequired[int]  # Community level live streams achievements
    video_live_count: NotRequired[int]  # Number of community's live streams
    counters: NotRequired['objects.groups_counters_group']
    cover: NotRequired['objects.groups_cover']
    can_post: NotRequired['objects.base_bool_int']  # Information whether current user can post on community's wall
    can_see_all_posts: NotRequired['objects.base_bool_int']  # Information whether current user can see all posts on community's wall
    activity: NotRequired[str]  # Type of group, start date of event or category of public page
    fixed_post: NotRequired[int]  # Fixed post ID
    can_create_topic: NotRequired['objects.base_bool_int']  # Information whether current user can create topic
    can_upload_doc: NotRequired['objects.base_bool_int']  # Information whether current user can upload doc
    can_upload_story: NotRequired['objects.base_bool_int']  # Information whether current user can upload story
    can_upload_video: NotRequired['objects.base_bool_int']  # Information whether current user can upload video
    has_photo: NotRequired['objects.base_bool_int']  # Information whether community has photo
    crop_photo: NotRequired['objects.base_crop_photo']  # Данные о точках, по которым вырезаны профильная и миниатюрная фотографии сообщества
    status: NotRequired[str]  # Community status
    main_album_id: NotRequired[int]  # Community's main photo album ID
    links: NotRequired[List['objects.groups_links_item']]
    contacts: NotRequired[List['objects.groups_contacts_item']]
    wall: NotRequired[Literal[0, 1, 2, 3]]  # Information about wall status in community
    site: NotRequired[str]  # Community's website
    main_section: NotRequired['objects.groups_group_full_main_section']
    trending: NotRequired['objects.base_bool_int']  # Information whether the community has a "fire" pictogram.
    can_message: NotRequired['objects.base_bool_int']  # Information whether current user can send a message to community
    is_messages_blocked: NotRequired['objects.base_bool_int']  # Information whether community can send a message to current user
    can_send_notify: NotRequired['objects.base_bool_int']  # Information whether community can send notifications by phone number to current user
    online_status: NotRequired['objects.groups_online_status']  # Status of replies in community messages
    age_limits: NotRequired['objects.groups_group_full_age_limits']  # Information whether age limit
    ban_info: NotRequired['objects.groups_group_ban_info']  # User ban info
    has_market_app: NotRequired[bool]  # Information whether community has installed market app
    addresses: NotRequired['objects.groups_addresses_info']  # Info about addresses in groups
    is_subscribed_podcasts: NotRequired[bool]  # Information whether current user is subscribed to podcasts
    can_subscribe_podcasts: NotRequired[bool]  # Owner in whitelist or not
    can_subscribe_posts: NotRequired[bool]  # Can subscribe to wall
    live_covers: NotRequired['objects.groups_live_covers']  # Live covers state

groups_group_full_age_limits = Literal[
    1,  # no
    2,  # over 16
    3  # over 18
]

groups_group_full_main_section = Literal[
    0,  # absent
    1,  # photos
    2,  # topics
    3,  # audio
    4,  # video
    5  # market
]

groups_group_full_member_status = Literal[
    0,  # not a member
    1,  # member
    2,  # not sure
    3,  # declined
    4,  # has sent a request
    5  # invited
]

groups_group_is_closed = Literal[
    0,  # open
    1,  # closed
    2  # private
]

class groups_group_link(TypedDict):
    name: NotRequired[str]  # Link label
    desc: NotRequired[str]  # Link description
    edit_title: NotRequired['objects.base_bool_int']  # Information whether the title can be edited
    id: NotRequired[int]  # Link ID
    image_processing: NotRequired['objects.base_bool_int']  # Information whether the image on processing
    url: NotRequired[str]  # Link URL

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

class groups_group_public_category_list(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    subcategories: NotRequired[List['objects.groups_group_category_type']]

groups_group_role: TypeAlias = Literal['moderator', 'editor', 'administrator', 'advertiser']

groups_group_subject = Literal[
    '1',  # auto
    '2',  # activity holidays
    '3',  # business
    '4',  # pets
    '5',  # health
    '6',  # dating and communication
    '7',  # games
    '8',  # it
    '9',  # cinema
    '10',  # beauty and fashion
    '11',  # cooking
    '12',  # art and culture
    '13',  # literature
    '14',  # mobile services and internet
    '15',  # music
    '16',  # science and technology
    '17',  # real estate
    '18',  # news and media
    '19',  # security
    '20',  # education
    '21',  # home and renovations
    '22',  # politics
    '23',  # food
    '24',  # industry
    '25',  # travel
    '26',  # work
    '27',  # entertainment
    '28',  # religion
    '29',  # family
    '30',  # sports
    '31',  # insurance
    '32',  # television
    '33',  # goods and services
    '34',  # hobbies
    '35',  # finance
    '36',  # photo
    '37',  # esoterics
    '38',  # electronics and appliances
    '39',  # erotic
    '40',  # humor
    '41',  # society_humanities
    '42'  # design and graphics
]

class groups_group_tag(TypedDict):
    id: int
    name: str
    color: Literal['454647', '45678f', '4bb34b', '5181b8', '539b9c', '5c9ce6', '63b9ba', '6bc76b', '76787a', '792ec0', '7a6c4f', '7ececf', '9e8d6b', 'a162de', 'aaaeb3', 'bbaa84', 'e64646', 'ff5c5c', 'ffa000', 'ffc107']
    uses: NotRequired[int]

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

class groups_group_xtr_invited_by(TypedDict):
    admin_level: NotRequired['objects.groups_group_xtr_invited_by_admin_level']
    id: NotRequired[int]  # Community ID
    invited_by: NotRequired[int]  # Inviter ID
    is_admin: NotRequired['objects.base_bool_int']  # Information whether current user is manager
    is_advertiser: NotRequired['objects.base_bool_int']  # Information whether current user is advertiser
    is_closed: NotRequired['objects.base_bool_int']  # Information whether community is closed
    is_member: NotRequired['objects.base_bool_int']  # Information whether current user is member
    name: NotRequired[str]  # Community name
    photo_100: NotRequired[str]  # URL of square photo of the community with 100 pixels in width
    photo_200: NotRequired[str]  # URL of square photo of the community with 200 pixels in width
    photo_50: NotRequired[str]  # URL of square photo of the community with 50 pixels in width
    screen_name: NotRequired[str]  # Domain of the community page
    type: NotRequired['objects.groups_group_xtr_invited_by_type']

groups_group_xtr_invited_by_admin_level = Literal[
    1,  # moderator
    2,  # editor
    3  # administrator
]

groups_group_xtr_invited_by_type: TypeAlias = Literal['group', 'page', 'event']  # Community type

class groups_groups_array(TypedDict):
    count: int  # Communities number
    items: List[int]

class groups_links_item(TypedDict):
    desc: NotRequired[str]  # Link description
    edit_title: NotRequired['objects.base_bool_int']  # Information whether the link title can be edited
    id: NotRequired[int]  # Link ID
    name: NotRequired[str]  # Link title
    photo_100: NotRequired[str]  # URL of square image of the link with 100 pixels in width
    photo_50: NotRequired[str]  # URL of square image of the link with 50 pixels in width
    url: NotRequired[str]  # Link URL

class groups_live_covers(TypedDict):
    is_enabled: bool  # Information whether live covers is enabled
    is_scalable: NotRequired[bool]  # Information whether live covers photo scaling is enabled
    story_ids: NotRequired[List[str]]

class groups_long_poll_events(TypedDict):
    audio_new: 'objects.base_bool_int'
    board_post_delete: 'objects.base_bool_int'
    board_post_edit: 'objects.base_bool_int'
    board_post_new: 'objects.base_bool_int'
    board_post_restore: 'objects.base_bool_int'
    group_change_photo: 'objects.base_bool_int'
    group_change_settings: 'objects.base_bool_int'
    group_join: 'objects.base_bool_int'
    group_leave: 'objects.base_bool_int'
    group_officers_edit: 'objects.base_bool_int'
    lead_forms_new: NotRequired['objects.base_bool_int']
    market_comment_delete: 'objects.base_bool_int'
    market_comment_edit: 'objects.base_bool_int'
    market_comment_new: 'objects.base_bool_int'
    market_comment_restore: 'objects.base_bool_int'
    message_allow: 'objects.base_bool_int'
    message_deny: 'objects.base_bool_int'
    message_new: 'objects.base_bool_int'
    message_read: 'objects.base_bool_int'
    message_reply: 'objects.base_bool_int'
    message_typing_state: 'objects.base_bool_int'
    message_edit: 'objects.base_bool_int'
    photo_comment_delete: 'objects.base_bool_int'
    photo_comment_edit: 'objects.base_bool_int'
    photo_comment_new: 'objects.base_bool_int'
    photo_comment_restore: 'objects.base_bool_int'
    photo_new: 'objects.base_bool_int'
    poll_vote_new: 'objects.base_bool_int'
    user_block: 'objects.base_bool_int'
    user_unblock: 'objects.base_bool_int'
    video_comment_delete: 'objects.base_bool_int'
    video_comment_edit: 'objects.base_bool_int'
    video_comment_new: 'objects.base_bool_int'
    video_comment_restore: 'objects.base_bool_int'
    video_new: 'objects.base_bool_int'
    wall_post_new: 'objects.base_bool_int'
    wall_reply_delete: 'objects.base_bool_int'
    wall_reply_edit: 'objects.base_bool_int'
    wall_reply_new: 'objects.base_bool_int'
    wall_reply_restore: 'objects.base_bool_int'
    wall_repost: 'objects.base_bool_int'

class groups_long_poll_server(TypedDict):
    key: str  # Long Poll key
    server: str  # Long Poll server address
    ts: str  # Number of the last event

class groups_long_poll_settings(TypedDict):
    api_version: NotRequired[str]  # API version used for the events
    events: 'objects.groups_long_poll_events'
    is_enabled: bool  # Shows whether Long Poll is enabled

class groups_market_info(TypedDict):
    contact_id: NotRequired[int]  # Contact person ID
    currency: NotRequired['objects.market_currency']
    currency_text: NotRequired[str]  # Currency name
    enabled: NotRequired['objects.base_bool_int']  # Information whether the market is enabled
    main_album_id: NotRequired[int]  # Main market album ID
    price_max: NotRequired[str]  # Maximum price
    price_min: NotRequired[str]  # Minimum price

groups_market_state: TypeAlias = Literal['none', 'basic', 'advanced']  # Declares state if market is enabled in group.

class groups_member_role(TypedDict):
    id: NotRequired[int]  # User ID
    permissions: NotRequired[List['objects.groups_member_role_permission']]
    role: NotRequired['objects.groups_member_role_status']

groups_member_role_permission: TypeAlias = Literal['ads']

groups_member_role_status: TypeAlias = Literal['moderator', 'editor', 'administrator', 'creator']  # User's credentials as community admin

class groups_member_status(TypedDict):
    member: 'objects.base_bool_int'  # Information whether user is a member of the group
    user_id: int  # User ID

class groups_member_status_full(TypedDict):
    can_invite: NotRequired['objects.base_bool_int']  # Information whether user can be invited
    can_recall: NotRequired['objects.base_bool_int']  # Information whether user's invite to the group can be recalled
    invitation: NotRequired['objects.base_bool_int']  # Information whether user has been invited to the group
    member: 'objects.base_bool_int'  # Information whether user is a member of the group
    request: NotRequired['objects.base_bool_int']  # Information whether user has send request to the group
    user_id: int  # User ID

class groups_online_status(TypedDict):
    '''Online status of group'''
    minutes: NotRequired[int]  # Estimated time of answer (for status = answer_mark)
    status: 'objects.groups_online_status_type'

groups_online_status_type: TypeAlias = Literal['none', 'online', 'answer_mark']  # Type of online status of group

class groups_owner_xtr_ban_info(TypedDict):
    ban_info: NotRequired['objects.groups_ban_info']
    group: NotRequired['objects.groups_group']  # Information about group if type = group
    profile: NotRequired['objects.users_user']  # Information about group if type = profile
    type: NotRequired['objects.groups_owner_xtr_ban_info_type']

groups_owner_xtr_ban_info_type: TypeAlias = Literal['group', 'profile']  # Owner type

groups_role_options: TypeAlias = Literal['moderator', 'editor', 'administrator', 'creator']  # User's credentials as community admin

class groups_settings_twitter(TypedDict):
    status: Literal['loading', 'sync']
    name: NotRequired[str]

class groups_subject_item(TypedDict):
    id: int  # Subject ID
    name: str  # Subject title

class groups_token_permission_setting(TypedDict):
    name: str
    setting: int

class groups_user_xtr_role(objects.users_user_full):
    role: NotRequired['objects.groups_role_options']

class leads_checked(TypedDict):
    reason: NotRequired[str]  # Reason why user can't start the lead
    result: NotRequired['objects.leads_checked_result']
    sid: NotRequired[str]  # Session ID
    start_link: NotRequired[str]  # URL user should open to start the lead

leads_checked_result: TypeAlias = Literal['true', 'false']  # Information whether user can start the lead

class leads_complete(TypedDict):
    cost: NotRequired[int]  # Offer cost
    limit: NotRequired[int]  # Offer limit
    spent: NotRequired[int]  # Amount of spent votes
    success: NotRequired[int]
    test_mode: NotRequired['objects.base_bool_int']  # Information whether test mode is enabled

class leads_entry(TypedDict):
    aid: NotRequired[int]  # Application ID
    comment: NotRequired[str]  # Comment text
    date: NotRequired[int]  # Date when the action has been started in Unixtime
    sid: NotRequired[str]  # Session string ID
    start_date: NotRequired[int]  # Start date in Unixtime (for status=2)
    status: NotRequired[int]  # Action type
    test_mode: NotRequired['objects.base_bool_int']  # Information whether test mode is enabled
    uid: NotRequired[int]  # User ID

class leads_lead(TypedDict):
    completed: NotRequired[int]  # Completed offers number
    cost: NotRequired[int]  # Offer cost
    days: NotRequired['objects.leads_lead_days']
    impressions: NotRequired[int]  # Impressions number
    limit: NotRequired[int]  # Lead limit
    spent: NotRequired[int]  # Amount of spent votes
    started: NotRequired[int]  # Started offers number

class leads_lead_days(TypedDict):
    completed: NotRequired[int]  # Completed offers number
    impressions: NotRequired[int]  # Impressions number
    spent: NotRequired[int]  # Amount of spent votes
    started: NotRequired[int]  # Started offers number

class leads_start(TypedDict):
    test_mode: NotRequired['objects.base_bool_int']  # Information whether test mode is enabled
    vk_sid: NotRequired[str]  # Session data

likes_type: TypeAlias = Literal['post', 'comment', 'photo', 'audio', 'video', 'note', 'market', 'photo_comment', 'video_comment', 'topic_comment', 'market_comment', 'sitepage']

class link_target_object(TypedDict):
    type: NotRequired[str]  # Object type
    owner_id: NotRequired[int]  # Owner ID
    item_id: NotRequired[int]  # Item ID

class market_currency(TypedDict):
    id: int  # Currency ID
    name: str  # Currency sign

class market_market_album(TypedDict):
    count: int  # Items number
    id: int  # Market album ID
    owner_id: int  # Market album owner's ID
    photo: NotRequired['objects.photos_photo']
    title: str  # Market album title
    updated_time: int  # Date when album has been updated last time in Unixtime

class market_market_category(TypedDict):
    id: int  # Category ID
    name: str  # Category name
    section: 'objects.market_section'

class market_market_item(TypedDict):
    access_key: NotRequired[str]  # Access key for the market item
    availability: 'objects.market_market_item_availability'
    button_title: NotRequired[str]  # Title for button for url
    category: 'objects.market_market_category'
    date: NotRequired[int]  # Date when the item has been created in Unixtime
    description: str  # Item description
    external_id: NotRequired[str]
    id: int  # Item ID
    is_favorite: NotRequired[bool]
    owner_id: int  # Item owner's ID
    price: 'objects.market_price'
    thumb_photo: str  # URL of the preview image
    title: str  # Item title
    url: NotRequired[str]  # URL to item
    variants_grouping_id: NotRequired[int]
    is_main_variant: NotRequired[bool]

market_market_item_availability = Literal[
    0,  # available
    1,  # removed
    2  # unavailable
]

class market_market_item_full(objects.market_market_item):
    albums_ids: NotRequired[List[int]]
    photos: NotRequired[List['objects.photos_photo']]
    can_comment: NotRequired['objects.base_bool_int']  # Information whether current use can comment the item
    can_repost: NotRequired['objects.base_bool_int']  # Information whether current use can repost the item
    likes: NotRequired['objects.base_likes']
    reposts: NotRequired['objects.base_reposts_info']
    views_count: NotRequired[int]  # Views number

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
    tags: NotRequired[List['objects.market_order_tag']]
    dimensions: NotRequired['objects.market_item_dimensions']
    total_price: 'objects.market_price'
    preview_order_items: NotRequired[List['objects.market_order_item']]  # Several order items for preview
    delivery: NotRequired['objects.market_order_delivery']
    recipient: NotRequired['objects.market_order_recipient']
    price_details: NotRequired[List['market_order_details_price']]

class market_order_item(TypedDict):
    owner_id: int
    item_id: int
    price: 'objects.market_price'
    quantity: int
    item: 'objects.market_market_item'
    title: NotRequired[str]
    photo: NotRequired['objects.photos_photo']
    variants: NotRequired[List[str]]

class market_price(TypedDict):
    amount: NotRequired[str]  # Amount
    currency: NotRequired['objects.market_currency']
    discount_rate: NotRequired[int]
    old_amount: NotRequired[str]
    text: NotRequired[str]  # Text

class market_section(TypedDict):
    id: int  # Section ID
    name: str  # Section name

class media_restriction(TypedDict):
    '''Media restrictions'''
    text: NotRequired[str]
    title: str
    button: NotRequired['objects.video_restriction_button']
    always_shown: NotRequired['objects.base_bool_int']  # Need show restriction always or not
    blur: NotRequired['objects.base_bool_int']  # Need blur current video or not
    can_play: NotRequired['objects.base_bool_int']  # Can play video or not
    can_preview: NotRequired['objects.base_bool_int']  # Can preview video or not
    card_icon: NotRequired[List['objects.base_image']]
    list_icon: NotRequired[List['objects.base_image']]

class messages_audio_message(TypedDict):
    access_key: NotRequired[str]  # Access key for audio message
    duration: int  # Audio message duration in seconds
    id: int  # Audio message ID
    link_mp3: str  # MP3 file URL
    link_ogg: str  # OGG file URL
    owner_id: int  # Audio message owner ID
    waveform: List[int]

class messages_chat(TypedDict):
    admin_id: int  # Chat creator ID
    id: int  # Chat ID
    kicked: NotRequired['objects.base_bool_int']  # Shows that user has been kicked from the chat
    left: NotRequired['objects.base_bool_int']  # Shows that user has been left the chat
    photo_100: NotRequired[str]  # URL of the preview image with 100 px in width
    photo_200: NotRequired[str]  # URL of the preview image with 200 px in width
    photo_50: NotRequired[str]  # URL of the preview image with 50 px in width
    push_settings: NotRequired['objects.messages_chat_push_settings']
    title: NotRequired[str]  # Chat title
    type: str  # Chat type
    users: List[int]
    is_default_photo: NotRequired[bool]  # If provided photo is default

class messages_chat_full(TypedDict):
    admin_id: int  # Chat creator ID
    id: int  # Chat ID
    kicked: NotRequired['objects.base_bool_int']  # Shows that user has been kicked from the chat
    left: NotRequired['objects.base_bool_int']  # Shows that user has been left the chat
    photo_100: NotRequired[str]  # URL of the preview image with 100 px in width
    photo_200: NotRequired[str]  # URL of the preview image with 200 px in width
    photo_50: NotRequired[str]  # URL of the preview image with 50 px in width
    push_settings: NotRequired['objects.messages_chat_push_settings']
    title: NotRequired[str]  # Chat title
    type: str  # Chat type
    users: List['objects.messages_user_xtr_invited_by']

class messages_chat_preview(TypedDict):
    admin_id: NotRequired[int]
    joined: NotRequired[bool]
    local_id: NotRequired[int]
    members: NotRequired[List[int]]
    members_count: NotRequired[int]
    title: NotRequired[str]

class messages_chat_push_settings(TypedDict):
    disabled_until: NotRequired[int]  # Time until that notifications are disabled
    sound: NotRequired['objects.base_bool_int']  # Information whether the sound is on

class messages_chat_restrictions(TypedDict):
    admins_promote_users: NotRequired[bool]  # Only admins can promote users to admins
    only_admins_edit_info: NotRequired[bool]  # Only admins can change chat info
    only_admins_edit_pin: NotRequired[bool]  # Only admins can edit pinned message
    only_admins_invite: NotRequired[bool]  # Only admins can invite users to this chat
    only_admins_kick: NotRequired[bool]  # Only admins can kick users from this chat

class messages_conversation(TypedDict):
    peer: 'objects.messages_conversation_peer'
    last_message_id: int  # ID of the last message in conversation
    in_read: int  # Last message user have read
    out_read: int  # Last outcoming message have been read by the opponent
    unread_count: NotRequired[int]  # Unread messages number
    is_marked_unread: NotRequired[bool]  # Is this conversation uread
    important: NotRequired[bool]
    unanswered: NotRequired[bool]
    special_service_type: NotRequired[Literal['business_notify']]
    message_request_data: NotRequired['objects.messages_message_request_data']
    mentions: NotRequired[List[int]]  # Ids of messages with mentions
    current_keyboard: NotRequired['objects.messages_keyboard']

class messages_conversation_member(TypedDict):
    can_kick: NotRequired[bool]  # Is it possible for user to kick this member
    invited_by: NotRequired[int]
    is_admin: NotRequired[bool]
    is_owner: NotRequired[bool]
    is_message_request: NotRequired[bool]
    join_date: NotRequired[int]
    request_date: NotRequired[int]  # Message request date
    member_id: int

class messages_conversation_peer(TypedDict):
    id: int
    local_id: NotRequired[int]
    type: 'objects.messages_conversation_peer_type'

messages_conversation_peer_type: TypeAlias = Literal['chat', 'email', 'user', 'group']  # Peer type

class messages_conversation_with_message(TypedDict):
    conversation: NotRequired['objects.messages_conversation']
    last_message: NotRequired['objects.messages_message']

class messages_foreign_message(TypedDict):
    attachments: NotRequired[List['objects.messages_message_attachment']]
    conversation_message_id: NotRequired[int]  # Conversation message ID
    date: int  # Date when the message was created
    from_id: int  # Message author's ID
    fwd_messages: NotRequired[List['objects.messages_foreign_message']]
    geo: NotRequired['objects.base_geo']
    id: NotRequired[int]  # Message ID
    peer_id: NotRequired[int]  # Peer ID
    reply_message: NotRequired['objects.messages_foreign_message']
    text: str  # Message text
    update_time: NotRequired[int]  # Date when the message has been updated in Unixtime
    was_listened: NotRequired[bool]  # Was the audio message inside already listened by you
    payload: NotRequired[str]  # Additional data sent along with message for developer convenience

class messages_graffiti(TypedDict):
    access_key: NotRequired[str]  # Access key for graffiti
    height: int  # Graffiti height
    id: int  # Graffiti ID
    owner_id: int  # Graffiti owner ID
    url: str  # Graffiti URL
    width: int  # Graffiti width

class messages_history_attachment(TypedDict):
    attachment: 'objects.messages_history_message_attachment'
    message_id: int  # Message ID
    from_id: int  # Message author's ID

class messages_history_message_attachment(TypedDict):
    audio: NotRequired['objects.audio_audio']
    audio_message: NotRequired['objects.messages_audio_message']
    doc: NotRequired['objects.docs_doc']
    graffiti: NotRequired['objects.messages_graffiti']
    link: NotRequired['objects.base_link']
    market: NotRequired['objects.base_link']
    photo: NotRequired['objects.photos_photo']
    share: NotRequired['objects.base_link']
    type: 'objects.messages_history_message_attachment_type'
    video: NotRequired['objects.video_video']
    wall: NotRequired['objects.base_link']

messages_history_message_attachment_type: TypeAlias = Literal['photo', 'video', 'audio', 'doc', 'link', 'market', 'wall', 'share', 'graffiti', 'audio_message']  # Attachments type

class messages_keyboard(TypedDict):
    author_id: NotRequired[int]  # Community or bot, which set this keyboard
    buttons: 'objects.messages_keyboard_button'
    one_time: bool  # Should this keyboard disappear on first use
    inline: NotRequired[bool]

class messages_keyboard_button(TypedDict):
    action: 'objects.messages_keyboard_button_action'
    color: NotRequired[Literal['default', 'positive', 'negative', 'primary']]  # Button color

class messages_keyboard_button_action(TypedDict):
    '''Description of the action, that should be performed on button click'''
    app_id: NotRequired[int]  # Fragment value in app link like vk.com/app{app_id}_-654321#hash
    hash: NotRequired[str]  # Fragment value in app link like vk.com/app123456_-654321#{hash}
    label: NotRequired[str]  # Label for button
    link: NotRequired[str]  # link for button
    owner_id: NotRequired[int]  # Fragment value in app link like vk.com/app123456_{owner_id}#hash
    payload: NotRequired[str]  # Additional data sent along with message for developer convenience
    type: 'objects.messages_template_action_type_names'  # Button type

class messages_last_activity(TypedDict):
    online: 'objects.base_bool_int'  # Information whether user is online
    time: int  # Time when user was online in Unixtime

class messages_longpoll_messages(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.messages_message']]

class messages_longpoll_params(TypedDict):
    key: NotRequired[str]  # Key
    pts: NotRequired[int]  # Persistent timestamp
    server: NotRequired[str]  # Server URL
    ts: NotRequired[str]  # Timestamp

class messages_message(TypedDict):
    action: NotRequired['objects.messages_message_action']
    admin_author_id: NotRequired[int]  # Only for messages from community. Contains user ID of community admin, who sent this message.
    attachments: NotRequired[List['objects.messages_message_attachment']]
    conversation_message_id: NotRequired[int]  # Unique auto-incremented number for all messages with this peer
    date: int  # Date when the message has been sent in Unixtime
    deleted: NotRequired['objects.base_bool_int']  # Is it an deleted message
    from_id: int  # Message author's ID
    fwd_messages: NotRequired[List['objects.messages_foreign_message']]  # Forwarded messages
    geo: NotRequired['objects.base_geo']
    id: int  # Message ID
    important: NotRequired[bool]  # Is it an important message
    is_hidden: NotRequired[bool]
    is_cropped: NotRequired[bool]  # this message is cropped for bot
    keyboard: NotRequired['objects.messages_keyboard']
    members_count: NotRequired[int]  # Members number
    out: 'objects.base_bool_int'  # Information whether the message is outcoming
    payload: NotRequired[str]
    peer_id: int  # Peer ID
    random_id: NotRequired[int]  # ID used for sending messages. It returned only for outgoing messages
    ref: NotRequired[str]
    ref_source: NotRequired[str]
    reply_message: NotRequired['objects.messages_foreign_message']
    text: str  # Message text
    update_time: NotRequired[int]  # Date when the message has been updated in Unixtime
    was_listened: NotRequired[bool]  # Was the audio message inside already listened by you
    pinned_at: NotRequired[int]  # Date when the message has been pinned in Unixtime

class messages_message_action(TypedDict):
    conversation_message_id: NotRequired[int]  # Message ID
    email: NotRequired[str]  # Email address for chat_invite_user or chat_kick_user actions
    member_id: NotRequired[int]  # User or email peer ID
    message: NotRequired[str]  # Message body of related message
    photo: NotRequired['objects.messages_message_action_photo']
    text: NotRequired[str]  # New chat title for chat_create and chat_title_update actions
    type: 'objects.messages_message_action_status'

class messages_message_action_photo(TypedDict):
    photo_100: str  # URL of the preview image with 100px in width
    photo_200: str  # URL of the preview image with 200px in width
    photo_50: str  # URL of the preview image with 50px in width

messages_message_action_status: TypeAlias = Literal['chat_photo_update', 'chat_photo_remove', 'chat_create', 'chat_title_update', 'chat_invite_user', 'chat_kick_user', 'chat_pin_message', 'chat_unpin_message', 'chat_invite_user_by_link']  # Action status

class messages_message_attachment(TypedDict):
    audio: NotRequired['objects.audio_audio']
    audio_message: NotRequired['objects.messages_audio_message']
    doc: NotRequired['objects.docs_doc']
    gift: NotRequired['objects.gifts_layout']
    graffiti: NotRequired['objects.messages_graffiti']
    link: NotRequired['objects.base_link']
    market: NotRequired['objects.market_market_item']
    market_market_album: NotRequired['objects.market_market_album']
    photo: NotRequired['objects.photos_photo']
    sticker: NotRequired['objects.base_sticker']
    story: NotRequired['objects.stories_story']
    type: 'objects.messages_message_attachment_type'
    video: NotRequired['objects.video_video']
    wall: NotRequired['objects.wall_wallpost_full']
    wall_reply: NotRequired['objects.wall_wall_comment']

messages_message_attachment_type: TypeAlias = Literal['photo', 'audio', 'video', 'doc', 'link', 'market', 'market_album', 'gift', 'sticker', 'wall', 'wall_reply', 'article', 'graffiti', 'audio_message']  # Attachment type

class messages_message_request_data(TypedDict):
    status: NotRequired[str]  # Status of message request
    inviter_id: NotRequired[int]  # Message request sender id
    request_date: NotRequired[int]  # Message request date

class messages_messages_array(TypedDict):
    count: NotRequired[int]
    items: NotRequired[List['objects.messages_message']]

class messages_pinned_message(TypedDict):
    attachments: NotRequired[List['objects.messages_message_attachment']]
    conversation_message_id: NotRequired[int]  # Unique auto-incremented number for all messages with this peer
    date: int  # Date when the message has been sent in Unixtime
    from_id: int  # Message author's ID
    fwd_messages: NotRequired[List['objects.messages_foreign_message']]  # Forwarded messages
    geo: NotRequired['objects.base_geo']
    id: int  # Message ID
    peer_id: int  # Peer ID
    reply_message: NotRequired['objects.messages_foreign_message']
    text: str  # Message text
    keyboard: NotRequired['objects.messages_keyboard']

messages_template_action_type_names: TypeAlias = Literal['text', 'start', 'location', 'vkpay', 'open_app', 'open_photo', 'open_link']  # Template action type names

class messages_user_xtr_invited_by(objects.users_user_xtr_type):
    invited_by: NotRequired[int]  # ID of the inviter

newsfeed_comments_filters: TypeAlias = Literal['post', 'photo', 'video', 'topic', 'note']

class newsfeed_event_activity(TypedDict):
    address: NotRequired[str]  # address of event
    button_text: str  # text of attach
    friends: List[int]  # array of friends ids
    member_status: 'objects.groups_group_full_member_status'  # Current user's member status
    text: str  # text of attach
    time: NotRequired[int]  # event start time

newsfeed_filters: TypeAlias = Literal['post', 'photo', 'photo_tag', 'wall_photo', 'friend', 'recommended_groups', 'note', 'audio', 'video', 'audio_playlist', 'games_carousel', 'clip']

newsfeed_ignore_item_type = Literal[
    'wall',  # post on the wall
    'tag',  # tag on a photo
    'profilephoto',  # profile photo
    'video',  # video
    'photo',  # photo
    'audio'  # audio
]

class newsfeed_item_audio(objects.newsfeed_item_base):
    audio: NotRequired['objects.newsfeed_item_audio_audio']
    post_id: NotRequired[int]  # Post ID

class newsfeed_item_audio_audio(TypedDict):
    count: NotRequired[int]  # Audios number
    items: NotRequired[List['objects.audio_audio']]

class newsfeed_item_base(TypedDict):
    type: 'objects.newsfeed_newsfeed_item_type'
    source_id: int  # Item source ID
    date: int  # Date when item has been added in Unixtime

class newsfeed_item_digest(objects.newsfeed_item_base):
    button_text: NotRequired[str]
    feed_id: NotRequired[str]  # id of feed in digest
    items: NotRequired[List['objects.wall_wallpost']]
    main_post_ids: NotRequired[List[str]]
    template: NotRequired[Literal['list', 'grid']]  # type of digest
    title: NotRequired[str]
    track_code: NotRequired[str]

class newsfeed_item_friend(objects.newsfeed_item_base):
    friends: NotRequired['objects.newsfeed_item_friend_friends']

class newsfeed_item_friend_friends(TypedDict):
    count: NotRequired[int]  # Number of friends has been added
    items: NotRequired[List['objects.base_user_id']]

class newsfeed_item_holiday_recommendations_block_header(TypedDict):
    title: NotRequired[str]  # Title of the header
    subtitle: NotRequired[str]  # Subtitle of the header
    image: NotRequired[List['objects.base_image']]
    action: NotRequired['objects.base_link_button_action']

class newsfeed_item_photo(objects.wall_carousel_base, objects.newsfeed_item_base):
    photos: NotRequired['objects.newsfeed_item_photo_photos']
    post_id: NotRequired[int]  # Post ID

class newsfeed_item_photo_photos(TypedDict):
    count: NotRequired[int]  # Photos number
    items: NotRequired[List['objects.newsfeed_newsfeed_photo']]

class newsfeed_item_photo_tag(objects.wall_carousel_base, objects.newsfeed_item_base):
    photo_tags: NotRequired['objects.newsfeed_item_photo_tag_photo_tags']
    post_id: NotRequired[int]  # Post ID

class newsfeed_item_photo_tag_photo_tags(TypedDict):
    count: NotRequired[int]  # Tags number
    items: NotRequired[List['objects.newsfeed_newsfeed_photo']]

class newsfeed_item_promo_button(objects.newsfeed_item_base):
    text: NotRequired[str]
    title: NotRequired[str]
    action: NotRequired['objects.newsfeed_item_promo_button_action']
    images: NotRequired[List['objects.newsfeed_item_promo_button_image']]
    track_code: NotRequired[str]

class newsfeed_item_promo_button_action(TypedDict):
    url: NotRequired[str]
    type: NotRequired[str]
    target: NotRequired[str]

class newsfeed_item_promo_button_image(TypedDict):
    width: NotRequired[int]
    height: NotRequired[int]
    url: NotRequired[str]

class newsfeed_item_topic(objects.newsfeed_item_base):
    comments: NotRequired['objects.base_comments_info']
    likes: NotRequired['objects.base_likes_info']
    post_id: NotRequired[int]  # Topic post ID
    text: NotRequired[str]  # Post text

class newsfeed_item_video(objects.wall_carousel_base, objects.newsfeed_item_base):
    video: NotRequired['objects.newsfeed_item_video_video']

class newsfeed_item_video_video(TypedDict):
    count: NotRequired[int]  # Tags number
    items: NotRequired[List['objects.video_video']]

class newsfeed_item_wallpost(objects.wall_carousel_base, objects.newsfeed_item_base):
    activity: NotRequired['objects.newsfeed_event_activity']
    attachments: NotRequired[List['objects.wall_wallpost_attachment']]
    comments: NotRequired['objects.base_comments_info']
    copy_history: NotRequired[List['objects.wall_wallpost']]
    feedback: NotRequired['objects.newsfeed_item_wallpost_feedback']
    geo: NotRequired['objects.base_geo']
    is_favorite: NotRequired[bool]  # Information whether the post in favorites list
    likes: NotRequired['objects.base_likes_info']
    marked_as_ads: NotRequired['objects.base_bool_int']  # Information whether the post is marked as ads
    post_id: NotRequired[int]  # Post ID
    post_source: NotRequired['objects.wall_post_source']
    post_type: NotRequired['objects.newsfeed_item_wallpost_type']
    reposts: NotRequired['objects.base_reposts_info']
    signer_id: NotRequired[int]  # Post signer ID
    text: NotRequired[str]  # Post text
    views: NotRequired['objects.wall_views']  # Count of views
    short_text_rate: NotRequired[float]  # Preview length control parameter

class newsfeed_item_wallpost_feedback(TypedDict):
    type: 'objects.newsfeed_item_wallpost_feedback_type'
    question: str
    answers: NotRequired[List['objects.newsfeed_item_wallpost_feedback_answer']]
    stars_count: NotRequired[int]
    gratitude: NotRequired[str]

class newsfeed_item_wallpost_feedback_answer(TypedDict):
    title: str
    id: str

newsfeed_item_wallpost_feedback_type: TypeAlias = Literal['buttons', 'stars']

newsfeed_item_wallpost_type: TypeAlias = Literal['post', 'copy', 'reply']  # Post type

class newsfeed_list(TypedDict):
    id: int  # List ID
    title: str  # List title

class newsfeed_list_full(objects.newsfeed_list):
    no_reposts: NotRequired['objects.base_bool_int']  # Information whether reposts hiding is enabled
    source_ids: NotRequired[List[int]]

newsfeed_newsfeed_item: TypeAlias = Union['objects.newsfeed_item_wallpost', 'objects.newsfeed_item_photo', 'objects.newsfeed_item_photo_tag', 'objects.newsfeed_item_friend', 'objects.newsfeed_item_audio', 'objects.newsfeed_item_video', 'objects.newsfeed_item_topic', 'objects.newsfeed_item_digest', 'objects.newsfeed_item_promo_button']

newsfeed_newsfeed_item_type: TypeAlias = Literal['post', 'photo', 'photo_tag', 'wall_photo', 'friend', 'note', 'audio', 'video', 'topic', 'digest', 'stories', 'tags_suggestions']  # Item type

class newsfeed_newsfeed_photo(objects.photos_photo):
    likes: NotRequired['objects.base_likes']
    comments: NotRequired['objects.base_object_count']
    can_repost: NotRequired['objects.base_bool_int']  # Information whether current user can repost the photo

class notes_note(TypedDict):
    read_comments: NotRequired[int]
    can_comment: NotRequired['objects.base_bool_int']  # Information whether current user can comment the note
    comments: int  # Comments number
    date: int  # Date when the note has been created in Unixtime
    id: int  # Note ID
    owner_id: int  # Note owner's ID
    text: NotRequired[str]  # Note text
    text_wiki: NotRequired[str]  # Note text in wiki format
    title: str  # Note title
    view_url: str  # URL of the page with note preview

class notes_note_comment(TypedDict):
    date: int  # Date when the comment has beed added in Unixtime
    id: int  # Comment ID
    message: str  # Comment text
    nid: int  # Note ID
    oid: int  # Note ID
    reply_to: NotRequired[int]  # ID of replied comment
    uid: int  # Comment author's ID

class notifications_feedback(TypedDict):
    attachments: NotRequired[List['objects.wall_wallpost_attachment']]
    from_id: NotRequired[int]  # Reply author's ID
    geo: NotRequired['objects.base_geo']
    id: NotRequired[int]  # Item ID
    likes: NotRequired['objects.base_likes_info']
    text: NotRequired[str]  # Reply text
    to_id: NotRequired[int]  # Wall owner's ID

class notifications_notification(TypedDict):
    date: NotRequired[int]  # Date when the event has been occurred
    feedback: NotRequired['objects.notifications_feedback']
    parent: NotRequired['objects.notifications_notification_parent']
    reply: NotRequired['objects.notifications_reply']
    type: NotRequired[str]  # Notification type

notifications_notification_item: TypeAlias = Dict[str, Any]

class notifications_notification_parent(objects.wall_wallpost_to_id, objects.photos_photo, objects.board_topic, objects.video_video, objects.notifications_notifications_comment): ...

class notifications_notifications_comment(TypedDict):
    date: NotRequired[int]  # Date when the comment has been added in Unixtime
    id: NotRequired[int]  # Comment ID
    owner_id: NotRequired[int]  # Author ID
    photo: NotRequired['objects.photos_photo']
    post: NotRequired['objects.wall_wallpost']
    text: NotRequired[str]  # Comment text
    topic: NotRequired['objects.board_topic']
    video: NotRequired['objects.video_video']

class notifications_reply(TypedDict):
    date: NotRequired[int]  # Date when the reply has been created in Unixtime
    id: NotRequired[int]  # Reply ID
    text: NotRequired[int]  # Reply text

class notifications_send_message_error(TypedDict):
    code: NotRequired[Literal[1, 2, 3, 4]]  # Error code
    description: NotRequired[str]  # Error description

class notifications_send_message_item(TypedDict):
    user_id: NotRequired[int]  # User ID
    status: NotRequired[bool]  # Notification status
    error: NotRequired['objects.notifications_send_message_error']

class oauth_error(TypedDict):
    error: str  # Error type
    error_description: str  # Error description
    redirect_uri: NotRequired[str]  # URI for validation

class orders_amount(TypedDict):
    amounts: NotRequired[List['objects.orders_amount_item']]
    currency: NotRequired[str]  # Currency name

class orders_amount_item(TypedDict):
    amount: NotRequired[int]  # Votes amount in user's currency
    description: NotRequired[str]  # Amount description
    votes: NotRequired[str]  # Votes number

class orders_order(TypedDict):
    amount: NotRequired[int]  # Amount
    app_order_id: NotRequired[int]  # App order ID
    cancel_transaction_id: NotRequired[int]  # Cancel transaction ID
    date: NotRequired[int]  # Date of creation in Unixtime
    id: NotRequired[int]  # Order ID
    item: NotRequired[str]  # Order item
    receiver_id: NotRequired[int]  # Receiver ID
    status: NotRequired[str]  # Order status
    transaction_id: NotRequired[int]  # Transaction ID
    user_id: NotRequired[int]  # User ID

class orders_subscription(TypedDict):
    cancel_reason: NotRequired[str]  # Cancel reason
    create_time: int  # Date of creation in Unixtime
    id: int  # Subscription ID
    item_id: str  # Subscription order item
    next_bill_time: NotRequired[int]  # Date of next bill in Unixtime
    pending_cancel: NotRequired[bool]  # Pending cancel state
    period: int  # Subscription period
    period_start_time: int  # Date of last period start in Unixtime
    price: int  # Subscription price
    status: str  # Subscription status
    test_mode: NotRequired[bool]  # Is test subscription
    trial_expire_time: NotRequired[int]  # Date of trial expire in Unixtime
    update_time: int  # Date of last change in Unixtime

class owner_state(TypedDict):
    state: NotRequired[Literal[1, 2, 3, 4]]
    description: NotRequired[str]  # wiki text to describe user state

pages_privacy_settings = Literal[
    0,  # community managers only
    1,  # community members only
    2  # everyone
]

class pages_wikipage(TypedDict):
    creator_id: NotRequired[int]  # Page creator ID
    creator_name: NotRequired[int]  # Page creator name
    editor_id: NotRequired[int]  # Last editor ID
    editor_name: NotRequired[str]  # Last editor name
    group_id: int  # Community ID
    id: int  # Page ID
    title: str  # Page title
    views: int  # Views number
    who_can_edit: 'objects.pages_privacy_settings'  # Edit settings of the page
    who_can_view: 'objects.pages_privacy_settings'  # View settings of the page

class pages_wikipage_full(TypedDict):
    created: int  # Date when the page has been created in Unixtime
    creator_id: NotRequired[int]  # Page creator ID
    current_user_can_edit: NotRequired['objects.base_bool_int']  # Information whether current user can edit the page
    current_user_can_edit_access: NotRequired['objects.base_bool_int']  # Information whether current user can edit the page access settings
    edited: int  # Date when the page has been edited in Unixtime
    editor_id: NotRequired[int]  # Last editor ID
    group_id: int  # Community ID
    html: NotRequired[str]  # Page content, HTML
    id: int  # Page ID
    source: NotRequired[str]  # Page content, wiki
    title: str  # Page title
    view_url: str  # URL of the page preview
    views: int  # Views number
    who_can_edit: 'objects.pages_privacy_settings'  # Edit settings of the page
    who_can_view: 'objects.pages_privacy_settings'  # View settings of the page

class pages_wikipage_history(TypedDict):
    id: int  # Version ID
    length: int  # Page size in bytes
    date: int  # Date when the page has been edited in Unixtime
    editor_id: int  # Last editor ID
    editor_name: str  # Last editor name

class photos_comment_xtr_pid(TypedDict):
    attachments: NotRequired[List['objects.wall_comment_attachment']]
    date: int  # Date when the comment has been added in Unixtime
    from_id: int  # Author ID
    id: int  # Comment ID
    likes: NotRequired['objects.base_likes_info']
    pid: int  # Photo ID
    reply_to_comment: NotRequired[int]  # Replied comment ID
    reply_to_user: NotRequired[int]  # Replied user ID
    text: str  # Comment text
    parents_stack: NotRequired[List[int]]
    thread: NotRequired['objects.comment_thread']

class photos_image(TypedDict):
    height: NotRequired[int]  # Height of the photo in px.
    type: NotRequired['objects.photos_image_type']
    url: NotRequired[str]  # Photo URL.
    width: NotRequired[int]  # Width of the photo in px.

photos_image_type: TypeAlias = Literal['s', 'm', 'x', 'l', 'o', 'p', 'q', 'r', 'y', 'z', 'w']  # Photo's type.

class photos_market_album_upload_response(TypedDict):
    gid: NotRequired[int]  # Community ID
    hash: NotRequired[str]  # Uploading hash
    photo: NotRequired[str]  # Uploaded photo data
    server: NotRequired[int]  # Upload server number

class photos_market_upload_response(TypedDict):
    crop_data: NotRequired[str]  # Crop data
    crop_hash: NotRequired[str]  # Crop hash
    group_id: NotRequired[int]  # Community ID
    hash: NotRequired[str]  # Uploading hash
    photo: NotRequired[str]  # Uploaded photo data
    server: NotRequired[int]  # Upload server number

class photos_message_upload_response(TypedDict):
    hash: NotRequired[str]  # Uploading hash
    photo: NotRequired[str]  # Uploaded photo data
    server: NotRequired[int]  # Upload server number

class photos_owner_upload_response(TypedDict):
    hash: NotRequired[str]  # Uploading hash
    photo: NotRequired[str]  # Uploaded photo data
    server: NotRequired[int]  # Upload server number

class photos_photo(TypedDict):
    access_key: NotRequired[str]  # Access key for the photo
    album_id: int  # Album ID
    date: int  # Date when uploaded
    height: NotRequired[int]  # Original photo height
    id: int  # Photo ID
    images: NotRequired[List['objects.photos_image']]
    lat: NotRequired[float]  # Latitude
    long: NotRequired[float]  # Longitude
    owner_id: int  # Photo owner's ID
    photo_256: NotRequired[str]  # URL of image with 2560 px width
    can_comment: NotRequired['objects.base_bool_int']  # Information whether current user can comment the photo
    place: NotRequired[str]
    post_id: NotRequired[int]  # Post ID
    sizes: NotRequired[List['objects.photos_photo_sizes']]
    text: NotRequired[str]  # Photo caption
    user_id: NotRequired[int]  # ID of the user who have uploaded the photo
    width: NotRequired[int]  # Original photo width
    has_tags: bool  # Whether photo has attached tag links
    restrictions: NotRequired['objects.media_restriction']

class photos_photo_album(TypedDict):
    created: int  # Date when the album has been created in Unixtime
    description: NotRequired[str]  # Photo album description
    id: int  # Photo album ID
    owner_id: int  # Album owner's ID
    size: int  # Photos number
    thumb: NotRequired['objects.photos_photo']
    title: str  # Photo album title
    updated: int  # Date when the album has been updated last time in Unixtime

class photos_photo_album_full(TypedDict):
    can_upload: NotRequired['objects.base_bool_int']  # Information whether current user can upload photo to the album
    comments_disabled: NotRequired['objects.base_bool_int']  # Information whether album comments are disabled
    created: int  # Date when the album has been created in Unixtime
    description: NotRequired[str]  # Photo album description
    id: int  # Photo album ID
    owner_id: int  # Album owner's ID
    size: int  # Photos number
    sizes: NotRequired[List['objects.photos_photo_sizes']]
    thumb_id: NotRequired[int]  # Thumb photo ID
    thumb_is_last: NotRequired['objects.base_bool_int']  # Information whether the album thumb is last photo
    thumb_src: NotRequired[str]  # URL of the thumb image
    title: str  # Photo album title
    updated: int  # Date when the album has been updated last time in Unixtime
    upload_by_admins_only: NotRequired['objects.base_bool_int']  # Information whether only community administrators can upload photos

class photos_photo_full(TypedDict):
    access_key: NotRequired[str]  # Access key for the photo
    album_id: int  # Album ID
    can_comment: NotRequired['objects.base_bool_int']  # Information whether current user can comment the photo
    comments: NotRequired['objects.base_object_count']
    date: int  # Date when uploaded
    height: NotRequired[int]  # Original photo height
    id: int  # Photo ID
    images: NotRequired[List['objects.photos_image']]
    lat: NotRequired[float]  # Latitude
    likes: NotRequired['objects.base_likes']
    long: NotRequired[float]  # Longitude
    owner_id: int  # Photo owner's ID
    post_id: NotRequired[int]  # Post ID
    reposts: NotRequired['objects.base_object_count']
    tags: NotRequired['objects.base_object_count']
    text: NotRequired[str]  # Photo caption
    user_id: NotRequired[int]  # ID of the user who have uploaded the photo
    width: NotRequired[int]  # Original photo width

class photos_photo_full_xtr_real_offset(TypedDict):
    access_key: NotRequired[str]  # Access key for the photo
    album_id: int  # Album ID
    can_comment: NotRequired['objects.base_bool_int']
    comments: NotRequired['objects.base_object_count']
    date: int  # Date when uploaded
    height: NotRequired[int]  # Original photo height
    hidden: NotRequired['objects.base_property_exists']  # Returns if the photo is hidden above the wall
    id: int  # Photo ID
    lat: NotRequired[float]  # Latitude
    likes: NotRequired['objects.base_likes']
    long: NotRequired[float]  # Longitude
    owner_id: int  # Photo owner's ID
    photo_1280: NotRequired[str]  # URL of image with 1280 px width
    photo_130: NotRequired[str]  # URL of image with 130 px width
    photo_2560: NotRequired[str]  # URL of image with 2560 px width
    photo_604: NotRequired[str]  # URL of image with 604 px width
    photo_75: NotRequired[str]  # URL of image with 75 px width
    photo_807: NotRequired[str]  # URL of image with 807 px width
    post_id: NotRequired[int]  # Post ID
    real_offset: NotRequired[int]  # Real position of the photo
    reposts: NotRequired['objects.base_object_count']
    sizes: NotRequired[List['objects.photos_photo_sizes']]
    tags: NotRequired['objects.base_object_count']
    text: NotRequired[str]  # Photo caption
    user_id: NotRequired[int]  # ID of the user who have uploaded the photo
    width: NotRequired[int]  # Original photo width

class photos_photo_sizes(TypedDict):
    height: int  # Height in px
    url: str  # URL of the image
    src: NotRequired[str]  # URL of the image
    type: 'objects.photos_photo_sizes_type'
    width: int  # Width in px

photos_photo_sizes_type: TypeAlias = Literal['s', 'm', 'x', 'o', 'p', 'q', 'r', 'k', 'l', 'y', 'z', 'c', 'w']  # Size type

class photos_photo_tag(TypedDict):
    date: int  # Date when tag has been added in Unixtime
    id: int  # Tag ID
    placer_id: int  # ID of the tag creator
    tagged_name: str  # Tag description
    description: NotRequired[str]  # Tagged description.
    user_id: int  # Tagged user ID
    viewed: 'objects.base_bool_int'  # Information whether the tag is reviewed
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

class photos_photo_upload_response(TypedDict):
    aid: NotRequired[int]  # Album ID
    hash: NotRequired[str]  # Uploading hash
    photos_list: NotRequired[str]  # Uploaded photos data
    server: NotRequired[int]  # Upload server number

class photos_photo_xtr_real_offset(TypedDict):
    access_key: NotRequired[str]  # Access key for the photo
    album_id: int  # Album ID
    date: int  # Date when uploaded
    height: NotRequired[int]  # Original photo height
    hidden: NotRequired['objects.base_property_exists']  # Returns if the photo is hidden above the wall
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
    post_id: NotRequired[int]  # Post ID
    real_offset: NotRequired[int]  # Real position of the photo
    sizes: NotRequired[List['objects.photos_photo_sizes']]
    text: NotRequired[str]  # Photo caption
    user_id: NotRequired[int]  # ID of the user who have uploaded the photo
    width: NotRequired[int]  # Original photo width

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
    sizes: NotRequired[List['objects.photos_photo_sizes']]
    tag_created: NotRequired[int]  # Date when tag has been added in Unixtime
    tag_id: NotRequired[int]  # Tag ID
    text: NotRequired[str]  # Photo caption
    user_id: NotRequired[int]  # ID of the user who have uploaded the photo
    width: NotRequired[int]  # Original photo width

class photos_tags_suggestion_item(TypedDict):
    title: NotRequired[str]
    caption: NotRequired[str]
    type: NotRequired[str]
    buttons: NotRequired[List['objects.photos_tags_suggestion_item_button']]
    photo: NotRequired['objects.photos_photo']
    tags: NotRequired[List['objects.photos_photo_tag']]
    track_code: NotRequired[str]

class photos_tags_suggestion_item_button(TypedDict):
    title: NotRequired[str]
    action: NotRequired[Literal['confirm', 'decline', 'show_tags']]
    style: NotRequired[Literal['primary', 'secondary']]

class photos_wall_upload_response(TypedDict):
    hash: NotRequired[str]  # Uploading hash
    photo: NotRequired[str]  # Uploaded photo data
    server: NotRequired[int]  # Upload server number

class podcast_podcast(TypedDict):
    owner_id: int  # ID of the podcast's owner
    podcast_title: str  # Podcast title

class podcast_popular_podcast(TypedDict):
    owner_id: NotRequired[int]
    owner_title: NotRequired[str]
    url: NotRequired[str]

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
    images: NotRequired[List['objects.base_image']]  # Pattern tiles
    points: NotRequired[List['objects.base_gradient_point']]  # Gradient points
    type: NotRequired[Literal['gradient', 'tile']]
    width: NotRequired[int]  # Original with of pattern tile

class polls_friend(TypedDict):
    id: int

class polls_poll(TypedDict):
    anonymous: 'objects.polls_poll_anonymous'
    friends: NotRequired[List['objects.polls_friend']]
    multiple: bool  # Information whether the poll with multiple choices
    answer_id: NotRequired[int]  # Current user's answer ID
    end_date: int
    answer_ids: NotRequired[List[int]]  # Current user's answer IDs
    closed: bool
    is_board: bool
    can_edit: bool
    can_vote: bool
    can_report: bool
    can_share: bool
    photo: NotRequired['objects.polls_background']
    answers: List['objects.polls_answer']
    created: int  # Date when poll has been created in Unixtime
    id: int  # Poll ID
    owner_id: int  # Poll owner's ID
    author_id: NotRequired[int]  # Poll author's ID
    question: str  # Poll question
    background: NotRequired['objects.polls_background']
    votes: int  # Votes number
    disable_unvote: bool

polls_poll_anonymous: TypeAlias = bool  # Information whether the field is anonymous

class polls_voters(TypedDict):
    answer_id: NotRequired[int]  # Answer ID
    users: NotRequired['objects.polls_voters_users']

class polls_voters_users(TypedDict):
    count: NotRequired[int]  # Votes number
    items: NotRequired[List[int]]

class prettyCards_prettyCard(TypedDict):
    button: NotRequired[str]  # Button key
    button_text: NotRequired[str]  # Button text in current language
    card_id: str  # Card ID (long int returned as string)
    images: NotRequired[List['objects.base_image']]
    link_url: str  # Link URL
    photo: str  # Photo ID (format "<owner_id>_<media_id>")
    price: NotRequired[str]  # Price if set (decimal number returned as string)
    price_old: NotRequired[str]  # Old price if set (decimal number returned as string)
    title: str  # Title

class search_hint(TypedDict):
    app: NotRequired['objects.apps_app']
    description: str  # Object description
    # global: NotRequired['objects.base_bool_int']  # Information whether the object has been found globally
    group: NotRequired['objects.groups_group']
    profile: NotRequired['objects.users_user_min']
    section: 'objects.search_hint_section'
    type: 'objects.search_hint_type'

search_hint_section: TypeAlias = Literal['groups', 'events', 'publics', 'correspondents', 'people', 'friends', 'mutual_friends']  # Section title

search_hint_type: TypeAlias = Literal['group', 'profile', 'vk_app', 'app', 'html5_game']  # Object type

class secure_level(TypedDict):
    level: NotRequired[int]  # Level
    uid: NotRequired[int]  # User ID

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
    activity: NotRequired['objects.stats_activity']
    period_from: NotRequired[int]  # Unix timestamp
    period_to: NotRequired[int]  # Unix timestamp
    reach: NotRequired['objects.stats_reach']
    visitors: NotRequired['objects.stats_views']

class stats_reach(TypedDict):
    '''Reach stats'''
    age: NotRequired[List['objects.stats_sex_age']]
    cities: NotRequired[List['objects.stats_city']]
    countries: NotRequired[List['objects.stats_country']]
    mobile_reach: NotRequired[int]  # Reach count from mobile devices
    reach: NotRequired[int]  # Reach count
    reach_subscribers: NotRequired[int]  # Subscribers reach count
    sex: NotRequired[List['objects.stats_sex_age']]
    sex_age: NotRequired[List['objects.stats_sex_age']]

class stats_sex_age(TypedDict):
    count: NotRequired[int]  # Visitors number
    value: str  # Sex/age value
    reach: NotRequired[int]
    reach_subscribers: NotRequired[int]
    count_subscribers: NotRequired[int]

class stats_views(TypedDict):
    '''Views stats'''
    age: NotRequired[List['objects.stats_sex_age']]
    cities: NotRequired[List['objects.stats_city']]
    countries: NotRequired[List['objects.stats_country']]
    mobile_views: NotRequired[int]  # Number of views from mobile devices
    sex: NotRequired[List['objects.stats_sex_age']]
    sex_age: NotRequired[List['objects.stats_sex_age']]
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
    sex_age: NotRequired[List['objects.stats_sex_age']]

class status_status(TypedDict):
    text: str  # Status text
    audio: NotRequired['objects.audio_audio']

class storage_value(TypedDict):
    key: str
    value: str

class stories_clickable_area(TypedDict):
    x: NotRequired[int]
    y: NotRequired[int]

class stories_clickable_sticker(TypedDict):
    clickable_area: List['objects.stories_clickable_area']
    id: int  # Clickable sticker ID
    hashtag: NotRequired[str]
    link_object: NotRequired['objects.base_link']
    mention: NotRequired[str]
    tooltip_text: NotRequired[str]
    owner_id: NotRequired[int]
    story_id: NotRequired[int]
    question: NotRequired[str]
    question_button: NotRequired[str]
    place_id: NotRequired[int]
    market_item: NotRequired['objects.market_market_item']
    audio: NotRequired['objects.audio_audio']
    audio_start_time: NotRequired[int]
    style: NotRequired[Literal['transparent', 'blue_gradient', 'red_gradient', 'underline', 'blue', 'green', 'white', 'question_reply', 'light', 'impressive']]
    type: Literal['hashtag', 'mention', 'link', 'question', 'place', 'market_item', 'music', 'story_reply', 'owner', 'post', 'poll', 'sticker', 'app']
    subtype: NotRequired[Literal['market_item', 'aliexpress_product']]
    post_owner_id: NotRequired[int]
    post_id: NotRequired[int]
    poll: NotRequired['objects.polls_poll']
    color: NotRequired[str]  # Color, hex format
    sticker_id: NotRequired[int]  # Sticker ID
    sticker_pack_id: NotRequired[int]  # Sticker pack ID
    app: NotRequired['objects.apps_app_min']
    app_context: NotRequired[str]  # Additional context for app sticker
    has_new_interactions: NotRequired[bool]  # Whether current user has unread interaction with this app
    is_broadcast_notify_allowed: NotRequired[bool]  # Whether current user allowed broadcast notify from this app

class stories_clickable_stickers(TypedDict):
    clickable_stickers: List['objects.stories_clickable_sticker']
    original_height: int
    original_width: int

class stories_feed_item(TypedDict):
    type: Literal['promo_stories', 'stories', 'live_active', 'live_finished', 'community_grouped_stories', 'app_grouped_stories', 'birthday']  # Type of Feed Item
    stories: NotRequired[List['objects.stories_story']]  # Author stories
    grouped: NotRequired[List['objects.stories_feed_item']]  # Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)
    app: NotRequired['objects.apps_app_min']  # App, which stories has been grouped (for type app_grouped_stories)
    promo_data: NotRequired['objects.stories_promo_block']  # Additional data for promo stories (for type promo_stories)

class stories_promo_block(TypedDict):
    '''Additional data for promo stories'''
    name: str  # Promo story title
    photo_50: str  # RL of square photo of the story with 50 pixels in width
    photo_100: str  # RL of square photo of the story with 100 pixels in width
    not_animated: bool  # Hide animation for promo story

class stories_replies(TypedDict):
    count: int  # Replies number.
    new: NotRequired[int]  # New replies number.

class stories_stat_line(TypedDict):
    name: str
    counter: NotRequired[int]
    is_unavailable: NotRequired[bool]

class stories_story(TypedDict):
    access_key: NotRequired[str]  # Access key for private object.
    can_comment: NotRequired['objects.base_bool_int']  # Information whether current user can comment the story (0 - no, 1 - yes).
    can_reply: NotRequired['objects.base_bool_int']  # Information whether current user can reply to the story (0 - no, 1 - yes).
    can_see: NotRequired['objects.base_bool_int']  # Information whether current user can see the story (0 - no, 1 - yes).
    can_like: NotRequired[bool]  # Information whether current user can like the story.
    can_share: NotRequired['objects.base_bool_int']  # Information whether current user can share the story (0 - no, 1 - yes).
    can_hide: NotRequired['objects.base_bool_int']  # Information whether current user can hide the story (0 - no, 1 - yes).
    date: NotRequired[int]  # Date when story has been added in Unixtime.
    expires_at: NotRequired[int]  # Story expiration time. Unixtime.
    id: int  # Story ID.
    is_deleted: NotRequired[bool]  # Information whether the story is deleted (false - no, true - yes).
    is_expired: NotRequired[bool]  # Information whether the story is expired (false - no, true - yes).
    link: NotRequired['objects.stories_story_link']
    owner_id: int  # Story owner's ID.
    parent_story: NotRequired['objects.stories_story']
    parent_story_access_key: NotRequired[str]  # Access key for private object.
    parent_story_id: NotRequired[int]  # Parent story ID.
    parent_story_owner_id: NotRequired[int]  # Parent story owner's ID.
    photo: NotRequired['objects.photos_photo']
    replies: NotRequired['objects.stories_replies']  # Replies counters to current story.
    seen: NotRequired['objects.base_bool_int']  # Information whether current user has seen the story or not (0 - no, 1 - yes).
    type: NotRequired['objects.stories_story_type']
    clickable_stickers: NotRequired['objects.stories_clickable_stickers']
    video: NotRequired['objects.video_video']
    views: NotRequired[int]  # Views number.
    can_ask: NotRequired['objects.base_bool_int']  # Information whether story has question sticker and current user can send question to the author
    can_ask_anonymous: NotRequired['objects.base_bool_int']  # Information whether story has question sticker and current user can send anonymous question to the author
    narratives_count: NotRequired[int]
    first_narrative_title: NotRequired[str]
    birthday_wish_user_id: NotRequired[int]
    can_use_in_narrative: NotRequired[bool]

class stories_story_link(TypedDict):
    text: str  # Link text
    url: str  # Link URL

class stories_story_stats(TypedDict):
    answer: 'objects.stories_story_stats_stat'
    bans: 'objects.stories_story_stats_stat'
    open_link: 'objects.stories_story_stats_stat'
    replies: 'objects.stories_story_stats_stat'
    shares: 'objects.stories_story_stats_stat'
    subscribers: 'objects.stories_story_stats_stat'
    views: 'objects.stories_story_stats_stat'
    likes: 'objects.stories_story_stats_stat'

class stories_story_stats_stat(TypedDict):
    count: NotRequired[int]  # Stat value
    state: 'objects.stories_story_stats_state'

stories_story_stats_state: TypeAlias = Literal['on', 'off', 'hidden']  # Statistic state

stories_story_type: TypeAlias = Literal['photo', 'video', 'live_active', 'live_finished', 'birthday_invite']  # Story type.

stories_upload_link_text: TypeAlias = Literal['to_store', 'vote', 'more', 'book', 'order', 'enroll', 'fill', 'signup', 'buy', 'ticket', 'write', 'open', 'learn_more', 'view', 'go_to', 'contact', 'watch', 'play', 'install', 'read', 'calendar']

class stories_viewers_item(TypedDict):
    is_liked: bool  # user has like for this object
    user_id: int  # user id
    user: NotRequired['objects.users_user_full']

class users_career(TypedDict):
    city_id: NotRequired[int]  # City ID
    company: NotRequired[str]  # Company name
    country_id: NotRequired[int]  # Country ID
    # from: NotRequired[int]  # From year
    group_id: NotRequired[int]  # Community ID
    id: NotRequired[int]  # Career ID
    position: NotRequired[str]  # Position
    until: NotRequired[int]  # Till year

class users_exports(TypedDict):
    facebook: NotRequired[int]
    livejournal: NotRequired[int]
    twitter: NotRequired[int]

users_fields: TypeAlias = Literal['photo_id', 'verified', 'sex', 'bdate', 'city', 'country', 'home_town', 'has_photo', 'photo_50', 'photo_100', 'photo_200_orig', 'photo_200', 'photo_400_orig', 'photo_max', 'photo_max_orig', 'online', 'lists', 'domain', 'has_mobile', 'contacts', 'site', 'education', 'universities', 'schools', 'status', 'last_seen', 'followers_count', 'counters', 'common_count', 'occupation', 'nickname', 'relatives', 'relation', 'personal', 'connections', 'exports', 'wall_comments', 'activities', 'interests', 'music', 'movies', 'tv', 'books', 'games', 'about', 'quotes', 'can_post', 'can_see_all_posts', 'can_see_audio', 'can_write_private_message', 'can_send_friend_request', 'is_favorite', 'is_hidden_from_feed', 'timezone', 'screen_name', 'maiden_name', 'crop_photo', 'is_friend', 'friend_status', 'career', 'military', 'blacklisted', 'blacklisted_by_me', 'can_subscribe_posts', 'descriptions', 'trending', 'mutual', 'friendship_weeks', 'can_invite_to_chats', 'stories_archive_count', 'video_live_level', 'video_live_count', 'clips_count']

class users_last_seen(TypedDict):
    platform: NotRequired[int]  # Type of the platform that used for the last authorization
    time: NotRequired[int]  # Last visit date (in Unix time)

class users_military(TypedDict):
    country_id: int  # Country ID
    # from: NotRequired[int]  # From year
    id: NotRequired[int]  # Military ID
    unit: str  # Unit name
    unit_id: int  # Unit ID
    until: NotRequired[int]  # Till year

class users_occupation(TypedDict):
    id: NotRequired[int]  # ID of school, university, company group
    name: NotRequired[str]  # Name of occupation
    type: NotRequired[str]  # Type of occupation

class users_online_info(TypedDict):
    visible: bool  # Whether you can see real online status of user or not
    last_seen: NotRequired[int]  # Last time we saw user being active
    is_online: NotRequired[bool]  # Whether user is currently online or not
    app_id: NotRequired[int]  # Application id from which user is currently online or was last seen online
    is_mobile: NotRequired[bool]  # Is user online from desktop app or mobile app
    status: NotRequired[Literal['recently', 'last_week', 'last_month', 'long_ago', 'not_show']]  # In case user online is not visible, it indicates approximate timeframe of user online

class users_personal(TypedDict):
    alcohol: NotRequired[int]  # User's views on alcohol
    inspired_by: NotRequired[str]  # User's inspired by
    langs: NotRequired[List[str]]
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
    country: NotRequired[int]  # Country ID
    id: NotRequired[str]  # School ID
    name: NotRequired[str]  # School name
    type: NotRequired[int]  # School type ID
    type_str: NotRequired[str]  # School type name
    year_from: NotRequired[int]  # Year the user started to study
    year_graduated: NotRequired[int]  # Graduation year
    year_to: NotRequired[int]  # Year the user finished to study

users_subscriptions_item: TypeAlias = Union['objects.users_user_xtr_type', 'objects.groups_group_full']

class users_university(TypedDict):
    chair: NotRequired[int]  # Chair ID
    chair_name: NotRequired[str]  # Chair name
    city: NotRequired[int]  # City ID
    country: NotRequired[int]  # Country ID
    education_form: NotRequired[str]  # Education form
    education_status: NotRequired[str]  # Education status
    faculty: NotRequired[int]  # Faculty ID
    faculty_name: NotRequired[str]  # Faculty name
    graduation: NotRequired[int]  # Graduation year
    id: NotRequired[int]  # University ID
    name: NotRequired[str]  # University name

class users_user(objects.users_user_min):
    sex: NotRequired['objects.base_sex']  # User sex
    screen_name: NotRequired[str]  # Domain name of the user's page
    photo_50: NotRequired[str]  # URL of square photo of the user with 50 pixels in width
    photo_100: NotRequired[str]  # URL of square photo of the user with 100 pixels in width
    online_info: NotRequired['objects.users_online_info']
    online: NotRequired['objects.base_bool_int']  # Information whether the user is online
    online_mobile: NotRequired['objects.base_bool_int']  # Information whether the user is online in mobile site or application
    online_app: NotRequired[int]  # Application ID
    verified: NotRequired['objects.base_bool_int']  # Information whether the user is verified
    trending: NotRequired['objects.base_bool_int']  # Information whether the user has a "fire" pictogram.
    friend_status: NotRequired['objects.friends_friend_status_status']
    mutual: NotRequired['objects.friends_requests_mutual']

class users_user_connections(TypedDict):
    skype: str  # User's Skype nickname
    facebook: str  # User's Facebook account
    facebook_name: NotRequired[str]  # User's Facebook name
    twitter: str  # User's Twitter account
    livejournal: NotRequired[str]  # User's Livejournal account
    instagram: str  # User's Instagram account

class users_user_counters(TypedDict):
    albums: NotRequired[int]  # Albums number
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

class users_user_full(objects.users_user):
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
    domain: NotRequired[str]  # Domain name of the user's page
    bdate: NotRequired[str]  # User's date of birth
    city: NotRequired['objects.base_city']
    country: NotRequired['objects.base_country']
    timezone: NotRequired[int]  # User's timezone
    owner_state: NotRequired['objects.owner_state']
    photo_200: NotRequired[str]  # URL of square photo of the user with 200 pixels in width
    photo_max: NotRequired[str]  # URL of square photo of the user with maximum width
    photo_200_orig: NotRequired[str]  # URL of user's photo with 200 pixels in width
    photo_400_orig: NotRequired[str]  # URL of user's photo with 400 pixels in width
    photo_max_orig: NotRequired[str]  # URL of user's photo of maximum size
    photo_id: NotRequired[str]  # ID of the user's main photo
    has_photo: NotRequired['objects.base_bool_int']  # Information whether the user has main photo
    has_mobile: NotRequired['objects.base_bool_int']  # Information whether the user specified his phone number
    is_friend: NotRequired['objects.base_bool_int']  # Information whether the user is a friend of current user
    wall_comments: NotRequired['objects.base_bool_int']  # Information whether current user can comment wall posts
    can_post: NotRequired['objects.base_bool_int']  # Information whether current user can post on the user's wall
    can_see_all_posts: NotRequired['objects.base_bool_int']  # Information whether current user can see other users' audio on the wall
    can_see_audio: NotRequired['objects.base_bool_int']  # Information whether current user can see the user's audio
    can_write_private_message: NotRequired['objects.base_bool_int']  # Information whether current user can write private message
    can_send_friend_request: NotRequired['objects.base_bool_int']  # Information whether current user can send a friend request
    can_be_invited_group: NotRequired[bool]  # Information whether current user can be invited to the community
    mobile_phone: NotRequired[str]  # User's mobile phone number
    home_phone: NotRequired[str]  # User's additional phone number
    site: NotRequired[str]  # User's website
    status_audio: NotRequired['objects.audio_audio']
    status: NotRequired[str]  # User's status
    activity: NotRequired[str]  # User's status
    last_seen: NotRequired['objects.users_last_seen']
    exports: NotRequired['objects.users_exports']
    crop_photo: NotRequired['objects.base_crop_photo']
    followers_count: NotRequired[int]  # Number of user's followers
    video_live_level: NotRequired[int]  # User level in live streams achievements
    video_live_count: NotRequired[int]  # Number of user's live streams
    blacklisted: NotRequired['objects.base_bool_int']  # Information whether current user is in the requested user's blacklist.
    blacklisted_by_me: NotRequired['objects.base_bool_int']  # Information whether the requested user is in current user's blacklist
    is_favorite: NotRequired['objects.base_bool_int']  # Information whether the requested user is in faves of current user
    is_hidden_from_feed: NotRequired['objects.base_bool_int']  # Information whether the requested user is hidden from current user's newsfeed
    common_count: NotRequired[int]  # Number of common friends with current user
    occupation: NotRequired['objects.users_occupation']
    career: NotRequired[List['objects.users_career']]
    military: NotRequired[List['objects.users_military']]
    university: NotRequired[int]  # University ID
    university_name: NotRequired[str]  # University name
    faculty: NotRequired[int]  # Faculty ID
    faculty_name: NotRequired[str]  # Faculty name
    graduation: NotRequired[int]  # Graduation year
    education_form: NotRequired[str]  # Education form
    education_status: NotRequired[str]  # User's education status
    home_town: NotRequired[str]  # User hometown
    relation: NotRequired['objects.users_user_relation']  # User relationship status
    relation_partner: NotRequired['objects.users_user_min']
    personal: NotRequired['objects.users_personal']
    universities: NotRequired[List['objects.users_university']]
    schools: NotRequired[List['objects.users_school']]
    relatives: NotRequired[List['objects.users_relative']]
    is_subscribed_podcasts: NotRequired[bool]  # Information whether current user is subscribed to podcasts
    can_subscribe_podcasts: NotRequired[bool]  # Owner in whitelist or not
    can_subscribe_posts: NotRequired[bool]  # Can subscribe to wall

class users_user_min(TypedDict):
    deactivated: NotRequired[str]  # Returns if a profile is deleted or blocked
    first_name: str  # User first name
    hidden: NotRequired[int]  # Returns if a profile is hidden.
    id: int  # User ID
    last_name: str  # User last name
    can_access_closed: NotRequired[bool]
    is_closed: NotRequired[bool]

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

class users_user_settings_xtr(TypedDict):
    connections: NotRequired['objects.users_user_connections']
    bdate: NotRequired[str]  # User's date of birth
    bdate_visibility: NotRequired[int]  # Information whether user's birthdate are hidden
    city: NotRequired['objects.base_city']
    country: NotRequired['objects.base_country']
    first_name: NotRequired[str]  # User first name
    home_town: str  # User's hometown
    last_name: NotRequired[str]  # User last name
    maiden_name: NotRequired[str]  # User maiden name
    name_request: NotRequired['objects.account_name_request']
    personal: NotRequired['objects.users_personal']
    phone: NotRequired[str]  # User phone number with some hidden digits
    relation: NotRequired['objects.users_user_relation']  # User relationship status
    relation_partner: NotRequired['objects.users_user_min']
    relation_pending: NotRequired['objects.base_bool_int']  # Information whether relation status is pending
    relation_requests: NotRequired[List['objects.users_user_min']]
    screen_name: NotRequired[str]  # Domain name of the user's page
    sex: NotRequired['objects.base_sex']  # User sex
    status: str  # User status
    status_audio: NotRequired['objects.audio_audio']
    interests: NotRequired['objects.account_user_settings_interests']
    languages: NotRequired[List[str]]

users_user_type: TypeAlias = Literal['profile']  # Object type

class users_user_xtr_counters(objects.users_user_full):
    counters: NotRequired['objects.users_user_counters']

class users_user_xtr_type(objects.users_user):
    type: NotRequired['objects.users_user_type']

class users_users_array(TypedDict):
    count: int  # Users number
    items: List[int]

class utils_domain_resolved(TypedDict):
    object_id: NotRequired[int]  # Object ID
    group_id: NotRequired[int]  # Group ID
    type: NotRequired['objects.utils_domain_resolved_type']

utils_domain_resolved_type: TypeAlias = Literal['user', 'group', 'application', 'page', 'vk_app']  # Object type

class utils_last_shortened_link(TypedDict):
    access_key: NotRequired[str]  # Access key for private stats
    key: NotRequired[str]  # Link key (characters after vk.cc/)
    short_url: NotRequired[str]  # Short link URL
    timestamp: NotRequired[int]  # Creation time in Unixtime
    url: NotRequired[str]  # Full URL
    views: NotRequired[int]  # Total views number

class utils_link_checked(TypedDict):
    link: NotRequired[str]  # Link URL
    status: NotRequired['objects.utils_link_checked_status']

utils_link_checked_status: TypeAlias = Literal['not_banned', 'banned', 'processing']  # Link status

class utils_link_stats(TypedDict):
    key: NotRequired[str]  # Link key (characters after vk.cc/)
    stats: NotRequired[List['objects.utils_stats']]

class utils_link_stats_extended(TypedDict):
    key: NotRequired[str]  # Link key (characters after vk.cc/)
    stats: NotRequired[List['objects.utils_stats_extended']]

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
    cities: NotRequired[List['objects.utils_stats_city']]
    countries: NotRequired[List['objects.utils_stats_country']]
    sex_age: NotRequired[List['objects.utils_stats_sex_age']]
    timestamp: NotRequired[int]  # Start time
    views: NotRequired[int]  # Total views number

class utils_stats_sex_age(TypedDict):
    age_range: NotRequired[str]  # Age denotation
    female: NotRequired[int]  #  Views by female users
    male: NotRequired[int]  #  Views by male users

class video_live_settings(TypedDict):
    '''Video live settings'''
    can_rewind: NotRequired['objects.base_bool_int']  # If user car rewind live or not
    is_endless: NotRequired['objects.base_bool_int']  # If live is endless or not
    max_duration: NotRequired[int]  # Max possible time for rewind

class video_restriction_button(TypedDict):
    '''Video restriction button'''
    action: NotRequired[Literal['play']]
    title: NotRequired[str]

class video_save_result(TypedDict):
    access_key: NotRequired[str]  # Video access key
    description: NotRequired[str]  # Video description
    owner_id: NotRequired[int]  # Video owner ID
    title: NotRequired[str]  # Video title
    upload_url: NotRequired[str]  # URL for the video uploading
    video_id: NotRequired[int]  # Video ID

class video_video(TypedDict):
    access_key: NotRequired[str]  # Video access key
    adding_date: NotRequired[int]  # Date when the video has been added in Unixtime
    can_comment: NotRequired['objects.base_bool_int']  # Information whether current user can comment the video
    can_edit: NotRequired['objects.base_bool_int']  # Information whether current user can edit the video
    can_like: NotRequired['objects.base_bool_int']  # Information whether current user can like the video
    can_repost: NotRequired['objects.base_bool_int']  # Information whether current user can repost the video
    can_subscribe: NotRequired['objects.base_bool_int']  # Information whether current user can subscribe to author of the video
    can_add_to_faves: NotRequired['objects.base_bool_int']  # Information whether current user can add the video to favourites
    can_add: NotRequired['objects.base_bool_int']  # Information whether current user can add the video
    can_attach_link: NotRequired['objects.base_bool_int']  # Information whether current user can attach action button to the video
    is_private: NotRequired['objects.base_bool_int']  # 1 if video is private
    comments: NotRequired[int]  # Number of comments
    date: NotRequired[int]  # Date when video has been uploaded in Unixtime
    description: NotRequired[str]  # Video description
    duration: NotRequired[int]  # Video duration in seconds
    image: NotRequired[List['objects.video_video_image']]
    first_frame: NotRequired[List['objects.video_video_image']]
    width: NotRequired[int]  # Video width
    height: NotRequired[int]  # Video height
    id: NotRequired[int]  # Video ID
    owner_id: NotRequired[int]  # Video owner ID
    user_id: NotRequired[int]  # Id of the user who uploaded the video if it was uploaded to a group by member
    title: NotRequired[str]  # Video title
    is_favorite: NotRequired[bool]  # Whether video is added to bookmarks
    player: NotRequired[str]  # Video embed URL
    processing: NotRequired['objects.base_property_exists']  # Returns if the video is processing
    converting: NotRequired['objects.base_bool_int']  # 1 if  video is being converted
    restriction: NotRequired['objects.media_restriction']
    added: NotRequired['objects.base_bool_int']  # 1 if video is added to user's albums
    is_subscribed: NotRequired['objects.base_bool_int']  # 1 if user is subscribed to author of the video
    track_code: NotRequired[str]
    repeat: NotRequired['objects.base_property_exists']  # Information whether the video is repeated
    type: NotRequired[Literal['video', 'music_video', 'movie']]
    views: NotRequired[int]  # Number of views
    local_views: NotRequired[int]  # If video is external, number of views on vk
    content_restricted: NotRequired[int]  # Restriction code
    content_restricted_message: NotRequired[str]  # Restriction text
    balance: NotRequired[int]  # Live donations balance
    live_status: NotRequired[Literal['waiting', 'started', 'finished', 'failed', 'upcoming']]  # Live stream status
    live: NotRequired['objects.base_property_exists']  # 1 if the video is a live stream
    upcoming: NotRequired['objects.base_property_exists']  # 1 if the video is an upcoming stream
    spectators: NotRequired[int]  # Number of spectators of the stream
    platform: NotRequired[str]  # External platform
    likes: NotRequired['objects.base_likes']
    reposts: NotRequired['objects.base_reposts_info']

class video_video_album_full(TypedDict):
    count: int  # Total number of videos in album
    id: NotRequired[int]  # Album ID
    image: NotRequired[List['objects.video_video_image']]  # Album cover image in different sizes
    image_blur: NotRequired['objects.base_property_exists']  # Need blur album thumb or not
    is_system: NotRequired['objects.base_property_exists']  # Information whether album is system
    owner_id: int  # Album owner's ID
    title: str  # Album title
    updated_time: int  # Date when the album has been updated last time in Unixtime

class video_video_files(TypedDict):
    external: NotRequired[str]  # URL of the external player
    mp4_240: NotRequired[str]  # URL of the mpeg4 file with 240p quality
    mp4_360: NotRequired[str]  # URL of the mpeg4 file with 360p quality
    mp4_480: NotRequired[str]  # URL of the mpeg4 file with 480p quality
    mp4_720: NotRequired[str]  # URL of the mpeg4 file with 720p quality
    mp4_1080: NotRequired[str]  # URL of the mpeg4 file with 1080p quality
    flv_320: NotRequired[str]  # URL of the flv file with 320p quality

class video_video_full(objects.video_video):
    files: NotRequired['objects.video_video_files']
    live_settings: NotRequired['objects.video_live_settings']  # Settings for live stream

class video_video_image(objects.base_image):
    with_padding: NotRequired['objects.base_property_exists']

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
    view_url: str  # URL of the page with note preview

class wall_carousel_base(TypedDict):
    carousel_offset: NotRequired[int]  # Index of current carousel element

class wall_comment_attachment(TypedDict):
    audio: NotRequired['objects.audio_audio']
    doc: NotRequired['objects.docs_doc']
    link: NotRequired['objects.base_link']
    market: NotRequired['objects.market_market_item']
    market_market_album: NotRequired['objects.market_market_album']
    note: NotRequired['objects.wall_attached_note']
    page: NotRequired['objects.pages_wikipage_full']
    photo: NotRequired['objects.photos_photo']
    sticker: NotRequired['objects.base_sticker']
    type: 'objects.wall_comment_attachment_type'
    video: NotRequired['objects.video_video']

wall_comment_attachment_type: TypeAlias = Literal['photo', 'audio', 'video', 'doc', 'link', 'note', 'page', 'market_market_album', 'market', 'sticker']  # Attachment type

class wall_geo(TypedDict):
    coordinates: NotRequired[str]  # Coordinates as string. <latitude> <longtitude>
    place: NotRequired['objects.base_place']
    showmap: NotRequired[int]  # Information whether a map is showed
    type: NotRequired[str]  # Place type

class wall_graffiti(TypedDict):
    id: NotRequired[int]  # Graffiti ID
    owner_id: NotRequired[int]  # Graffiti owner's ID
    photo_200: NotRequired[str]  # URL of the preview image with 200 px in width
    photo_586: NotRequired[str]  # URL of the preview image with 586 px in width

class wall_post_copyright(TypedDict):
    id: NotRequired[int]
    link: str
    name: str
    type: str

class wall_post_source(TypedDict):
    data: NotRequired[str]  # Additional data
    platform: NotRequired[str]  # Platform name
    type: NotRequired['objects.wall_post_source_type']
    url: NotRequired[str]  # URL to an external site used to publish the post

wall_post_source_type: TypeAlias = Literal['vk', 'widget', 'api', 'rss', 'sms']  # Type of post source

wall_post_type: TypeAlias = Literal['post', 'copy', 'reply', 'postpone', 'suggest']  # Post type

class wall_posted_photo(TypedDict):
    id: NotRequired[int]  # Photo ID
    owner_id: NotRequired[int]  # Photo owner's ID
    photo_130: NotRequired[str]  # URL of the preview image with 130 px in width
    photo_604: NotRequired[str]  # URL of the preview image with 604 px in width

class wall_views(TypedDict):
    count: NotRequired[int]  # Count

class wall_wall_comment(TypedDict):
    attachments: NotRequired[List['objects.wall_comment_attachment']]
    date: int  # Date when the comment has been added in Unixtime
    from_id: int  # Author ID
    id: int  # Comment ID
    likes: NotRequired['objects.base_likes_info']
    real_offset: NotRequired[int]  # Real position of the comment
    reply_to_comment: NotRequired[int]  # Replied comment ID
    reply_to_user: NotRequired[int]  # Replied user ID
    text: str  # Comment text
    thread: NotRequired['objects.comment_thread']
    post_id: NotRequired[int]
    owner_id: NotRequired[int]
    parents_stack: NotRequired[List[int]]
    deleted: NotRequired[bool]

class wall_wallpost(TypedDict):
    access_key: NotRequired[str]  # Access key to private object
    attachments: NotRequired[List['objects.wall_wallpost_attachment']]
    copyright: NotRequired['objects.wall_post_copyright']  # Information about the source of the post
    date: NotRequired[int]  # Date of publishing in Unixtime
    edited: NotRequired[int]  # Date of editing in Unixtime
    from_id: NotRequired[int]  # Post author ID
    geo: NotRequired['objects.wall_geo']
    id: NotRequired[int]  # Post ID
    is_archived: NotRequired[bool]  # Is post archived, only for post owners
    is_favorite: NotRequired[bool]  # Information whether the post in favorites list
    likes: NotRequired['objects.base_likes_info']  # Count of likes
    owner_id: NotRequired[int]  # Wall owner's ID
    post_source: NotRequired['objects.wall_post_source']
    post_type: NotRequired['objects.wall_post_type']
    reposts: NotRequired['objects.base_reposts_info']
    signer_id: NotRequired[int]  # Post signer ID
    text: NotRequired[str]  # Post text
    views: NotRequired['objects.wall_views']  # Count of views

class wall_wallpost_attachment(TypedDict):
    access_key: NotRequired[str]  # Access key for the audio
    album: NotRequired['objects.photos_photo_album']
    app: NotRequired['objects.wall_app_post']
    audio: NotRequired['objects.audio_audio']
    doc: NotRequired['objects.docs_doc']
    event: NotRequired['objects.events_event_attach']
    group: NotRequired['objects.groups_group_attach']
    graffiti: NotRequired['objects.wall_graffiti']
    link: NotRequired['objects.base_link']
    market: NotRequired['objects.market_market_item']
    market_album: NotRequired['objects.market_market_album']
    note: NotRequired['objects.wall_attached_note']
    page: NotRequired['objects.pages_wikipage_full']
    photo: NotRequired['objects.photos_photo']
    photos_list: NotRequired[List[str]]
    poll: NotRequired['objects.polls_poll']
    posted_photo: NotRequired['objects.wall_posted_photo']
    type: 'objects.wall_wallpost_attachment_type'
    video: NotRequired['objects.video_video']

wall_wallpost_attachment_type: TypeAlias = Literal['photo', 'posted_photo', 'audio', 'video', 'doc', 'link', 'graffiti', 'note', 'app', 'poll', 'page', 'album', 'photos_list', 'market_market_album', 'market', 'event']  # Attachment type

class wall_wallpost_full(objects.wall_carousel_base, objects.wall_wallpost):
    copy_history: NotRequired[List['objects.wall_wallpost']]
    can_edit: NotRequired['objects.base_bool_int']  # Information whether current user can edit the post
    created_by: NotRequired[int]  # Post creator ID (if post still can be edited)
    can_delete: NotRequired['objects.base_bool_int']  # Information whether current user can delete the post
    can_pin: NotRequired['objects.base_bool_int']  # Information whether current user can pin the post
    is_pinned: NotRequired[int]  # Information whether the post is pinned
    comments: NotRequired['objects.base_comments_info']
    marked_as_ads: NotRequired['objects.base_bool_int']  # Information whether the post is marked as ads
    short_text_rate: NotRequired[float]  # Preview length control parameter

class wall_wallpost_to_id(TypedDict):
    attachments: NotRequired[List['objects.wall_wallpost_attachment']]
    comments: NotRequired['objects.base_comments_info']
    copy_owner_id: NotRequired[int]  # ID of the source post owner
    copy_post_id: NotRequired[int]  # ID of the source post
    date: NotRequired[int]  # Date of publishing in Unixtime
    from_id: NotRequired[int]  # Post author ID
    geo: NotRequired['objects.wall_geo']
    id: NotRequired[int]  # Post ID
    is_favorite: NotRequired[bool]  # Information whether the post in favorites list
    likes: NotRequired['objects.base_likes_info']
    post_id: NotRequired[int]  # wall post ID (if comment)
    post_source: NotRequired['objects.wall_post_source']
    post_type: NotRequired['objects.wall_post_type']
    reposts: NotRequired['objects.base_reposts_info']
    signer_id: NotRequired[int]  # Post signer ID
    text: NotRequired[str]  # Post text
    to_id: NotRequired[int]  # Wall owner's ID

class widgets_comment_media(TypedDict):
    item_id: NotRequired[int]  # Media item ID
    owner_id: NotRequired[int]  # Media owner's ID
    thumb_src: NotRequired[str]  # URL of the preview image (type=photo only)
    type: NotRequired['objects.widgets_comment_media_type']

widgets_comment_media_type: TypeAlias = Literal['audio', 'photo', 'video']  # Media type

class widgets_comment_replies(TypedDict):
    can_post: NotRequired['objects.base_bool_int']  # Information whether current user can comment the post
    count: NotRequired[int]  # Comments number
    replies: NotRequired[List['objects.widgets_comment_replies_item']]

class widgets_comment_replies_item(TypedDict):
    cid: NotRequired[int]  # Comment ID
    date: NotRequired[int]  # Date when the comment has been added in Unixtime
    likes: NotRequired['objects.widgets_widget_likes']
    text: NotRequired[str]  # Comment text
    uid: NotRequired[int]  # User ID
    user: NotRequired['objects.users_user_full']

class widgets_widget_comment(TypedDict):
    attachments: NotRequired[List['objects.wall_comment_attachment']]
    can_delete: NotRequired['objects.base_bool_int']  # Information whether current user can delete the comment
    comments: NotRequired['objects.widgets_comment_replies']
    date: int  # Date when the comment has been added in Unixtime
    from_id: int  # Comment author ID
    id: int  # Comment ID
    likes: NotRequired['objects.base_likes_info']
    media: NotRequired['objects.widgets_comment_media']
    post_source: NotRequired['objects.wall_post_source']
    post_type: int  # Post type
    reposts: NotRequired['objects.base_reposts_info']
    text: str  # Comment text
    to_id: int  # Wall owner
    user: NotRequired['objects.users_user_full']

class widgets_widget_likes(TypedDict):
    count: NotRequired[int]  # Likes number

class widgets_widget_page(TypedDict):
    comments: NotRequired['objects.base_object_count']
    date: NotRequired[int]  # Date when widgets on the page has been initialized firstly in Unixtime
    description: NotRequired[str]  # Page description
    id: NotRequired[int]  # Page ID
    likes: NotRequired['objects.base_object_count']
    page_id: NotRequired[str]  # page_id parameter value
    photo: NotRequired[str]  # URL of the preview image
    title: NotRequired[str]  # Page title
    url: NotRequired[str]  # Page absolute URL
