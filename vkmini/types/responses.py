from vkmini.types import objects
from typing import Any, Dict, List, Literal, Union
from typing_extensions import NotRequired, TypeAlias, TypedDict


Flag: TypeAlias = int

class account_changePassword_response(TypedDict):
    token: str  # New token
    secret: NotRequired[str]  # New secret

class account_getActiveOffers_response(TypedDict):
    count: int  # Total number
    items: List['objects.account_offer']

account_getAppPermissions_response: TypeAlias = int  # Permissions mask

class account_getBanned_response(TypedDict):
    count: int  # Total number
    items: List[int]
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group']]

account_getCounters_response: TypeAlias = 'objects.account_account_counters'

account_getInfo_response: TypeAlias = 'objects.account_info'

account_getProfileInfo_response: TypeAlias = 'objects.account_user_settings'

account_getPushSettings_response: TypeAlias = 'objects.account_push_settings'

class account_saveProfileInfo_response(TypedDict):
    changed: 'objects.base_bool_int'  # 1 if changes has been processed
    name_request: NotRequired['objects.account_name_request']

ads_addOfficeUsers_response: TypeAlias = List[Flag]

ads_checkLink_response: TypeAlias = 'objects.ads_link_status'

ads_createAds_response: TypeAlias = List['objects.ads_create_ad_status']

ads_createCampaigns_response: TypeAlias = List['objects.ads_create_campaign_status']

ads_createClients_response: TypeAlias = List['objects.ads_create_clients_status']

class ads_createLookalikeRequest_response(TypedDict):
    request_id: NotRequired[int]  # Request ID

class ads_createTargetGroup_response(TypedDict):
    id: NotRequired[int]  # Group ID
    pixel: NotRequired[str]  # Pixel code

class ads_createTargetPixel_response(TypedDict):
    id: NotRequired[int]  # Pixel ID
    pixel: NotRequired[str]  # Pixel code

ads_deleteAds_response: TypeAlias = List[int]

ads_deleteCampaigns_response: TypeAlias = List[int]

ads_deleteClients_response: TypeAlias = List[int]

ads_getAccounts_response: TypeAlias = List['objects.ads_account']

ads_getAdsLayout_response: TypeAlias = List['objects.ads_ad_layout']

ads_getAdsTargeting_response: TypeAlias = List['objects.ads_targ_settings']

ads_getAds_response: TypeAlias = List['objects.ads_ad']

ads_getBudget_response: TypeAlias = str  # Budget

ads_getCampaigns_response: TypeAlias = List['objects.ads_campaign']

class ads_getCategories_response(TypedDict):
    v1: NotRequired[List['objects.ads_category']]  # Old categories
    v2: NotRequired[List['objects.ads_category']]  # Actual categories

ads_getClients_response: TypeAlias = List['objects.ads_client']

ads_getDemographics_response: TypeAlias = List['objects.ads_demo_stats']

ads_getFloodStats_response: TypeAlias = 'objects.ads_flood_stats'

class ads_getLookalikeRequests_response(TypedDict):
    count: int  # Total count of found lookalike requests
    items: List['objects.ads_lookalike_request']  # found lookalike requests

class ads_getMusicians_response(TypedDict):
    items: List['objects.ads_musician']  # Musicians

ads_getOfficeUsers_response: TypeAlias = List['objects.ads_users']

ads_getPostsReach_response: TypeAlias = List['objects.ads_promoted_post_reach']

ads_getRejectionReason_response: TypeAlias = 'objects.ads_reject_reason'

ads_getStatistics_response: TypeAlias = List['objects.ads_stats']

ads_getSuggestions_cities_response: TypeAlias = List['objects.ads_targ_suggestions_cities']

ads_getSuggestions_regions_response: TypeAlias = List['objects.ads_targ_suggestions_regions']

ads_getSuggestions_response: TypeAlias = List['objects.ads_targ_suggestions']

ads_getSuggestions_schools_response: TypeAlias = List['objects.ads_targ_suggestions_schools']

ads_getTargetGroups_response: TypeAlias = List['objects.ads_target_group']

ads_getTargetPixels_response: TypeAlias = List['objects.ads_target_pixel_info']

ads_getTargetingStats_response: TypeAlias = 'objects.ads_targ_stats'

ads_getUploadURL_response: TypeAlias = str  # Photo upload URL

ads_getVideoUploadURL_response: TypeAlias = str  # Video upload URL

ads_importTargetContacts_response: TypeAlias = int  # Imported contacts number

ads_removeOfficeUsers_response: TypeAlias = List[Flag]

class ads_removeTargetContacts_response(TypedDict):
    result: Literal[1]  # Operation result

class ads_saveLookalikeRequestResult_response(TypedDict):
    retargeting_group_id: int  # Retargeting group ID
    audience_count: int  # Audience count

class ads_shareTargetGroup_response(TypedDict):
    id: int  # Group ID

ads_updateAds_response: TypeAlias = List['objects.ads_update_ads_status']

ads_updateCampaigns_response: TypeAlias = List['objects.ads_create_campaign_status']

ads_updateClients_response: TypeAlias = List['objects.ads_update_clients_status']

ads_updateOfficeUsers_response: TypeAlias = List['objects.ads_updateOfficeUsers_result']

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

class apps_addSnippet_response(TypedDict):
    snippet_id: int

class apps_created_group_response(TypedDict):
    group_id: int

apps_getCatalog_response: TypeAlias = 'objects.apps_catalog_list'

class apps_getFriendsList_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.users_user_full']

class apps_getFriendsList_response(TypedDict):
    count: int  # Total number
    items: List[int]

class apps_getLeaderboard_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.apps_leaderboard']
    profiles: NotRequired[List['objects.users_user']]

class apps_getLeaderboard_response(TypedDict):
    count: int  # Total number
    items: List['objects.apps_leaderboard']

class apps_getMiniAppPolicies_response(TypedDict):
    privacy_policy: NotRequired[str]  # URL of the app's privacy policy
    terms: NotRequired[str]  # URL of the app's terms

class apps_getScopes_response(TypedDict):
    count: int  # Total number
    items: List['objects.apps_scope']

apps_getScore_response: TypeAlias = int  # Score number

class apps_getSnippets_response(TypedDict):
    items: NotRequired[List['objects.apps_custom_snippet']]

apps_getTestingGroups_response: TypeAlias = List['objects.apps_testing_group']

class apps_get_response(TypedDict):
    count: int  # Total number of applications
    items: List['objects.apps_app']  # List of applications
    profiles: NotRequired[List['objects.users_user_full']]  # List of friends profiles, used only when return_friends=true
    groups: NotRequired[List['objects.groups_group_full']]  # List of groups, used only when extended=true

class apps_image_upload_response(TypedDict):
    hash: NotRequired[str]  # Uploading hash
    image: NotRequired[str]  # Uploaded photo data

class apps_isNotificationsAllowed_response(TypedDict):
    is_allowed: Flag  # Whether notifications are allowed for current user from concrete app or not

apps_sendRequest_response: TypeAlias = int  # Request ID

class appWidgets_getAppImageUploadServer_response(TypedDict):
    upload_url: NotRequired[str]  # To upload an image, generate POST-request to upload_url with a file in photo field. Then call appWidgets.saveAppImage method

appWidgets_getAppImages_response: TypeAlias = 'objects.appWidgets_photos'

class appWidgets_getGroupImageUploadServer_response(TypedDict):
    upload_url: NotRequired[str]  # To upload an image, generate POST-request to upload_url with a file in photo field. Then call appWidgets.saveAppImage method

appWidgets_getGroupImages_response: TypeAlias = 'objects.appWidgets_photos'

appWidgets_getImagesById_response: TypeAlias = List['objects.appWidgets_photo']

appWidgets_saveAppImage_response: TypeAlias = 'objects.appWidgets_photo'

appWidgets_saveGroupImage_response: TypeAlias = 'objects.appWidgets_photo'

asr_checkStatus_response: TypeAlias = 'objects.asr_task'

class asr_process_response(TypedDict):
    task_id: str  # ID of created task in UUID format.

class auth_restore_response(TypedDict):
    success: NotRequired[Literal[1]]  # 1 if success
    sid: NotRequired[str]  # Parameter needed to grant access by code

base_bool_response: TypeAlias = 'objects.base_bool_int'

base_getUploadServer_response: TypeAlias = 'objects.base_upload_server'

base_ok_response: TypeAlias = Literal[1]

base_undefined_response: TypeAlias = Dict[str, Any]

board_addTopic_response: TypeAlias = int  # Topic ID

board_createComment_response: TypeAlias = int  # Comment ID

class board_getComments_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.board_topic_comment']
    poll: NotRequired['objects.polls_poll']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']
    real_offset: NotRequired[int]  # Offset of comment

class board_getComments_response(TypedDict):
    count: int  # Total number
    items: List['objects.board_topic_comment']
    poll: NotRequired['objects.polls_poll']
    real_offset: NotRequired[int]  # Offset of comment

class board_getTopics_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.board_topic']
    default_order: 'objects.board_default_order'
    can_add_topics: 'objects.base_bool_int'  # Information whether current user can add topic
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']

class board_getTopics_response(TypedDict):
    count: int  # Total number
    items: List['objects.board_topic']
    default_order: 'objects.board_default_order'
    can_add_topics: 'objects.base_bool_int'  # Information whether current user can add topic

class bugtracker_addCompanyGroupsMembers_response(TypedDict):
    errors: List['objects.bugtracker_add_company_groups_members_error']

class bugtracker_addCompanyMembers_response(TypedDict):
    errors: List[str]

class bugtracker_createComment_response(TypedDict):
    comment: 'objects.bugtracker_comment'
    comment_flood: NotRequired[Flag]
    subscribe_state: NotRequired['objects.bugtracker_bugreport_subscribe_state']

class bugtracker_getBugreportById_response(TypedDict):
    bugreport: NotRequired['objects.bugtracker_bugreport']
    profiles: NotRequired[List['objects.users_user_full']]

class bugtracker_getCompanyGroupMembers_response(TypedDict):
    user_ids: List[int]
    profiles: NotRequired[List['objects.users_user_full']]

class bugtracker_getCompanyMembers_response(TypedDict):
    company_members: List['objects.bugtracker_company_member']
    count: int
    profiles: NotRequired[List['objects.users_user_full']]

class bugtracker_getDownloadVersionUrl_response(TypedDict):
    url: str
    app_title: NotRequired[str]
    bundle_name: NotRequired[str]
    build_id: NotRequired[int]
    build_name: NotRequired[str]
    build_title: NotRequired[str]

class calls_start_response(TypedDict):
    call_id: NotRequired[str]  # Call id
    join_link: str  # Join link
    ok_join_link: str  # OK join link
    broadcast_video_id: NotRequired[str]  # video id for link
    broadcast_ov_id: NotRequired[str]  # video id for streaming

class database_getChairs_response(TypedDict):
    count: int  # Total number
    items: List['objects.base_object']

database_getCitiesById_response: TypeAlias = List['objects.database_city_by_id']

class database_getCities_response(TypedDict):
    count: int  # Total number
    items: List['objects.database_city']

database_getCountriesById_response: TypeAlias = List['objects.base_country']

class database_getCountries_response(TypedDict):
    count: int  # Total number
    items: List['objects.base_country']

class database_getFaculties_response(TypedDict):
    count: int  # Total number
    items: List['objects.database_faculty']

database_getMetroStationsById_response: TypeAlias = List['objects.database_station']

class database_getMetroStations_response(TypedDict):
    count: int  # Total number
    items: List['objects.database_station']

class database_getRegions_response(TypedDict):
    count: int  # Total number
    items: List['objects.database_region']

database_getSchoolClasses_new_response: TypeAlias = List['objects.database_school_class']

class database_getSchools_response(TypedDict):
    count: int  # Total number
    items: List['objects.database_school']

class database_getUniversities_response(TypedDict):
    count: int  # Total number
    items: List['objects.database_university']

docs_add_response: TypeAlias = int  # Document ID

class docs_doc_upload_response(TypedDict):
    file: NotRequired[str]  # Uploaded file data

docs_getById_response: TypeAlias = List['objects.docs_doc']

class docs_getTypes_response(TypedDict):
    count: int  # Total number
    items: List['objects.docs_doc_types']

docs_getUploadServer_response: TypeAlias = 'objects.base_upload_server'

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

donut_getSubscription_response: TypeAlias = 'objects.donut_donator_subscription_info'

class donut_getSubscriptions_response(TypedDict):
    subscriptions: List['objects.donut_donator_subscription_info']
    count: NotRequired[int]
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

class downloadedGames_paid_status_response(TypedDict):
    is_paid: Flag  # Game has been paid

fave_addTag_response: TypeAlias = 'objects.fave_tag'

class fave_getPages_response(TypedDict):
    count: int
    items: List['objects.fave_page']

class fave_getTags_response(TypedDict):
    count: int
    items: List['objects.fave_tag']

class fave_get_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.fave_bookmark']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group']]

class fave_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.fave_bookmark']

class friends_addList_response(TypedDict):
    list_id: int  # List ID

friends_add_response: TypeAlias = Literal[1, 2, 4]  # Friend request status

friends_areFriends_extended_response: TypeAlias = List['objects.friends_friend_extended_status']

friends_areFriends_response: TypeAlias = List['objects.friends_friend_status']

class friends_delete_response(TypedDict):
    success: int
    friend_deleted: NotRequired[Literal[1]]  # Returns 1 if friend has been deleted
    out_request_deleted: NotRequired[Literal[1]]  # Returns 1 if out request has been canceled
    in_request_deleted: NotRequired[Literal[1]]  # Returns 1 if incoming request has been declined
    suggestion_deleted: NotRequired[Literal[1]]  # Returns 1 if suggestion has been declined

friends_getAppUsers_response: TypeAlias = List[int]

class friends_getLists_response(TypedDict):
    count: int  # Total number of friends lists
    items: List['objects.friends_friends_list']

friends_getMutual_response: TypeAlias = List[int]

friends_getMutual_target_uids_response: TypeAlias = List['objects.friends_mutual_friend']

friends_getMutual_total_count_response: TypeAlias = 'objects.friends_mutual_friend'

friends_getOnline_extended_response: TypeAlias = 'objects.friends_online_users'

friends_getOnline_online_mobile_extended_response: TypeAlias = 'objects.friends_online_users_with_mobile'

class friends_getOnline_online_mobile_response(TypedDict):
    online: List[int]
    online_mobile: List[int]

friends_getOnline_response: TypeAlias = List[int]

friends_getRecent_response: TypeAlias = List[int]

class friends_getRequests_extended_response(TypedDict):
    count: int  # Total requests number
    items: List['objects.friends_requests_xtr_message']
    count_unread: NotRequired[int]  # Total unread requests number
    last_viewed: NotRequired[int]  # Friend requests last viewed timestamp

class friends_getRequests_need_mutual_response(TypedDict):
    count: int  # Total requests number
    items: List['objects.friends_requests_xtr_mutual']
    count_unread: NotRequired[int]  # Total unread requests number
    last_viewed: NotRequired[int]  # Friend requests last viewed timestamp

class friends_getRequests_response(TypedDict):
    count: int  # Total requests number
    items: List[int]
    count_unread: NotRequired[int]  # Total unread requests number
    last_viewed: NotRequired[int]  # Friend requests last viewed timestamp

class friends_getSuggestions_response(TypedDict):
    count: int  # Total results number
    items: List['objects.users_user_full']

class friends_get_fields_response(TypedDict):
    count: int  # Total friends number
    items: List['objects.users_user_full']
    profiles: NotRequired[List['objects.users_user_full']]

class friends_get_response(TypedDict):
    count: int  # Total friends number
    items: List[int]

class friends_search_response(TypedDict):
    count: int  # Total number
    items: List['objects.users_user_full']

class gifts_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.gifts_gift']

groups_addAddress_response: TypeAlias = 'objects.groups_address'

class groups_addCallbackServer_response(TypedDict):
    server_id: int

groups_addLink_response: TypeAlias = 'objects.groups_links_item'

groups_create_response: TypeAlias = 'objects.groups_group_full'

groups_editAddress_response: TypeAlias = 'objects.groups_address'  # Result

class groups_getAddresses_response(TypedDict):
    count: int  # Total count of addresses
    items: List['objects.groups_address']

class groups_getBanned_response(TypedDict):
    count: int  # Total users number
    items: List['objects.groups_owner_xtr_ban_info']

class groups_getById_object_response(TypedDict):
    groups: NotRequired[List['objects.groups_group_full']]
    profiles: NotRequired[List['objects.groups_profile_item']]

class groups_getCallbackConfirmationCode_response(TypedDict):
    code: str  # Confirmation code

class groups_getCallbackServers_response(TypedDict):
    count: int
    items: List['objects.groups_callback_server']

groups_getCallbackSettings_response: TypeAlias = 'objects.groups_callback_settings'

class groups_getCatalogInfo_extended_response(TypedDict):
    enabled: 'objects.base_bool_int'  # Information whether catalog is enabled for current user
    categories: NotRequired[List['objects.groups_group_category_full']]

class groups_getCatalogInfo_response(TypedDict):
    enabled: 'objects.base_bool_int'  # Information whether catalog is enabled for current user
    categories: NotRequired[List['objects.groups_group_category']]

class groups_getInvitedUsers_response(TypedDict):
    count: int  # Total communities number
    items: List['objects.users_user_full']

class groups_getInvites_extended_response(TypedDict):
    count: int  # Total communities number
    items: List['objects.groups_group_full']
    profiles: List['objects.users_user_min']
    groups: List['objects.groups_group_full']

class groups_getInvites_response(TypedDict):
    count: int  # Total communities number
    items: List['objects.groups_group_full']

groups_getLongPollServer_response: TypeAlias = 'objects.groups_long_poll_server'

groups_getLongPollSettings_response: TypeAlias = 'objects.groups_long_poll_settings'

class groups_getMembers_fields_response(TypedDict):
    count: int  # Total members number
    items: List['objects.groups_user_xtr_role']
    next_from: NotRequired[str]  # Encoded string for a next page

class groups_getMembers_filter_response(TypedDict):
    count: int  # Total members number
    items: List['objects.groups_member_role']
    next_from: NotRequired[str]  # Encoded string for a next page

class groups_getMembers_response(TypedDict):
    count: int  # Total members number
    items: List[int]
    next_from: NotRequired[str]  # Encoded string for a next page

class groups_getOnlineStatus_response(TypedDict):
    minutes: NotRequired[int]  # Estimated time of answer (for status = answer_mark)
    status: 'objects.groups_online_status_type'

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
    recognize_photo: NotRequired[int]  # Photo suggests setting
    city_id: int  # City id of group
    city_name: str  # City name of group
    contacts: NotRequired['objects.base_bool_int']
    links: NotRequired['objects.base_bool_int']
    sections_list: NotRequired[List['objects.groups_sections_list_item']]
    main_section: NotRequired['objects.groups_group_full_section']
    secondary_section: NotRequired['objects.groups_group_full_section']
    age_limits: NotRequired['objects.groups_group_age_limits']
    description: str  # Community description
    docs: 'objects.groups_group_docs'  # Docs settings
    events: NotRequired['objects.base_bool_int']
    addresses: NotRequired[Flag]
    bots_capabilities: NotRequired['objects.base_bool_int']  # By enabling bot abilities, you can send users messages with a customized keyboard attached as well as use other promotional abilities
    bots_start_button: NotRequired['objects.base_bool_int']  # If this setting is enabled, users will see a Start button when they start a chat with your community for the first time
    bots_add_to_chat: NotRequired['objects.base_bool_int']  # If this setting is enabled then users can add your community to a chat
    obscene_filter: 'objects.base_bool_int'  # Information whether the obscene filter is enabled
    obscene_stopwords: 'objects.base_bool_int'  # Information whether the stop words filter is enabled
    obscene_words: List[str]  # The list of stop words
    toxic_filter: 'objects.base_bool_int'  # Information whether the toxic filter is enabled
    disable_replies_from_groups: 'objects.base_bool_int'  # Information whether the replies from groups is disabled
    event_group_id: NotRequired[int]
    photos: 'objects.groups_group_photos'  # Photos settings
    public_category: NotRequired[int]  # Information about the group category
    public_category_list: NotRequired[List['objects.groups_group_public_category_list']]
    public_date: NotRequired[str]
    public_date_label: NotRequired[str]
    public_subcategory: NotRequired[int]  # Information about the group subcategory
    rss: NotRequired[str]  # URL of the RSS feed
    start_date: NotRequired[int]  # Start date
    finish_date: NotRequired[int]  # Finish date in Unix-time format
    subject: NotRequired[int]  # Community subject ID
    subject_list: NotRequired[List['objects.groups_subject_item']]
    suggested_privacy: NotRequired['objects.groups_group_suggested_privacy']
    title: str  # Community title
    topics: 'objects.groups_group_topics'  # Topics settings
    twitter: NotRequired['objects.groups_settings_twitter']
    video: 'objects.groups_group_video'  # Video settings
    wall: 'objects.groups_group_wall'  # Wall settings
    website: NotRequired[str]  # Community website
    phone: NotRequired[str]  # Community phone
    email: NotRequired[str]  # Community email
    wiki: 'objects.groups_group_wiki'  # Wiki settings

groups_getTagList_response: TypeAlias = List['objects.groups_group_tag']

class groups_getTokenPermissions_response(TypedDict):
    mask: int
    permissions: List['objects.groups_token_permission_setting']

class groups_get_object_extended_response(TypedDict):
    count: int  # Total communities number
    items: List['objects.groups_group_full']

class groups_get_response(TypedDict):
    count: int  # Total communities number
    items: List[int]

class groups_invite_user_ids_list_response(TypedDict):
    invites_send_count: int  # Total invited users number

class groups_isMember_extended_response(TypedDict):
    member: 'objects.base_bool_int'  # Information whether user is a member of the group
    invitation: NotRequired['objects.base_bool_int']  # Information whether user has been invited to the group
    can_invite: NotRequired['objects.base_bool_int']  # Information whether user can be invited
    can_recall: NotRequired['objects.base_bool_int']  # Information whether user's invite to the group can be recalled
    request: NotRequired['objects.base_bool_int']  # Information whether user has sent request to the group

groups_isMember_user_ids_extended_response: TypeAlias = List['objects.groups_member_status_full']

groups_isMember_user_ids_response: TypeAlias = List['objects.groups_member_status']

class groups_search_response(TypedDict):
    count: int  # Total communities number
    items: List['objects.groups_group_full']

class leadForms_create_response(TypedDict):
    form_id: int
    url: str

class leadForms_delete_response(TypedDict):
    form_id: int

class leadForms_getLeads_response(TypedDict):
    leads: List['objects.leadForms_lead']
    next_page_token: NotRequired[str]

leadForms_get_response: TypeAlias = 'objects.leadForms_form'

leadForms_list_response: TypeAlias = List['objects.leadForms_form']

leadForms_uploadUrl_response: TypeAlias = str

class likes_add_response(TypedDict):
    likes: int  # Total likes number

class likes_delete_response(TypedDict):
    likes: int  # Total likes number

class likes_getList_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.users_subscriptions_item']
    liked_by_author: NotRequired['objects.users_subscriptions_item']  # Author of post if he liked the comment
    liked_by_group: NotRequired['objects.users_subscriptions_item']  # Group where post is present if they liked the comment

class likes_getList_response(TypedDict):
    count: int  # Total number
    items: List[int]

class likes_isLiked_response(TypedDict):
    liked: 'objects.base_bool_int'  # Information whether user liked the object
    copied: 'objects.base_bool_int'  # Information whether user reposted the object

class market_addAlbum_response(TypedDict):
    market_album_id: NotRequired[int]  # Album ID
    albums_count: NotRequired[int]  # Albums count

class market_addPropertyVariant_response(TypedDict):
    variant_id: int

class market_addProperty_response(TypedDict):
    property_id: int

class market_add_response(TypedDict):
    market_item_id: int  # Item ID

market_createComment_response: TypeAlias = int  # Comment ID

class market_getAlbumById_response(TypedDict):
    count: int  # Total number
    items: List['objects.market_market_album']

class market_getAlbums_response(TypedDict):
    count: int  # Total number
    items: List['objects.market_market_album']

class market_getById_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.market_market_item_full']

class market_getById_response(TypedDict):
    count: int  # Total number
    items: List['objects.market_market_item']

class market_getCategories_new_response(TypedDict):
    items: List['objects.market_market_category_tree']

class market_getComments_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_comment']
    profiles: NotRequired[List['objects.users_user_full']]  # List of users, available only if extended=true exists in query params
    groups: NotRequired[List['objects.groups_group_full']]  # List of groups, available only if extended=true exists in query params

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

class market_getProperties_response(TypedDict):
    items: List['objects.market_property']
    count: int

class market_get_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.market_market_item_full']
    variants: NotRequired[List['objects.market_market_item_full']]

class market_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.market_market_item']
    variants: NotRequired[List['objects.market_market_item']]

class market_groupItems_response(TypedDict):
    item_group_id: int

class market_photo_id_response(TypedDict):
    photo_id: int  # Photo ID
    photo: NotRequired['objects.photos_photo']

class market_search_basic_response(TypedDict):
    count: int  # Current chunk size
    total: int  # Total size
    has_more: NotRequired[Flag]  # Next chunk present
    items: List['objects.market_market_item_basic_with_group']

class market_search_extended_response(TypedDict):
    count: int  # Total number
    view_type: 'objects.market_services_view_type'
    items: List['objects.market_market_item_full']
    variants: NotRequired[List['objects.market_market_item_full']]

class market_search_response(TypedDict):
    count: int  # Total number
    view_type: 'objects.market_services_view_type'
    items: List['objects.market_market_item']
    variants: NotRequired[List['objects.market_market_item']]
    groups: NotRequired[List['objects.groups_group_full']]
    filters: NotRequired['objects.market_global_search_filters']

class messages_addChatUsers_response(TypedDict):
    failed_peer_ids: List[int]
    failed_phone_numbers: List[str]
    invitees: List[int]

class messages_createChat_withPeerIds_response(TypedDict):
    chat_id: NotRequired[int]  # Chat ID
    peer_ids: NotRequired[List[int]]  # List of successfully added peer ids

class messages_deleteChatPhoto_response(TypedDict):
    message_id: NotRequired[int]  # Service message ID
    chat: NotRequired['objects.messages_chat']

class messages_deleteConversation_response(TypedDict):
    last_deleted_id: int  # Id of the last message, that was deleted

messages_delete_full_response: TypeAlias = List['objects.messages_delete_full_response_item']

class messages_getByConversationMessageId_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_message']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

class messages_getByConversationMessageId_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_message']

class messages_getById_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_message']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

class messages_getById_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_message']

class messages_getChatPreview_response(TypedDict):
    preview: NotRequired['objects.messages_chat_preview']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

messages_getChat_chat_ids_fields_response: TypeAlias = List['objects.messages_chat_full']

messages_getChat_chat_ids_response: TypeAlias = List['objects.messages_chat']

messages_getChat_fields_response: TypeAlias = 'objects.messages_chat_full'

messages_getChat_response: TypeAlias = 'objects.messages_chat'

messages_getConversationMembers_response: TypeAlias = 'objects.messages_getConversationMembers'

messages_getConversationsById_extended_response: TypeAlias = 'objects.messages_getConversationById_extended'

messages_getConversationsById_response: TypeAlias = 'objects.messages_getConversationById'

class messages_getConversations_response(TypedDict):
    count: int  # Total number
    unread_count: NotRequired[int]  # Unread dialogs number
    items: List['objects.messages_conversation_with_message']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

class messages_getHistoryAttachments_response(TypedDict):
    items: List['objects.messages_history_attachment']
    next_from: NotRequired[str]  # Value for pagination
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

class messages_getHistory_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_message']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]
    conversations: NotRequired[List['objects.messages_conversation']]

class messages_getHistory_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_message']

class messages_getImportantMessages_extended_response(TypedDict):
    messages: 'objects.messages_messages_array'
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]
    conversations: NotRequired[List['objects.messages_conversation']]

class messages_getImportantMessages_response(TypedDict):
    messages: 'objects.messages_messages_array'
    profiles: NotRequired[List['objects.users_user']]
    groups: NotRequired[List['objects.groups_group_full']]
    conversations: NotRequired[List['objects.messages_conversation']]

class messages_getIntentUsers_response(TypedDict):
    count: int
    items: List[int]
    profiles: NotRequired[List['objects.users_user_full']]

class messages_getInviteLink_by_owner_response(TypedDict):
    items: List['objects.messages_getInviteLink_by_owner_response_item']

class messages_getInviteLink_response(TypedDict):
    link: NotRequired[str]

messages_getLastActivity_response: TypeAlias = 'objects.messages_last_activity'

class messages_getLongPollHistory_response(TypedDict):
    history: NotRequired[Union[str, int]]
    messages: NotRequired['objects.messages_longpoll_messages']
    credentials: NotRequired['objects.messages_longpoll_params']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]
    chats: NotRequired[List['objects.messages_chat']]
    new_pts: NotRequired[int]  # Persistence timestamp
    from_pts: NotRequired[int]
    more: NotRequired[Flag]  # Has more
    conversations: NotRequired[List['objects.messages_conversation']]

messages_getLongPollServer_response: TypeAlias = 'objects.messages_longpoll_params'

class messages_getMessagesReactions_response(TypedDict):
    items: List['objects.messages_reaction_counters_response_item']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

class messages_getReactedPeers_response(TypedDict):
    count: int  # Total number
    reactions: List['objects.messages_reaction_response_item']
    counters: List['objects.messages_reaction_counter_response_item']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

class messages_getReactionsAssets_response(TypedDict):
    version: int  # Current reactions assets version
    assets: List['objects.messages_reaction_asset_item']  # Base reactions assets to display by default
    override_assets: NotRequired[List['objects.messages_reaction_asset_item']]  # Extended reactions assets for special occasions, user allowed to switch to the base version

class messages_isMessagesFromGroupAllowed_response(TypedDict):
    is_allowed: NotRequired['objects.base_bool_int']

class messages_joinChatByInviteLink_response(TypedDict):
    chat_id: NotRequired[int]

messages_markAsImportant_deprecated_response: TypeAlias = List[int]

messages_pin_response: TypeAlias = 'objects.messages_pinned_message'

class messages_searchConversations_extended_response(TypedDict):
    count: int  # Total results number
    items: List['objects.messages_conversation']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

class messages_searchConversations_response(TypedDict):
    count: int  # Total results number
    items: List['objects.messages_conversation']

class messages_search_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_message']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]
    conversations: NotRequired[List['objects.messages_conversation']]

class messages_search_response(TypedDict):
    count: int  # Total number
    items: List['objects.messages_message']

messages_send_deprecated_response: TypeAlias = int  # Message ID

messages_send_user_ids_response: TypeAlias = List['objects.messages_send_user_ids_response_item']

class messages_setChatPhoto_response(TypedDict):
    message_id: NotRequired[int]  # Service message ID
    chat: NotRequired['objects.messages_chat']

class newsfeed_generic_response(TypedDict):
    items: List['objects.newsfeed_newsfeed_item']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']
    lives_items: NotRequired[List['objects.newsfeed_newsfeed_item']]

class newsfeed_getBanned_extended_response(TypedDict):
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

class newsfeed_getBanned_response(TypedDict):
    groups: NotRequired[List[int]]
    members: NotRequired[List[int]]

class newsfeed_getComments_response(TypedDict):
    items: List['objects.newsfeed_comments_item']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']
    next_from: NotRequired[str]  # Next from value

class newsfeed_getLists_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.newsfeed_list_full']

class newsfeed_getLists_response(TypedDict):
    count: int  # Total number
    items: List['objects.newsfeed_list']

class newsfeed_getMentions_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wallpost_full']

class newsfeed_getSuggestedSources_response(TypedDict):
    count: int  # Total number
    items: List['objects.users_subscriptions_item']

class newsfeed_ignore_item_response(TypedDict):
    status: Flag

newsfeed_saveList_response: TypeAlias = int  # List ID

class newsfeed_search_extended_response(TypedDict):
    items: List['objects.wall_wallpost_full']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]
    suggested_queries: NotRequired[List[str]]
    next_from: NotRequired[str]
    count: int  # Filtered number
    total_count: NotRequired[int]  # Total number

class newsfeed_search_extended_strict_response(TypedDict):
    items: List['objects.wall_wallpost_full']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]
    suggested_queries: NotRequired[List[str]]
    next_from: NotRequired[str]
    count: int  # Filtered number
    total_count: NotRequired[int]  # Total number

class newsfeed_search_response(TypedDict):
    items: List['objects.wall_wallpost_full']
    suggested_queries: NotRequired[List[str]]
    next_from: NotRequired[str]
    count: int  # Filtered number
    total_count: NotRequired[int]  # Total number

class newsfeed_search_strict_response(TypedDict):
    items: List['objects.wall_wallpost_full']
    suggested_queries: NotRequired[List[str]]
    next_from: NotRequired[str]
    count: int  # Filtered number
    total_count: NotRequired[int]  # Total number

notes_add_response: TypeAlias = int  # Note ID

notes_createComment_response: TypeAlias = int  # Comment ID

notes_getById_response: TypeAlias = 'objects.notes_note'

class notes_getComments_response(TypedDict):
    count: int  # Total number
    items: List['objects.notes_note_comment']

class notes_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.notes_note']

class notifications_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.notifications_notification_item']
    profiles: NotRequired[List['objects.users_user']]
    groups: NotRequired[List['objects.groups_group']]
    last_viewed: NotRequired[int]  # Time when user has been checked notifications last time
    photos: NotRequired[List['objects.photos_photo']]
    videos: NotRequired[List['objects.video_video_full']]
    apps: NotRequired[List['objects.apps_app']]
    next_from: NotRequired[str]
    ttl: NotRequired[int]

notifications_sendMessage_response: TypeAlias = List['objects.notifications_send_message_item']

orders_changeState_response: TypeAlias = str  # New state

orders_getAmount_response: TypeAlias = List['objects.orders_amount']

orders_getById_response: TypeAlias = List['objects.orders_order']

orders_getUserSubscriptionById_response: TypeAlias = 'objects.orders_subscription'

class orders_getUserSubscriptions_response(TypedDict):
    count: int  # Total number
    items: List['objects.orders_subscription']

orders_get_response: TypeAlias = List['objects.orders_order']

pages_getHistory_response: TypeAlias = List['objects.pages_wikipage_history']

pages_getTitles_response: TypeAlias = List['objects.pages_wikipage']

pages_getVersion_response: TypeAlias = 'objects.pages_wikipage_full'

pages_get_response: TypeAlias = 'objects.pages_wikipage_full'

pages_parseWiki_response: TypeAlias = str  # HTML source

pages_saveAccess_response: TypeAlias = int  # Page ID

pages_save_response: TypeAlias = int  # Page ID

photos_copy_response: TypeAlias = int  # Photo ID

photos_createAlbum_response: TypeAlias = 'objects.photos_photo_album_full'

photos_createComment_response: TypeAlias = int  # Created comment ID

photos_getAlbumsCount_response: TypeAlias = int  # Albums number

class photos_getAlbums_response(TypedDict):
    count: int  # Total number
    items: List['objects.photos_photo_album_full']

class photos_getAllComments_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_comment']

class photos_getAll_response(TypedDict):
    count: int  # Total number
    items: List['objects.photos_photo']
    more: NotRequired['objects.base_bool_int']  # Information whether next page is presented

photos_getById_response: TypeAlias = List['objects.photos_photo']

class photos_getComments_extended_response(TypedDict):
    count: int  # Total number
    real_offset: NotRequired[int]  # Real offset of the comments
    items: List['objects.wall_wall_comment']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']

class photos_getComments_response(TypedDict):
    count: int  # Total number
    real_offset: NotRequired[int]  # Real offset of the comments
    items: List['objects.wall_wall_comment']

photos_getMarketUploadServer_response: TypeAlias = 'objects.base_upload_server'

photos_getMessagesUploadServer_response: TypeAlias = 'objects.photos_photo_upload'

class photos_getNewTags_response(TypedDict):
    count: int  # Total number
    items: List['objects.photos_photo_xtr_tag_info']

photos_getTags_response: TypeAlias = List['objects.photos_photo_tag']

photos_getUploadServer_response: TypeAlias = 'objects.photos_photo_upload'

class photos_getUserPhotos_response(TypedDict):
    count: int  # Total number
    items: List['objects.photos_photo']
    next_from: NotRequired[str]  # next from pagination cursor

photos_getWallUploadServer_response: TypeAlias = 'objects.photos_photo_upload'

class photos_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.photos_photo']
    next_from: NotRequired[str]  # next from pagination cursor

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

class photos_owner_cover_upload_response(TypedDict):
    hash: NotRequired[str]  # Uploading hash
    photo: NotRequired[str]  # Uploaded photo data

class photos_owner_upload_response(TypedDict):
    hash: NotRequired[str]  # Uploading hash
    photo: NotRequired[str]  # Uploaded photo data
    server: NotRequired[int]  # Upload server number

class photos_photo_upload_response(TypedDict):
    aid: NotRequired[int]  # Album ID
    hash: NotRequired[str]  # Uploading hash
    photo: NotRequired[str]  # Uploaded photo data
    photos_list: NotRequired[str]  # Uploaded photos data
    server: NotRequired[int]  # Upload server number

photos_putTag_response: TypeAlias = int  # Created tag ID

photos_saveMarketAlbumPhoto_response: TypeAlias = List['objects.photos_photo']

photos_saveMarketPhoto_response: TypeAlias = List['objects.photos_photo']

photos_saveMessagesPhoto_response: TypeAlias = List['objects.photos_photo']

class photos_saveOwnerCoverPhoto_response(TypedDict):
    images: NotRequired[List['objects.base_image']]

class photos_saveOwnerPhoto_response(TypedDict):
    photo_hash: str  # Photo hash
    photo_src: str  # Uploaded image url
    photo_src_big: NotRequired[str]  # Uploaded image url
    photo_src_small: NotRequired[str]  # Uploaded image url
    saved: NotRequired[int]  # Returns 1 if profile photo is saved
    post_id: NotRequired[int]  # Created post ID

photos_saveWallPhoto_response: TypeAlias = List['objects.photos_photo']

photos_save_response: TypeAlias = List['objects.photos_photo']

class photos_search_response(TypedDict):
    count: int  # Total number
    items: List['objects.photos_photo']

class photos_wall_upload_response(TypedDict):
    hash: NotRequired[str]  # Uploading hash
    photo: NotRequired[str]  # Uploaded photo data
    server: NotRequired[int]  # Upload server number

class podcasts_searchPodcast_response(TypedDict):
    podcasts: List['objects.podcast_external_data']
    results_total: int  # Total amount of found results

polls_create_response: TypeAlias = 'objects.polls_poll'

polls_getBackgrounds_response: TypeAlias = List['objects.polls_background']

polls_getById_response: TypeAlias = 'objects.polls_poll_extended'

polls_getVoters_fields_response: TypeAlias = List['objects.polls_fields_voters']

polls_getVoters_response: TypeAlias = List['objects.polls_voters']

polls_savePhoto_response: TypeAlias = 'objects.polls_background'

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

prettyCards_getById_response: TypeAlias = List['objects.prettyCards_prettyCardOrError']

prettyCards_getUploadURL_response: TypeAlias = str  # Upload URL

class prettyCards_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.prettyCards_prettyCard']

class search_getHints_response(TypedDict):
    count: int
    items: List['objects.search_hint']
    suggested_queries: NotRequired[List[str]]

secure_checkToken_response: TypeAlias = 'objects.secure_token_checked'

secure_getAppBalance_response: TypeAlias = int  # App balance

secure_getSMSHistory_response: TypeAlias = List['objects.secure_sms_notification']

secure_getTransactionsHistory_response: TypeAlias = List['objects.secure_transaction']

secure_getUserLevel_response: TypeAlias = List['objects.secure_level']

secure_giveEventSticker_response: TypeAlias = List['objects.secure_giveEventSticker_item']

secure_sendNotification_response: TypeAlias = List[int]

secure_setCounter_array_response: TypeAlias = List['objects.secure_setCounter_item']

stats_getPostReach_response: TypeAlias = List['objects.stats_wallpost_stat']

stats_get_response: TypeAlias = List['objects.stats_period']

status_get_response: TypeAlias = 'objects.status_status'

storage_getKeys_response: TypeAlias = List[str]

storage_get_response: TypeAlias = List['objects.storage_value']

class store_getFavoriteStickers_response(TypedDict):
    count: int  # Count of favorite stickers
    items: List['objects.base_sticker_new']  # List of sticker objects

class store_getProducts_response(TypedDict):
    items: List['objects.store_product']
    count: int

class store_getStickersKeywords_response(TypedDict):
    count: int
    dictionary: List['objects.store_stickers_keyword']
    chunks_count: NotRequired[int]  # Total count of chunks to load
    chunks_hash: NotRequired[str]  # Chunks version hash

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

class stories_getPhotoUploadServer_response(TypedDict):
    upload_url: str  # Upload URL
    user_ids: List[int]  # Users ID who can to see story.

class stories_getStats_V5200_response(TypedDict):
    preview: NotRequired[str]
    achievement: NotRequired[str]
    achievement_subtitle: NotRequired[str]
    categories: NotRequired[List['objects.stories_stat_category']]
    need_privacy_block: NotRequired[Flag]

stories_getStats_response: TypeAlias = 'objects.stories_story_stats'

class stories_getVideoUploadServer_response(TypedDict):
    upload_url: str  # Upload URL
    user_ids: List[int]  # Users ID who can to see story.

class stories_getViewers_extended_V5115_response(TypedDict):
    count: int  # Viewers count
    items: List['objects.stories_viewers_item']
    hidden_reason: NotRequired[str]
    next_from: NotRequired[str]

class stories_get_V5113_response(TypedDict):
    count: int
    items: List['objects.stories_feed_item']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]
    need_upload_screen: NotRequired[Flag]
    track_code: NotRequired[str]
    next_from: NotRequired[str]

class stories_save_response(TypedDict):
    count: int
    items: List['objects.stories_story']
    profiles: NotRequired[List['objects.users_user']]
    groups: NotRequired[List['objects.groups_group_full']]

class stories_upload_response(TypedDict):
    upload_result: NotRequired[str]  # A string hash that is used in the stories.save method

class streaming_getServerUrl_response(TypedDict):
    endpoint: NotRequired[str]  # Server host
    key: NotRequired[str]  # Access key

streaming_getStats_response: TypeAlias = List['objects.streaming_stats']

class streaming_getStem_response(TypedDict):
    stem: NotRequired[str]  # part of a word responsible for its lexical meaning

class translations_translate_response(TypedDict):
    texts: NotRequired[List[str]]
    source_lang: NotRequired[str]

class users_getFollowers_fields_response(TypedDict):
    count: int  # Total number of available results
    friends_count: NotRequired[int]
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

users_get_response: TypeAlias = List['objects.users_user_full']

class users_search_response(TypedDict):
    count: int  # Total number of available results
    items: List['objects.users_user_full']

utils_checkLink_response: TypeAlias = 'objects.utils_link_checked'

class utils_getLastShortenedLinks_response(TypedDict):
    count: int  # Total number of available results
    items: List['objects.utils_last_shortened_link']

utils_getLinkStats_extended_response: TypeAlias = 'objects.utils_link_stats_extended'

utils_getLinkStats_response: TypeAlias = 'objects.utils_link_stats'

utils_getServerTime_response: TypeAlias = int  # Time as Unixtime

utils_getShortLink_response: TypeAlias = 'objects.utils_short_link'

utils_resolveScreenName_response: TypeAlias = 'objects.utils_domain_resolved'

class video_addAlbum_response(TypedDict):
    album_id: int  # Created album ID

video_changeVideoAlbums_response: TypeAlias = List[int]

video_createComment_response: TypeAlias = int  # Created comment ID

class video_edit_response(TypedDict):
    success: 'objects.base_bool_int'
    access_key: NotRequired[str]  # Access key for access link

video_getAlbumById_response: TypeAlias = 'objects.video_video_album_full'

class video_getAlbumsByVideo_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.video_video_album_full']

video_getAlbumsByVideo_response: TypeAlias = List[int]

class video_getAlbums_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.video_video_album_full']

class video_getAlbums_response(TypedDict):
    count: int  # Total number
    items: List['objects.video_video_album']

class video_getComments_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_comment']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']
    current_level_count: NotRequired[int]  # Count of replies of current level
    can_post: NotRequired[Flag]  # Information whether current user can comment the post
    show_reply_button: NotRequired[Flag]
    groups_can_post: NotRequired[Flag]  # Information whether groups can comment the post
    real_offset: NotRequired[int]

class video_getComments_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_comment']
    current_level_count: NotRequired[int]  # Count of replies of current level
    can_post: NotRequired[Flag]  # Information whether current user can comment the post
    show_reply_button: NotRequired[Flag]
    groups_can_post: NotRequired[Flag]  # Information whether groups can comment the post
    real_offset: NotRequired[int]

class video_getLongPollServer_response(TypedDict):
    url: str

class video_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.video_video_full']
    profiles: NotRequired[List['objects.users_user_full']]
    groups: NotRequired[List['objects.groups_group_full']]

video_liveGetCategories_response: TypeAlias = List['objects.video_live_category']

video_save_response: TypeAlias = 'objects.video_save_result'

class video_search_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.video_video_full']
    profiles: List['objects.users_user']
    groups: List['objects.groups_group_full']

class video_search_response(TypedDict):
    count: int  # Total number
    items: List['objects.video_video_full']

class video_startStreaming_response(TypedDict):
    owner_id: int  # Owner ID of created video object
    video_id: int  # Video ID of created video object
    name: str  # Video title
    description: str  # Video description
    access_key: str  # Video access key
    stream: 'objects.video_stream_input_params'
    post_id: NotRequired[int]

class video_stopStreaming_response(TypedDict):
    unique_viewers: NotRequired[int]

class video_upload_response(TypedDict):
    size: NotRequired[int]  # Video size
    video_id: NotRequired[int]  # Video ID

class wall_createComment_response(TypedDict):
    comment_id: int  # Created comment ID
    parents_stack: NotRequired[List[int]]

class wall_edit_response(TypedDict):
    post_id: int  # Edited post ID

class wall_getById_extended_response(TypedDict):
    items: List['objects.wall_wall_item']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']

class wall_getById_response(TypedDict):
    items: NotRequired[List['objects.wall_wall_item']]

class wall_getComment_extended_response(TypedDict):
    items: List['objects.wall_wall_comment']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']
    can_post: NotRequired[Flag]  # Information whether current user can comment the post
    show_reply_button: NotRequired[Flag]
    groups_can_post: NotRequired[Flag]  # Information whether groups can comment the post
    post_author_id: NotRequired[int]  # Author id of the comment's post

class wall_getComment_response(TypedDict):
    items: List['objects.wall_wall_comment']
    can_post: NotRequired[Flag]  # Information whether current user can comment the post
    show_reply_button: NotRequired[Flag]
    groups_can_post: NotRequired[Flag]  # Information whether groups can comment the post

class wall_getComments_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_comment']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']
    current_level_count: NotRequired[int]  # Count of replies of current level
    can_post: NotRequired[Flag]  # Information whether current user can comment the post
    show_reply_button: NotRequired[Flag]
    groups_can_post: NotRequired[Flag]  # Information whether groups can comment the post
    post_author_id: NotRequired[int]  # Author id of comments' post

class wall_getComments_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_comment']
    current_level_count: NotRequired[int]  # Count of replies of current level
    can_post: NotRequired[Flag]  # Information whether current user can comment the post
    show_reply_button: NotRequired[Flag]
    groups_can_post: NotRequired[Flag]  # Information whether groups can comment the post

class wall_getReposts_response(TypedDict):
    items: List['objects.wall_wallpost_full']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']

class wall_get_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_item']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']

class wall_get_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_item']

class wall_parseAttachedLink_response(TypedDict):
    data: List['objects.wall_wallpost_attachment']
    groups: NotRequired[List['objects.groups_group_full']]
    profiles: NotRequired[List['objects.users_user']]

class wall_postAdsStealth_response(TypedDict):
    post_id: int  # Created post ID

class wall_post_response(TypedDict):
    post_id: int  # Created post ID

class wall_repost_response(TypedDict):
    success: int
    post_id: int  # Created post ID
    reposts_count: int  # Reposts number
    wall_repost_count: NotRequired[int]  # Reposts to wall number
    mail_repost_count: NotRequired[int]  # Reposts to mail number
    likes_count: int  # Reposts number

class wall_search_extended_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_item']
    profiles: List['objects.users_user_full']
    groups: List['objects.groups_group_full']

class wall_search_response(TypedDict):
    count: int  # Total number
    items: List['objects.wall_wall_item']

class widgets_getComments_response(TypedDict):
    count: int  # Total number
    posts: List['objects.widgets_widget_comment']

class widgets_getPages_response(TypedDict):
    count: int  # Total number
    pages: List['objects.widgets_widget_page']

