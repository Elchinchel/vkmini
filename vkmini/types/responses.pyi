from typing import TYPE_CHECKING, Any, Dict, List, Union, Literal, Optional
from typing_extensions import TypedDict, NotRequired

if TYPE_CHECKING:
    from . import objects, methods, responses


class account_changePassword_response(TypedDict):
    token: str  # New token
    secret: NotRequired[str]  # New secret

class account_getActiveOffers_response(TypedDict):
    count: int  # Total number
    items: List['objects.account_offer']

account_getAppPermissions_response: int  # Permissions mask

class account_getBanned_response(TypedDict):
    count: int  # Total number
    items: List[int]
    profiles: NotRequired[List['objects.users_user_min']]
    groups: NotRequired[List['objects.groups_group']]

account_getCounters_response: 'objects.account_account_counters'

account_getInfo_response: 'objects.account_info'

account_getProfileInfo_response: 'objects.account_user_settings'

account_getPushSettings_response: 'objects.account_push_settings'

class account_saveProfileInfo_response(TypedDict):
    changed: NotRequired['objects.base_bool_int']  # 1 if changes has been processed
    name_request: NotRequired['objects.account_name_request']

ads_addOfficeUsers_response: bool  # true if success

ads_checkLink_response: 'objects.ads_link_status'

ads_createAds_response: List[int]

ads_createCampaigns_response: List[int]

ads_createClients_response: List[int]

class ads_createTargetGroup_response(TypedDict):
    id: NotRequired[int]  # Group ID
    pixel: NotRequired[str]  # Pixel code

ads_deleteAds_response: List[int]

ads_deleteCampaigns_response: int  # 0 if success

ads_deleteClients_response: int  # 0 if sucess

ads_getAccounts_response: List['objects.ads_account']

ads_getAdsLayout_response: List['objects.ads_ad_layout']

ads_getAdsTargeting_response: List['objects.ads_targ_settings']

ads_getAds_response: List['objects.ads_ad']

ads_getBudget_response: int  # Budget

ads_getCampaigns_response: List['objects.ads_campaign']

class ads_getCategories_response(TypedDict):
    v1: NotRequired[List['objects.ads_category']]  # Old categories
    v2: NotRequired[List['objects.ads_category']]  # Actual categories

ads_getClients_response: List['objects.ads_client']

ads_getDemographics_response: List['objects.ads_demo_stats']

ads_getFloodStats_response: 'objects.ads_flood_stats'

class ads_getLookalikeRequests_response(TypedDict):
    count: int  # Total count of found lookalike requests
    items: List['objects.ads_lookalike_request']  # found lookalike requests

class ads_getMusicians_response(TypedDict):
    items: List['objects.ads_musician']  # Musicians

ads_getOfficeUsers_response: List['objects.ads_users']

ads_getPostsReach_response: List['objects.ads_promoted_post_reach']

ads_getRejectionReason_response: 'objects.ads_reject_reason'

ads_getStatistics_response: List['objects.ads_stats']

ads_getSuggestions_cities_response: List['objects.ads_targ_suggestions_cities']

ads_getSuggestions_regions_response: List['objects.ads_targ_suggestions_regions']

ads_getSuggestions_response: List['objects.ads_targ_suggestions']

ads_getSuggestions_schools_response: List['objects.ads_targ_suggestions_schools']

ads_getTargetGroups_response: List['objects.ads_target_group']

ads_getTargetingStats_response: 'objects.ads_targ_stats'

ads_getUploadURL_response: str  # Photo upload URL

ads_getVideoUploadURL_response: str  # Video upload URL

ads_importTargetContacts_response: int  # Imported contacts number

ads_removeOfficeUsers_response: bool  # true if success

ads_updateAds_response: List[int]

ads_updateCampaigns_response: int  # Campaign ID

ads_updateClients_response: int  # Client ID

ads_updateOfficeUsers_response: List['objects.ads_updateOfficeUsers_result']

class adsweb_getAdCategories_response(TypedDict):
    categories: List['objects.adsweb_getAdCategories_response_categories_category']

class adsweb_getAdUnitCode_response(TypedDict):
    html: str

class adsweb_getAdUnits_response(TypedDict):
    count: int
    ad_units: NotRequired[List['objects.adsweb_getAdUnits_response_ad_units_ad_unit']]

class adsweb_getFraudHistory_response(TypedDict):
    count: int
    entries: NotRequired[List['objects.adsweb_getFraudHistory_response_entries_entry']]

class adsweb_getSites_response(TypedDict):
    count: int
    sites: NotRequired[List['objects.adsweb_getSites_response_sites_site']]

class adsweb_getStatistics_response(TypedDict):
    next_page_id: NotRequired[str]
    items: List['objects.adsweb_getStatistics_response_items_item']

class appWidgets_getAppImageUploadServer_response(TypedDict):
    upload_url: NotRequired[str]  # To upload an image, generate POST-request to upload_url with a file in photo field. Then call appWidgets.saveAppImage method

appWidgets_getAppImages_response: 'objects.appWidgets_photos'

class appWidgets_getGroupImageUploadServer_response(TypedDict):
    upload_url: NotRequired[str]  # To upload an image, generate POST-request to upload_url with a file in photo field. Then call appWidgets.saveAppImage method

appWidgets_getGroupImages_response: 'objects.appWidgets_photos'

appWidgets_getImagesById_response: List['objects.appWidgets_photo']

appWidgets_saveAppImage_response: 'objects.appWidgets_photo'

appWidgets_saveGroupImage_response: 'objects.appWidgets_photo'

class apps_getCatalog_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.apps_app']]

class apps_getFriendsList_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.users_user_full']]

class apps_getLeaderboard_extended_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.apps_leaderboard']]
    profiles: NotRequired[List['objects.users_user_min']]

class apps_getLeaderboard_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.apps_leaderboard']]

class apps_getScopes_response(TypedDict):
    count: int  # Total number
    items: List['objects.apps_scope']

apps_getScore_response: int  # Score number

class apps_get_response(TypedDict):
    count: NotRequired[int]  # Total number of applications
    items: NotRequired[List['objects.apps_app']]  # List of applications

apps_sendRequest_response: int  # Request ID

class auth_restore_response(TypedDict):
    success: NotRequired[Literal[1]]  # 1 if success
    sid: NotRequired[str]  # Parameter needed to grant access by code

base_bool_response: 'objects.base_bool_int'

base_getUploadServer_response: 'objects.base_upload_server'

base_ok_response: Literal[1]

board_addTopic_response: int  # Topic ID

board_createComment_response: int  # Comment ID

class board_getComments_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.board_topic_comment']
    poll: NotRequired['objects.board_topic_poll']
    profiles: List['objects.users_user']
    groups: List['objects.groups_group']

class board_getComments_response(TypedDict):
    count: int  # Total number
    items: List['objects.board_topic_comment']
    poll: NotRequired['objects.board_topic_poll']

class board_getTopics_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.board_topic']
    default_order: 'objects.board_default_order'
    can_add_topics: 'objects.base_bool_int'  # Information whether current user can add topic
    profiles: List['objects.users_user_min']

class board_getTopics_response(TypedDict):
    count: int  # Total number
    items: List['objects.board_topic']
    default_order: 'objects.board_default_order'
    can_add_topics: 'objects.base_bool_int'  # Information whether current user can add topic

class database_getChairs_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.base_object']]

database_getCitiesById_response: List['objects.base_object']

class database_getCities_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.database_city']]

database_getCountriesById_response: List['objects.base_country']

class database_getCountries_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.base_country']]

class database_getFaculties_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.database_faculty']]

database_getMetroStationsById_response: List['objects.database_station']

class database_getMetroStations_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.database_station']]

class database_getRegions_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.database_region']]

database_getSchoolClasses_response: Union[str, int]

class database_getSchools_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.database_school']]

class database_getUniversities_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.database_university']]

class docs_add_response(TypedDict):
    id: NotRequired[int]  # Doc ID

docs_getById_response: List['objects.docs_doc']

class docs_getTypes_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.docs_doc_types']]

docs_getUploadServer: 'objects.base_upload_server'

class docs_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.docs_doc']

class docs_save_response(TypedDict):
    type: NotRequired['objects.docs_doc_attachment_type']
    audio_message: NotRequired['objects.messages_audio_message']
    doc: NotRequired['objects.docs_doc']
    graffiti: NotRequired['objects.messages_graffiti']

class docs_search_response(TypedDict):
    count: int  # Total number
    items: List['objects.docs_doc']

class downloadedGames_paid_status_response(TypedDict):
    is_paid: bool  # Game has been paid

fave_addTag_response: 'objects.fave_tag'

class fave_getPages_response(TypedDict):
    count: NotRequired[int]
    items: NotRequired[List['objects.fave_page']]

class fave_getTags_response(TypedDict):
    count: NotRequired[int]
    items: NotRequired[List['objects.fave_tag']]

class fave_get_extended_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.fave_bookmark']]
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group']]

class fave_get_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.fave_bookmark']]

class friends_addList_response(TypedDict):
    list_id: int  # List ID

friends_add_response: Literal[1, 2, 4]  # Friend request status

friends_areFriends_extended_response: List['objects.friends_friend_extended_status']

friends_areFriends_response: List['objects.friends_friend_status']

class friends_delete_response(TypedDict):
    success: int
    friend_deleted: NotRequired[Literal[1]]  # Returns 1 if friend has been deleted
    out_request_deleted: NotRequired[Literal[1]]  # Returns 1 if out request has been canceled
    in_request_deleted: NotRequired[Literal[1]]  # Returns 1 if incoming request has been declined
    suggestion_deleted: NotRequired[Literal[1]]  # Returns 1 if suggestion has been declined

friends_getAppUsers_response: List[int]

friends_getByPhones_response: List['objects.friends_user_xtr_phone']

class friends_getLists_response(TypedDict):
    count: int  # Total number of friends lists
    items: List['objects.friends_friends_list']

friends_getMutual_response: List[int]

friends_getMutual_target_uids_response: List['objects.friends_mutual_friend']

class friends_getOnline_online_mobile_response(TypedDict):
    online: NotRequired[List[int]]
    online_mobile: NotRequired[List[int]]

friends_getOnline_response: List[int]

friends_getRecent_response: List[int]

class friends_getRequests_extended_response(TypedDict):
    count: NotRequired[int]  # Total requests number
    items: NotRequired[List['objects.friends_requests_xtr_message']]

class friends_getRequests_need_mutual_response(TypedDict):
    count: NotRequired[int]  # Total requests number
    items: NotRequired[List['objects.friends_requests']]

class friends_getRequests_response(TypedDict):
    count: NotRequired[int]  # Total requests number
    items: NotRequired[List[int]]
    count_unread: NotRequired[int]  # Total unread requests number

class friends_getSuggestions_response(TypedDict):
    count: int  # Total results number
    items: List['objects.users_user_full']

class friends_get_fields_response(TypedDict):
    count: int  # Total friends number
    items: List['objects.friends_user_xtr_lists']

class friends_get_response(TypedDict):
    count: int  # Total friends number
    items: List[int]

class friends_search_response(TypedDict):
    count: int  # Total number
    items: List['objects.users_user_full']

class gifts_get_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.gifts_gift']]

groups_addAddress_response: 'objects.groups_address'

class groups_addCallbackServer_response(TypedDict):
    server_id: NotRequired[int]

groups_addLink_response: 'objects.groups_group_link'

groups_create_response: 'objects.groups_group'

groups_editAddress_response: 'objects.groups_address'  # Result

class groups_getAddresses_response(TypedDict):
    count: int  # Total count of addresses
    items: List['objects.groups_address']

class groups_getBanned_response(TypedDict):
    count: int  # Total users number
    items: List['objects.groups_banned_item']

groups_getById_response: List['objects.groups_group_full']

class groups_getCallbackConfirmationCode_response(TypedDict):
    code: NotRequired[str]  # Confirmation code

class groups_getCallbackServers_response(TypedDict):
    count: int
    items: List['objects.groups_callback_server']

groups_getCallbackSettings_response: 'objects.groups_callback_settings'

class groups_getCatalogInfo_extended_response(TypedDict):
    enabled: int  # Information whether catalog is enabled for current user
    categories: NotRequired[List['objects.groups_group_category_full']]

class groups_getCatalogInfo_response(TypedDict):
    enabled: int  # Information whether catalog is enabled for current user
    categories: NotRequired[List['objects.groups_group_category']]

class groups_getCatalog_response(TypedDict):
    count: int  # Total communities number
    items: List['objects.groups_group']

class groups_getInvitedUsers_response(TypedDict):
    count: int  # Total communities number
    items: List['objects.users_user_full']

class groups_getInvites_extended_response(TypedDict):
    count: int  # Total communities number
    items: List['objects.groups_group_xtr_invited_by']
    profiles: List['objects.users_user_min']
    groups: List['objects.groups_group_full']

class groups_getInvites_response(TypedDict):
    count: int  # Total communities number
    items: List['objects.groups_group_xtr_invited_by']

groups_getLongPollServer_response: 'objects.groups_long_poll_server'

groups_getLongPollSettings_response: 'objects.groups_long_poll_settings'

class groups_getMembers_fields_response(TypedDict):
    count: int  # Total members number
    items: List['objects.groups_user_xtr_role']

class groups_getMembers_filter_response(TypedDict):
    count: int  # Total members number
    items: List['objects.groups_member_role']

class groups_getMembers_response(TypedDict):
    count: int  # Total members number
    items: List[int]

class groups_getRequests_fields_response(TypedDict):
    count: int  # Total communities number
    items: List['objects.users_user_full']

class groups_getRequests_response(TypedDict):
    count: int  # Total communities number
    items: List[int]

class groups_getSettings_response(TypedDict):
    access: NotRequired['objects.groups_group_access']  # Community access settings
    address: NotRequired[str]  # Community's page domain
    audio: 'objects.groups_group_audio'  # Audio settings
    articles: int  # Articles settings
    city_id: int  # City id of group
    contacts: NotRequired['objects.base_bool_int']
    links: NotRequired['objects.base_bool_int']
    sections_list: NotRequired[Dict[str, Any]]
    main_section: NotRequired['objects.groups_group_full_main_section']
    secondary_section: NotRequired[int]
    age_limits: NotRequired[int]
    country_id: int  # Country id of group
    description: str  # Community description
    docs: 'objects.groups_group_docs'  # Docs settings
    events: NotRequired['objects.base_bool_int']
    obscene_filter: 'objects.base_bool_int'  # Information whether the obscene filter is enabled
    obscene_stopwords: 'objects.base_bool_int'  # Information whether the stopwords filter is enabled
    obscene_words: List[str]  # The list of stop words
    event_group_id: NotRequired[int]
    photos: int  # Photos settings
    public_category: NotRequired[int]  # Information about the group category
    public_category_list: NotRequired[List['objects.groups_group_public_category_list']]
    public_date: NotRequired[str]
    public_date_label: NotRequired[str]
    public_subcategory: NotRequired[int]  # Information about the group subcategory
    rss: NotRequired[str]  # URL of the RSS feed
    start_date: NotRequired[int]  # Start date
    finish_date: NotRequired[int]  # Finish date in Unixtime format
    subject: NotRequired[int]  # Community subject ID
    subject_list: NotRequired[List['objects.groups_subject_item']]
    suggested_privacy: NotRequired[int]
    title: str  # Community title
    topics: 'objects.groups_group_topics'  # Topics settings
    twitter: NotRequired['objects.groups_settings_twitter']
    video: 'objects.groups_group_video'  # Video settings
    wall: 'objects.groups_group_wall'  # Wall settings
    website: NotRequired[str]  # Community website
    phone: NotRequired[str]  # Community phone
    email: NotRequired[str]  # Community email
    wiki: 'objects.groups_group_wiki'  # Wiki settings

groups_getTagList_response: List['objects.groups_group_tag']

class groups_getTokenPermissions_response(TypedDict):
    mask: int
    permissions: List['objects.groups_token_permission_setting']

class groups_get_extended_response(TypedDict):
    count: int  # Total communities number
    items: List['objects.groups_group_full']

class groups_get_response(TypedDict):
    count: int  # Total communities number
    items: List[int]

class groups_isMember_extended_response(TypedDict):
    member: 'objects.base_bool_int'  # Information whether user is a member of the group
    invitation: NotRequired['objects.base_bool_int']  # Information whether user has been invited to the group
    can_invite: NotRequired['objects.base_bool_int']  # Information whether user can be invited
    can_recall: NotRequired['objects.base_bool_int']  # Information whether user's invite to the group can be recalled
    request: NotRequired['objects.base_bool_int']  # Information whether user has sent request to the group

groups_isMember_response: 'objects.base_bool_int'  # Information whether user is a member of the group

groups_isMember_user_ids_extended_response: List['objects.groups_member_status_full']

groups_isMember_user_ids_response: List['objects.groups_member_status']

class groups_search_response(TypedDict):
    count: int  # Total communities number
    items: List['objects.groups_group']

leads_checkUser_response: 'objects.leads_checked'

leads_complete_response: 'objects.leads_complete'

leads_getStats_response: 'objects.leads_lead'

leads_getUsers_response: List['objects.leads_entry']

class leads_metricHit_response(TypedDict):
    result: NotRequired[bool]  # Information whether request has been processed successfully
    redirect_link: NotRequired[str]  # Redirect link

leads_start_response: 'objects.leads_start'

class likes_add_response(TypedDict):
    likes: int  # Total likes number

class likes_delete_response(TypedDict):
    likes: int  # Total likes number

class likes_getList_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.users_user_min']

class likes_getList_response(TypedDict):
    count: int  # Total number
    items: List[int]

class likes_isLiked_response(TypedDict):
    liked: 'objects.base_bool_int'  # Information whether user liked the object
    copied: 'objects.base_bool_int'  # Information whether user reposted the object

class market_addAlbum_response(TypedDict):
    market_album_id: NotRequired[int]  # Album ID

class market_add_response(TypedDict):
    market_item_id: NotRequired[int]  # Item ID

market_createComment_response: int  # Comment ID

market_deleteComment_response: 'objects.base_bool_int'  # Returns 1 if request has been processed successfully (0 if the comment is not found)

class market_getAlbumById_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.market_market_album']]

class market_getAlbums_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.market_market_album']]

class market_getById_extended_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.market_market_item_full']]

class market_getById_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.market_market_item']]

class market_getCategories_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.market_market_category']]

class market_getComments_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.wall_wall_comment']]

class market_getGroupOrders_response(TypedDict):
    count: int  # Total number
    items: List['objects.market_order']

class market_getOrderById_response(TypedDict):
    order: NotRequired['objects.market_order']

class market_getOrderItems_response(TypedDict):
    count: int  # Total number
    items: List['objects.market_order_item']

class market_getOrders_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.market_order']
    groups: NotRequired[List['objects.groups_group_full']]

class market_getOrders_response(TypedDict):
    count: int  # Total number
    items: List['objects.market_order']

class market_get_extended_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.market_market_item_full']]

class market_get_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.market_market_item']]

market_restoreComment_response: 'objects.base_bool_int'  # Returns 1 if request has been processed successfully (0 if the comment is not found)

class market_search_extended_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.market_market_item_full']]

class market_search_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.market_market_item']]

messages_createChat_response: int  # Chat ID

class messages_deleteChatPhoto_response(TypedDict):
    message_id: NotRequired[int]  # Service message ID
    chat: NotRequired['objects.messages_chat']

class messages_deleteConversation_response(TypedDict):
    last_deleted_id: int  # Id of the last message, that was deleted

messages_delete_response: Dict[str, Any]

messages_edit_response: 'objects.base_bool_int'  # Result

class messages_getByConversationMessageId_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_message']

class messages_getById_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_message']
    profiles: List['objects.users_user_full']
    groups: NotRequired[List['objects.groups_group_full']]

class messages_getById_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_message']

class messages_getChatPreview_response(TypedDict):
    preview: NotRequired['objects.messages_chat_preview']
    profiles: NotRequired[List['objects.users_user_full']]

messages_getChat_chat_ids_fields_response: List['objects.messages_chat_full']

messages_getChat_chat_ids_response: List['objects.messages_chat']

messages_getChat_fields_response: 'objects.messages_chat_full'

messages_getChat_response: 'objects.messages_chat'

class messages_getConversationMembers_response(TypedDict):
    count: int  # Chat members count
    items: List['objects.messages_conversation_member']
    chat_restrictions: NotRequired['objects.messages_chat_restrictions']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

class messages_getConversationsById_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_conversation']
    profiles: NotRequired[List['objects.users_user']]

class messages_getConversationsById_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_conversation']

class messages_getConversations_response(TypedDict):
    count: int  # Total number
    unread_count: NotRequired[int]  # Unread dialogs number
    items: List['objects.messages_conversation_with_message']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

class messages_getHistoryAttachments_response(TypedDict):
    items: NotRequired[List['objects.messages_history_attachment']]
    next_from: NotRequired[str]  # Value for pagination

class messages_getHistory_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_message']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

class messages_getImportantMessages_extended_response(TypedDict):
    messages: 'objects.messages_messages_array'
    profiles: NotRequired[List['objects.users_user']]
    groups: NotRequired[List['objects.groups_group']]
    conversations: NotRequired[List['objects.messages_conversation']]

class messages_getImportantMessages_response(TypedDict):
    messages: 'objects.messages_messages_array'
    profiles: NotRequired[List['objects.users_user']]
    groups: NotRequired[List['objects.groups_group']]
    conversations: NotRequired[List['objects.messages_conversation']]

class messages_getInviteLink_response(TypedDict):
    link: NotRequired[str]

messages_getLastActivity_response: 'objects.messages_last_activity'

class messages_getLongPollHistory_response(TypedDict):
    history: NotRequired[int]
    groups: NotRequired[List['objects.groups_group']]
    messages: NotRequired['objects.messages_longpoll_messages']
    profiles: NotRequired[List['objects.users_user_full']]
    chats: NotRequired[List['objects.messages_chat']]
    new_pts: NotRequired[int]  # Persistence timestamp
    more: NotRequired[bool]  # Has more
    conversations: NotRequired[List['objects.messages_conversation']]

messages_getLongPollServer_response: 'objects.messages_longpoll_params'

class messages_isMessagesFromGroupAllowed_response(TypedDict):
    is_allowed: NotRequired['objects.base_bool_int']

class messages_joinChatByInviteLink_response(TypedDict):
    chat_id: NotRequired[int]

messages_markAsImportant_response: List[int]

messages_pin_response: 'objects.messages_pinned_message'

class messages_searchConversations_response(TypedDict):
    count: NotRequired[int]  # Total results number
    items: NotRequired[List['objects.messages_conversation']]
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

class messages_search_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_message']

messages_send_response: int  # Message ID

messages_send_user_ids_response: Dict[str, Any]

class messages_setChatPhoto_response(TypedDict):
    message_id: NotRequired[int]  # Service message ID
    chat: NotRequired['objects.messages_chat']

class newsfeed_getBanned_extended_response(TypedDict):
    groups: NotRequired[List['objects.users_user_full']]
    profiles: NotRequired[List['objects.groups_group_full']]

class newsfeed_getBanned_response(TypedDict):
    groups: NotRequired[List[int]]
    members: NotRequired[List[int]]

class newsfeed_getComments_response(TypedDict):
    items: List['objects.newsfeed_newsfeed_item']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']
    next_from: NotRequired[str]  # New from value

class newsfeed_getLists_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.newsfeed_list_full']

class newsfeed_getLists_response(TypedDict):
    count: int  # Total number
    items: List['objects.newsfeed_list']

class newsfeed_getMentions_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wallpost_to_id']

class newsfeed_getRecommended_response(TypedDict):
    items: NotRequired[List['objects.newsfeed_newsfeed_item']]
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]
    new_offset: NotRequired[str]  # New offset value
    next_from: NotRequired[str]  # Next from value

class newsfeed_getSuggestedSources_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[Union['objects.groups_group_full', 'objects.users_user_xtr_type']]

class newsfeed_get_response(TypedDict):
    items: NotRequired[List['objects.newsfeed_newsfeed_item']]
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]
    next_from: NotRequired[str]  # New from value

newsfeed_saveList_response: int  # List ID

class newsfeed_search_extended_response(TypedDict):
    items: NotRequired[List['objects.wall_wallpost_full']]
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]
    suggested_queries: NotRequired[List[str]]
    next_from: NotRequired[str]
    count: NotRequired[int]  # Filtered number
    total_count: NotRequired[int]  # Total number

class newsfeed_search_response(TypedDict):
    items: NotRequired[List['objects.wall_wallpost_full']]
    suggested_queries: NotRequired[List[str]]
    next_from: NotRequired[str]
    count: NotRequired[int]  # Filtered number
    total_count: NotRequired[int]  # Total number

notes_add_response: int  # Note ID

notes_createComment_response: int  # Comment ID

notes_getById_response: 'objects.notes_note'

class notes_getComments_response(TypedDict):
    count: int  # Total number
    items: List['objects.notes_note_comment']

class notes_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.notes_note']

class notifications_get_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.notifications_notification_item']]
    profiles: NotRequired[List['objects.users_user']]
    groups: NotRequired[List['objects.groups_group']]
    last_viewed: NotRequired[int]  # Time when user has been checked notifications last time
    photos: NotRequired[List['objects.photos_photo']]
    videos: NotRequired[List['objects.video_video']]
    apps: NotRequired[List['objects.apps_app']]
    next_from: NotRequired[str]
    ttl: NotRequired[int]

notifications_markAsViewed_response: 'objects.base_bool_int'  # Result

notifications_sendMessage_response: List['objects.notifications_send_message_item']

orders_cancelSubscription_response: 'objects.base_bool_int'  # Result

orders_changeState_response: str  # New state

orders_getAmount_response: 'objects.orders_amount'

orders_getById_response: List['objects.orders_order']

orders_getUserSubscriptionById_response: 'objects.orders_subscription'

class orders_getUserSubscriptions_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.orders_subscription']]

orders_get_response: List['objects.orders_order']

orders_updateSubscription_response: 'objects.base_bool_int'  # Result

pages_getHistory_response: List['objects.pages_wikipage_history']

pages_getTitles_response: List['objects.pages_wikipage']

pages_getVersion_response: 'objects.pages_wikipage_full'

pages_get_response: 'objects.pages_wikipage_full'

pages_parseWiki_response: str  # HTML source

pages_saveAccess_response: int  # Page ID

pages_save_response: int  # Page ID

photos_copy_response: int  # Photo ID

photos_createAlbum_response: 'objects.photos_photo_album_full'

photos_createComment_response: int  # Created comment ID

photos_deleteComment_response: 'objects.base_bool_int'  # Returns 1 if request has been processed successfully, 0 if the comment is not found

photos_getAlbumsCount_response: int  # Albums number

class photos_getAlbums_response(TypedDict):
    count: int  # Total number
    items: List['objects.photos_photo_album_full']

class photos_getAllComments_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.photos_comment_xtr_pid']]

class photos_getAll_extended_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.photos_photo_full_xtr_real_offset']]
    more: NotRequired['objects.base_bool_int']  # Information whether next page is presented

class photos_getAll_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.photos_photo_xtr_real_offset']]
    more: NotRequired['objects.base_bool_int']  # Information whether next page is presented

photos_getById_extended_response: List['objects.photos_photo_full']

photos_getById_response: List['objects.photos_photo']

class photos_getComments_extended_response(TypedDict):
    count: int  # Total number
    real_offset: NotRequired[int]  # Real offset of the comments
    items: List['objects.wall_wall_comment']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']

class photos_getComments_response(TypedDict):
    count: NotRequired[int]  # Total number
    real_offset: NotRequired[int]  # Real offset of the comments
    items: NotRequired[List['objects.wall_wall_comment']]

photos_getMarketUploadServer_response: 'objects.base_upload_server'

photos_getMessagesUploadServer_response: 'objects.photos_photo_upload'

class photos_getNewTags_response(TypedDict):
    count: int  # Total number
    items: List['objects.photos_photo_xtr_tag_info']

photos_getTags_response: List['objects.photos_photo_tag']

photos_getUploadServer_response: 'objects.photos_photo_upload'

class photos_getUserPhotos_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.photos_photo_full']

class photos_getUserPhotos_response(TypedDict):
    count: int  # Total number
    items: List['objects.photos_photo']

photos_getWallUploadServer_response: 'objects.photos_photo_upload'

class photos_get_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.photos_photo_full']

class photos_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.photos_photo']

photos_putTag_response: int  # Created tag ID

photos_restoreComment_response: 'objects.base_bool_int'  # Returns 1 if request has been processed successfully, 0 if the comment is not found

photos_saveMarketAlbumPhoto_response: List['objects.photos_photo']

photos_saveMarketPhoto_response: List['objects.photos_photo']

photos_saveMessagesPhoto_response: List['objects.photos_photo']

photos_saveOwnerCoverPhoto_response: List['objects.base_image']

class photos_saveOwnerPhoto_response(TypedDict):
    photo_hash: str  # Photo hash
    photo_src: str  # Uploaded image url
    photo_src_big: NotRequired[str]  # Uploaded image url
    photo_src_small: NotRequired[str]  # Uploaded image url
    saved: NotRequired[int]  # Returns 1 if profile photo is saved
    post_id: NotRequired[int]  # Created post ID

photos_saveWallPhoto_response: List['objects.photos_photo']

photos_save_response: List['objects.photos_photo']

class photos_search_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.photos_photo']]

podcasts_getPopular_response: List['objects.podcast_popular_podcast']

podcasts_getRecentSearchRequests_response: List[str]

class podcasts_search_response(TypedDict):
    podcasts: NotRequired[List['objects.podcast_podcast']]
    episodes: NotRequired[List['objects.audio_audio']]
    profiles: NotRequired[List['objects.users_user']]
    groups: NotRequired[List[Any]]

polls_addVote_response: 'objects.base_bool_int'  # Result

polls_create_response: 'objects.polls_poll'

polls_deleteVote_response: 'objects.base_bool_int'  # Result

polls_getById_response: 'objects.polls_poll'

polls_getVoters_response: List['objects.polls_voters']

class prettyCards_create_response(TypedDict):
    owner_id: int  # Owner ID of created pretty card
    card_id: str  # Card ID of created pretty card

class prettyCards_delete_response(TypedDict):
    owner_id: int  # Owner ID of deleted pretty card
    card_id: str  # Card ID of deleted pretty card
    error: NotRequired[str]  # Error reason if error happened

class prettyCards_edit_response(TypedDict):
    owner_id: int  # Owner ID of edited pretty card
    card_id: str  # Card ID of edited pretty card

prettyCards_getById_response: List['objects.prettyCards_prettyCard']

prettyCards_getUploadURL_response: str  # Upload URL

class prettyCards_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.prettyCards_prettyCard']

class search_getHints_response(TypedDict):
    count: int
    items: List['objects.search_hint']
    suggested_queries: NotRequired[List[str]]

secure_checkToken_response: 'objects.secure_token_checked'

secure_getAppBalance_response: int  # App balance

secure_getSMSHistory_response: List['objects.secure_sms_notification']

secure_getTransactionsHistory_response: List['objects.secure_transaction']

secure_getUserLevel_response: List['objects.secure_level']

secure_giveEventSticker_response: Dict[str, Any]

secure_sendNotification_response: List[int]

stats_getPostReach_response: List['objects.stats_wallpost_stat']

stats_get_response: List['objects.stats_period']

status_get_response: 'objects.status_status'

storage_getKeys_response: List[str]

storage_get_response: str  # Value of key

storage_get_v5110_response: List['objects.storage_value']

storage_get_with_keys_response: List['objects.storage_value']

class stories_getBanned_extended_response(TypedDict):
    count: int  # Stories count
    items: List[int]
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']

class stories_getBanned_response(TypedDict):
    count: int  # Stories count
    items: List[int]

class stories_getById_extended_response(TypedDict):
    count: int  # Stories count
    items: List['objects.stories_story']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']

class stories_getById_response(TypedDict):
    count: int  # Stories count
    items: List['objects.stories_story']

class stories_getPhotoUploadServer_response(TypedDict):
    upload_url: str  # Upload URL
    user_ids: List[int]  # Users ID who can to see story.

stories_getStats_response: 'objects.stories_story_stats'

class stories_getVideoUploadServer_response(TypedDict):
    upload_url: str  # Upload URL
    user_ids: List[int]  # Users ID who can to see story.

class stories_getViewers_extended_V5115_response(TypedDict):
    count: int  # Viewers count
    items: List['objects.stories_viewers_item']
    hidden_reason: NotRequired[str]

class stories_getViewers_extended_response(TypedDict):
    count: int  # Viewers count
    items: List['objects.users_user_full']

class stories_get_V5113_response(TypedDict):
    count: int
    items: List['objects.stories_feed_item']
    profiles: NotRequired[List['objects.users_user']]
    groups: NotRequired[List['objects.groups_group']]
    need_upload_screen: NotRequired[bool]

class stories_get_response(TypedDict):
    count: int  # Stories count
    items: 'objects.stories_story'
    promo_data: NotRequired['objects.stories_promo_block']
    profiles: NotRequired[List['objects.users_user']]
    groups: NotRequired[List['objects.groups_group']]
    need_upload_screen: NotRequired[bool]

class stories_save_response(TypedDict):
    count: int
    items: List['objects.stories_story']

class stories_upload_response(TypedDict):
    upload_result: NotRequired[str]  # A string hash that is used in the stories.save method

class streaming_getServerUrl_response(TypedDict):
    endpoint: NotRequired[str]  # Server host
    key: NotRequired[str]  # Access key

class users_getFollowers_fields_response(TypedDict):
    count: int  # Total number of available results
    items: List['objects.users_user_full']

class users_getFollowers_response(TypedDict):
    count: int  # Total friends number
    items: List[int]

class users_getSubscriptions_extended_response(TypedDict):
    count: int  # Total number of available results
    items: List['objects.users_subscriptions_item']

class users_getSubscriptions_response(TypedDict):
    users: 'objects.users_users_array'
    groups: 'objects.groups_groups_array'

users_get_response: List['objects.users_user_xtr_counters']

class users_search_response(TypedDict):
    count: NotRequired[int]  # Total number of available results
    items: NotRequired[List['objects.users_user_full']]

utils_checkLink_response: 'objects.utils_link_checked'

class utils_getLastShortenedLinks_response(TypedDict):
    count: NotRequired[int]  # Total number of available results
    items: NotRequired[List['objects.utils_last_shortened_link']]

utils_getLinkStats_extended_response: 'objects.utils_link_stats_extended'

utils_getLinkStats_response: 'objects.utils_link_stats'

utils_getServerTime_response: int  # Time as Unixtime

utils_getShortLink_response: 'objects.utils_short_link'

utils_resolveScreenName_response: 'objects.utils_domain_resolved'

class video_addAlbum_response(TypedDict):
    album_id: int  # Created album ID

video_createComment_response: int  # Created comment ID

video_getAlbumById_response: 'objects.video_video_album_full'

class video_getAlbumsByVideo_extended_response(TypedDict):
    count: NotRequired[int]  # Total number
    items: NotRequired[List['objects.video_video_album_full']]

video_getAlbumsByVideo_response: List[int]

class video_getAlbums_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.video_video_album_full']

class video_getAlbums_response(TypedDict):
    count: int  # Total number
    items: List['objects.video_video_album_full']

class video_getComments_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_comment']
    profiles: List['objects.users_user_min']
    groups: List['objects.groups_group_full']

class video_getComments_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_comment']

class video_get_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.video_video_full']
    profiles: List['objects.users_user_min']
    groups: List['objects.groups_group_full']

class video_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.video_video']

video_restoreComment_response: 'objects.base_bool_int'  # Returns 1 if request has been processed successfully, 0 if the comment is not found

video_save_response: 'objects.video_save_result'

class video_search_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.video_video']
    profiles: List['objects.users_user_min']
    groups: List['objects.groups_group_full']

class video_search_response(TypedDict):
    count: int  # Total number
    items: List['objects.video_video']

class wall_createComment_response(TypedDict):
    comment_id: int  # Created comment ID

class wall_edit_response(TypedDict):
    post_id: int  # Edited post ID

class wall_getById_extended_response(TypedDict):
    items: List['objects.wall_wallpost_full']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']

wall_getById_legacy_response: List['objects.wall_wallpost_full']

class wall_getById_response(TypedDict):
    items: NotRequired[List['objects.wall_wallpost_full']]

class wall_getComment_extended_response(TypedDict):
    items: List['objects.wall_wall_comment']
    profiles: List['objects.users_user']
    groups: List['objects.groups_group']

class wall_getComment_response(TypedDict):
    items: List['objects.wall_wall_comment']

class wall_getComments_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_comment']
    show_reply_button: NotRequired[bool]
    can_post: NotRequired[bool]  # Information whether current user can comment the post
    groups_can_post: NotRequired[bool]  # Information whether groups can comment the post
    current_level_count: NotRequired[int]  # Count of replies of current level
    profiles: List['objects.users_user']
    groups: List['objects.groups_group']

class wall_getComments_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_comment']
    can_post: NotRequired[bool]  # Information whether current user can comment the post
    groups_can_post: NotRequired[bool]  # Information whether groups can comment the post
    current_level_count: NotRequired[int]  # Count of replies of current level

class wall_getReposts_response(TypedDict):
    items: List['objects.wall_wallpost_full']
    profiles: List['objects.users_user']
    groups: List['objects.groups_group']

class wall_get_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wallpost_full']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']

class wall_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wallpost_full']

class wall_postAdsStealth_response(TypedDict):
    post_id: int  # Created post ID

class wall_post_response(TypedDict):
    post_id: int  # Created post ID

class wall_repost_response(TypedDict):
    success: int
    post_id: int  # Created post ID
    reposts_count: int  # Reposts number
    wall_repost_count: int  # Reposts to wall number
    mail_repost_count: int  # Reposts to mail number
    likes_count: int  # Reposts number

class wall_search_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wallpost_full']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']

class wall_search_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wallpost_full']

class widgets_getComments_response(TypedDict):
    count: int  # Total number
    posts: List['objects.widgets_widget_comment']

class widgets_getPages_response(TypedDict):
    count: int  # Total number
    pages: List['objects.widgets_widget_page']

