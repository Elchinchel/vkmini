from typing import Any, Union, Literal, Optional, Protocol, overload

from typing_extensions import TypeAlias

from vkmini.types import objects, responses

class _VkMethod(Protocol):
    async def __call__(self, **kwargs) -> Any: ...

Flag: TypeAlias = int

account_fields_enum: TypeAlias = Literal['country', 'https_required', 'own_posts_default', 'no_wall_replies', 'intro', 'lang', 'audio_autoplay']
ads_fields_enum: TypeAlias = Literal['ads_count']
ads_stats_fields_enum: TypeAlias = Literal['views_times']
apps_vk_ref_enum: TypeAlias = Literal['snippet_im', 'snippet_post']
apps_platforms_enum: TypeAlias = Literal['mobile', 'web', 'mvk']
friends_filter_enum: TypeAlias = Literal['mutual', 'contacts', 'mutual_contacts']
messages_attachment_types_enum: TypeAlias = Literal['app_action_games', 'app_action_mini_apps', 'audio', 'audio_message', 'clip', 'doc', 'graffiti', 'link', 'market', 'photo', 'share', 'video', 'wall']
notifications_filters_enum: TypeAlias = Literal['wall', 'mentions', 'comments', 'likes', 'reposted', 'followers', 'friends']
video_privacy_enum: TypeAlias = Literal['0', '1', '2', '3']
video_filters_enum: TypeAlias = Literal['long', 'short', 'vimeo', 'vk', 'youtube']


class account:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def ban(self, *, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def changePassword(self, *, new_password: str, restore_sid: Optional[str] = None, change_password_hash: Optional[str] = None, old_password: Optional[str] = None, **kwargs: Any) -> 'responses.account_changePassword_response':
        '''Changes a user password after access is successfully restored with the [vk.ru/dev/auth.restore|auth.restore] method.'''

    async def getActiveOffers(self, *, offset: int = 0, count: int = 100, **kwargs: Any) -> 'responses.account_getActiveOffers_response':
        '''Returns a list of active ads (offers) which executed by the user will bring him/her respective number of votes to his balance in the application.'''

    async def getAppPermissions(self, *, user_id: Optional[int] = None, **kwargs: Any) -> 'responses.account_getAppPermissions_response':
        '''Gets settings of the user in this application.'''

    async def getBanned(self, *, offset: Optional[int] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, count: int = 20, **kwargs: Any) -> 'responses.account_getBanned_response':
        '''Returns a user's blacklist.'''

    async def getCounters(self, *, filter: Optional[Union['objects.account_counters_filter', str]] = None, **kwargs: Any) -> 'responses.account_getCounters_response':
        '''Returns non-null values of user counters.'''

    async def getInfo(self, *, fields: Optional[account_fields_enum] = None, **kwargs: Any) -> 'responses.account_getInfo_response':
        '''Returns current account info.'''

    async def getProfileInfo(self, **kwargs: Any) -> 'responses.account_getProfileInfo_response':
        '''Returns the current account info.'''

    async def getPushSettings(self, *, device_id: Optional[str] = None, **kwargs: Any) -> 'responses.account_getPushSettings_response':
        '''Gets settings of push notifications.'''

    async def registerDevice(self, *, token: str, device_id: str, device_model: Optional[str] = None, device_year: Optional[int] = None, system_version: Optional[str] = None, settings: Optional[str] = None, sandbox: Flag = 0, **kwargs: Any) -> 'responses.base_ok_response':
        '''Subscribes an iOS/Android/Windows Phone-based device to receive push notifications'''

    async def saveProfileInfo(self, *, first_name: Optional[str] = None, last_name: Optional[str] = None, maiden_name: Optional[str] = None, screen_name: Optional[str] = None, cancel_request_id: Optional[int] = None, sex: Optional[Literal[0, 1, 2]] = None, relation: Optional[Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]] = None, relation_partner_id: Optional[int] = None, bdate: Optional[str] = None, bdate_visibility: Optional[Literal[0, 1, 2]] = None, home_town: Optional[str] = None, country_id: Optional[int] = None, city_id: Optional[int] = None, status: Optional[str] = None, **kwargs: Any) -> 'responses.account_saveProfileInfo_response':
        '''Edits current profile info.'''

    async def setInfo(self, *, name: Optional[Literal['audio_autoplay', 'intro', 'no_wall_replies', 'own_posts_default']] = None, value: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows to edit the current account info.'''

    async def setOffline(self, **kwargs: Any) -> 'responses.base_ok_response':
        '''Marks a current user as offline.'''

    async def setOnline(self, *, voip: Optional[Flag] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Marks the current user as online for 15 minutes.'''

    async def setPushSettings(self, *, device_id: str, settings: Optional[str] = None, key: Optional[str] = None, value: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Change push settings.'''

    async def setSilenceMode(self, *, device_id: Optional[str] = None, time: Optional[int] = None, peer_id: Optional[int] = None, sound: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Mutes push notifications for the set period of time.'''

    async def unban(self, *, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def unregisterDevice(self, *, device_id: Optional[str] = None, sandbox: Flag = 0, **kwargs: Any) -> 'responses.base_ok_response':
        '''Unsubscribes a device from push notifications.'''

class ads:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def addOfficeUsers(self, *, account_id: int, data: str, **kwargs: Any) -> 'responses.ads_addOfficeUsers_response':
        '''Adds managers and/or supervisors to advertising account.'''

    async def checkLink(self, *, account_id: int, link_type: Literal['application', 'community', 'mobile_app', 'post', 'site', 'user', 'user_post', 'video'], link_url: str, campaign_id: Optional[int] = None, **kwargs: Any) -> 'responses.ads_checkLink_response':
        '''Allows to check the ad link.'''

    async def createAds(self, *, account_id: int, data: str, **kwargs: Any) -> 'responses.ads_createAds_response':
        '''Creates ads.'''

    async def createCampaigns(self, *, account_id: int, data: str, **kwargs: Any) -> 'responses.ads_createCampaigns_response':
        '''Creates advertising campaigns.'''

    async def createClients(self, *, account_id: int, data: str, **kwargs: Any) -> 'responses.ads_createClients_response':
        '''Creates clients of an advertising agency.'''

    async def createLookalikeRequest(self, *, account_id: int, source_type: str, client_id: Optional[int] = None, retargeting_group_id: Optional[int] = None, **kwargs: Any) -> 'responses.ads_createLookalikeRequest_response': ...

    async def createTargetGroup(self, *, account_id: int, name: str, lifetime: int, client_id: Optional[int] = None, target_pixel_id: Optional[int] = None, target_pixel_rules: Optional[str] = None, **kwargs: Any) -> 'responses.ads_createTargetGroup_response':
        '''Creates a group to re-target ads for users who visited advertiser's site (viewed information about the product, registered, etc.).'''

    async def createTargetPixel(self, *, account_id: int, name: str, category_id: int, client_id: Optional[int] = None, domain: Optional[str] = None, **kwargs: Any) -> 'responses.ads_createTargetPixel_response': ...

    async def deleteAds(self, *, account_id: int, ids: str, **kwargs: Any) -> 'responses.ads_deleteAds_response':
        '''Archives ads.'''

    async def deleteCampaigns(self, *, account_id: int, ids: str, **kwargs: Any) -> 'responses.ads_deleteCampaigns_response':
        '''Archives advertising campaigns.'''

    async def deleteClients(self, *, account_id: int, ids: str, **kwargs: Any) -> 'responses.ads_deleteClients_response':
        '''Archives clients of an advertising agency.'''

    async def deleteTargetGroup(self, *, account_id: int, target_group_id: int, client_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a retarget group.'''

    async def deleteTargetPixel(self, *, account_id: int, target_pixel_id: int, client_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_undefined_response': ...

    async def getAccounts(self, **kwargs: Any) -> 'responses.ads_getAccounts_response':
        '''Returns a list of advertising accounts.'''

    async def getAds(self, *, account_id: int, client_id: Optional[int] = None, include_deleted: Optional[Flag] = None, only_deleted: Optional[Flag] = None, campaign_ids: Optional[str] = None, ad_ids: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, **kwargs: Any) -> 'responses.ads_getAds_response':
        '''Returns number of ads.'''

    async def getAdsLayout(self, *, account_id: int, client_id: Optional[int] = None, include_deleted: Optional[Flag] = None, only_deleted: Optional[Flag] = None, campaign_ids: Optional[str] = None, ad_ids: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, **kwargs: Any) -> 'responses.ads_getAdsLayout_response':
        '''Returns descriptions of ad layouts.'''

    async def getAdsTargeting(self, *, account_id: int, client_id: Optional[int] = None, include_deleted: Optional[Flag] = None, only_deleted: Optional[Flag] = None, campaign_ids: Optional[str] = None, ad_ids: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, **kwargs: Any) -> 'responses.ads_getAdsTargeting_response':
        '''Returns ad targeting parameters.'''

    async def getBudget(self, *, account_id: int, **kwargs: Any) -> 'responses.ads_getBudget_response':
        '''Returns current budget of the advertising account.'''

    async def getCampaigns(self, *, account_id: int, client_id: Optional[int] = None, include_deleted: Optional[Flag] = None, campaign_ids: Optional[str] = None, fields: Optional[ads_fields_enum] = None, **kwargs: Any) -> 'responses.ads_getCampaigns_response':
        '''Returns a list of campaigns in an advertising account.'''

    async def getCategories(self, *, lang: Optional[str] = None, **kwargs: Any) -> 'responses.ads_getCategories_response':
        '''Returns a list of possible ad categories.'''

    async def getClients(self, *, account_id: int, **kwargs: Any) -> 'responses.ads_getClients_response':
        '''Returns a list of advertising agency's clients.'''

    async def getDemographics(self, *, account_id: int, ids_type: Literal['ad', 'campaign'], ids: str, period: Literal['day', 'month', 'overall'], date_from: str, date_to: str, **kwargs: Any) -> 'responses.ads_getDemographics_response':
        '''Returns demographics for ads or campaigns.'''

    async def getFloodStats(self, *, account_id: int, **kwargs: Any) -> 'responses.ads_getFloodStats_response':
        '''Returns information about current state of a counter - number of remaining runs of methods and time to the next counter nulling in seconds.'''

    async def getLookalikeRequests(self, *, account_id: int, client_id: Optional[int] = None, requests_ids: Optional[str] = None, offset: int = 0, limit: int = 10, sort_by: str = 'id', **kwargs: Any) -> 'responses.ads_getLookalikeRequests_response': ...

    async def getMusicians(self, *, artist_name: str, **kwargs: Any) -> 'responses.ads_getMusicians_response': ...

    async def getMusiciansByIds(self, *, ids: Union[int, str], **kwargs: Any) -> 'responses.ads_getMusicians_response': ...

    async def getOfficeUsers(self, *, account_id: int, **kwargs: Any) -> 'responses.ads_getOfficeUsers_response':
        '''Returns a list of managers and supervisors of advertising account.'''

    async def getPostsReach(self, *, account_id: int, ids_type: Literal['ad', 'campaign'], ids: str, **kwargs: Any) -> 'responses.ads_getPostsReach_response':
        '''Returns detailed statistics of promoted posts reach from campaigns and ads.'''

    async def getRejectionReason(self, *, account_id: int, ad_id: int, **kwargs: Any) -> 'responses.ads_getRejectionReason_response':
        '''Returns a reason of ad rejection for pre-moderation.'''

    async def getStatistics(self, *, account_id: int, ids_type: Literal['ad', 'campaign', 'client', 'office'], ids: str, period: Literal['day', 'month', 'overall', 'week', 'year'], date_from: str, date_to: str, stats_fields: Optional[ads_stats_fields_enum] = None, **kwargs: Any) -> 'responses.ads_getStatistics_response':
        '''Returns statistics of performance indicators for ads, campaigns, clients or the whole account.'''

    async def getSuggestions(self, *, section: Literal['browsers', 'cities', 'cities_regions', 'countries', 'districts', 'group_types', 'interest_categories', 'interest_categories_v2', 'interests', 'operators', 'positions', 'price_lists', 'regions', 'religions', 'schools', 'stations', 'streets', 'user_browsers', 'user_devices', 'user_operating_systems', 'user_os'], ids: Optional[str] = None, q: Optional[str] = None, country: Optional[int] = None, cities: Optional[str] = None, lang: Optional['objects.base_lang'] = None, **kwargs: Any) -> Union['responses.ads_getSuggestions_response', 'responses.ads_getSuggestions_regions_response', 'responses.ads_getSuggestions_cities_response', 'responses.ads_getSuggestions_schools_response']:
        '''Returns a set of auto-suggestions for various targeting parameters.'''

    async def getTargetGroups(self, *, account_id: int, client_id: Optional[int] = None, extended: Optional[Flag] = None, **kwargs: Any) -> 'responses.ads_getTargetGroups_response':
        '''Returns a list of target groups.'''

    async def getTargetPixels(self, *, account_id: int, client_id: Optional[int] = None, **kwargs: Any) -> 'responses.ads_getTargetPixels_response': ...

    async def getTargetingStats(self, *, account_id: int, link_url: str, client_id: Optional[int] = None, criteria: Optional[str] = None, ad_id: Optional[int] = None, ad_format: Optional[Literal[1, 2, 4, 7, 10, 6, 9, 11]] = None, ad_platform: Optional[str] = None, ad_platform_no_wall: Optional[str] = None, ad_platform_no_ad_network: Optional[str] = None, publisher_platforms: Optional[str] = None, link_domain: Optional[str] = None, need_precise: Optional[Flag] = None, impressions_limit_period: Optional[int] = None, **kwargs: Any) -> 'responses.ads_getTargetingStats_response':
        '''Returns the size of targeting audience, and also recommended values for CPC and CPM.'''

    async def getUploadURL(self, *, ad_format: Literal[1, 2, 4, 7, 10, 11], icon: Optional[int] = None, **kwargs: Any) -> 'responses.ads_getUploadURL_response':
        '''Returns URL to upload an ad photo to.'''

    async def getVideoUploadURL(self, **kwargs: Any) -> 'responses.ads_getVideoUploadURL_response':
        '''Returns URL to upload an ad video to.'''

    async def importTargetContacts(self, *, account_id: int, target_group_id: int, contacts: str, client_id: Optional[int] = None, **kwargs: Any) -> 'responses.ads_importTargetContacts_response':
        '''Imports a list of advertiser's contacts to count VK registered users against the target group.'''

    async def removeOfficeUsers(self, *, account_id: int, ids: str, **kwargs: Any) -> 'responses.ads_removeOfficeUsers_response':
        '''Removes managers and/or supervisors from advertising account.'''

    async def removeTargetContacts(self, *, account_id: int, target_group_id: int, contacts: str, client_id: Optional[int] = None, **kwargs: Any) -> 'responses.ads_removeTargetContacts_response': ...

    async def saveLookalikeRequestResult(self, *, account_id: int, request_id: int, level: int, client_id: Optional[int] = None, **kwargs: Any) -> 'responses.ads_saveLookalikeRequestResult_response': ...

    async def shareTargetGroup(self, *, account_id: int, target_group_id: int, client_id: Optional[int] = None, share_with_client_id: Optional[int] = None, **kwargs: Any) -> 'responses.ads_shareTargetGroup_response': ...

    async def updateAds(self, *, account_id: int, data: str, **kwargs: Any) -> 'responses.ads_updateAds_response':
        '''Edits ads.'''

    async def updateCampaigns(self, *, account_id: int, data: str, **kwargs: Any) -> 'responses.ads_updateCampaigns_response':
        '''Edits advertising campaigns.'''

    async def updateClients(self, *, account_id: int, data: str, **kwargs: Any) -> 'responses.ads_updateClients_response':
        '''Edits clients of an advertising agency.'''

    async def updateOfficeUsers(self, *, account_id: int, data: str, **kwargs: Any) -> 'responses.ads_updateOfficeUsers_response':
        '''Adds managers and/or supervisors to advertising account.'''

    async def updateTargetGroup(self, *, account_id: int, target_group_id: int, name: str, lifetime: int, client_id: Optional[int] = None, domain: Optional[str] = None, target_pixel_id: Optional[int] = None, target_pixel_rules: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits a retarget group.'''

    async def updateTargetPixel(self, *, account_id: int, target_pixel_id: int, name: str, category_id: int, client_id: Optional[int] = None, domain: Optional[str] = None, **kwargs: Any) -> 'responses.base_undefined_response': ...

class adsweb:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def getAdCategories(self, *, office_id: int, **kwargs: Any) -> 'responses.adsweb_getAdCategories_response': ...

    async def getAdUnitCode(self, **kwargs: Any) -> 'responses.adsweb_getAdUnitCode_response': ...

    async def getAdUnits(self, *, office_id: int, sites_ids: Optional[str] = None, ad_units_ids: Optional[str] = None, fields: Optional[str] = None, limit: Optional[int] = None, offset: int = 0, **kwargs: Any) -> 'responses.adsweb_getAdUnits_response': ...

    async def getFraudHistory(self, *, office_id: int, sites_ids: Optional[str] = None, limit: Optional[int] = None, offset: int = 0, **kwargs: Any) -> 'responses.adsweb_getFraudHistory_response': ...

    async def getSites(self, *, office_id: int, sites_ids: Optional[str] = None, fields: Optional[str] = None, limit: Optional[int] = None, offset: int = 0, **kwargs: Any) -> 'responses.adsweb_getSites_response': ...

    async def getStatistics(self, *, office_id: int, ids_type: str, ids: str, period: str, date_from: str, date_to: str, fields: Optional[str] = None, page_id: Optional[str] = None, limit: Optional[int] = None, **kwargs: Any) -> 'responses.adsweb_getStatistics_response': ...

class apps:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def addSnippet(self, *, vk_ref: Optional[apps_vk_ref_enum] = None, group_id: Optional[Union[int, str]] = None, hash: Optional[str] = None, snippet_id: Optional[int] = None, title: Optional[str] = None, description: Optional[str] = None, image_url: Optional[str] = None, small_image_url: Optional[str] = None, button: Optional[Literal['buy', 'buy_ticket', 'contact', 'create', 'enroll', 'fill', 'go', 'help', 'open', 'play']] = None, **kwargs: Any) -> 'responses.apps_addSnippet_response': ...

    async def addUsersToTestingGroup(self, *, user_ids: Union[int, str], group_id: int, **kwargs: Any) -> 'responses.base_bool_response': ...

    async def deleteAppRequests(self, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes all request notifications from the current app.'''

    async def deleteSnippet(self, *, id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def get(self, *, app_id: Optional[int] = None, app_ids: Optional[Union[int, str]] = None, fields: Optional[Union['objects.users_fields', str]] = None, name_case: Optional['objects.base_name_case'] = None, app_fields: Optional[Union['objects.apps_app_fields', str]] = None, platform: Literal['android', 'ios', 'web'] = 'web', extended: Flag = 0, return_friends: Flag = 0, **kwargs: Any) -> 'responses.apps_get_response':
        '''Returns applications data.'''

    async def getCatalog(self, *, sort: Optional[Literal['create_date', 'growth_rate', 'popular', 'popular_today', 'popular_week', 'visitors']] = None, offset: Optional[int] = None, platform: Optional[str] = None, extended: Optional[Flag] = None, return_friends: Optional[Flag] = None, fields: Optional[Union['objects.users_fields', str]] = None, name_case: Optional['objects.base_name_case'] = None, q: Optional[str] = None, genre_id: Optional[int] = None, filter: Optional[Literal['favorite', 'featured', 'installed', 'new']] = None, count: int = 100, **kwargs: Any) -> 'responses.apps_getCatalog_response':
        '''Returns a list of applications (apps) available to users in the App Catalog.'''

    async def getFriendsList(self, *, query: Optional[str] = None, extended: Flag = 0, count: int = 20, offset: int = 0, type: Literal['invite', 'request'] = 'invite', fields: Union['objects.users_fields', str] = 'photo_200', **kwargs: Any) -> Union['responses.apps_getFriendsList_response', 'responses.apps_getFriendsList_extended_response']:
        '''Creates friends list for requests and invites in current app.'''

    async def getLeaderboard(self, *, type: Literal['level', 'points', 'score'], extended: Flag = False, **kwargs: Any) -> Union['responses.apps_getLeaderboard_response', 'responses.apps_getLeaderboard_extended_response']:
        '''Returns players rating in the game.'''

    async def getMiniAppPolicies(self, *, app_id: int, **kwargs: Any) -> 'responses.apps_getMiniAppPolicies_response':
        '''Returns policies and terms given to a mini app.'''

    async def getScopes(self, *, type: Literal['group', 'user'] = 'user', **kwargs: Any) -> 'responses.apps_getScopes_response':
        '''Returns scopes for auth'''

    async def getScore(self, *, user_id: Optional[int] = None, **kwargs: Any) -> 'responses.apps_getScore_response':
        '''Returns user score in app'''

    async def getSnippets(self, **kwargs: Any) -> 'responses.apps_getSnippets_response': ...

    async def getTestingGroups(self, *, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.apps_getTestingGroups_response': ...

    async def isNotificationsAllowed(self, *, user_id: Optional[int] = None, **kwargs: Any) -> 'responses.apps_isNotificationsAllowed_response': ...

    async def promoHasActiveGift(self, *, promo_id: int, user_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_bool_response': ...

    async def promoUseGift(self, *, promo_id: int, user_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_bool_response': ...

    async def removeTestingGroup(self, *, group_id: int, **kwargs: Any) -> 'responses.base_bool_response': ...

    async def removeUsersFromTestingGroups(self, *, user_ids: Union[int, str], **kwargs: Any) -> 'responses.base_bool_response': ...

    async def sendRequest(self, *, user_id: int, text: Optional[str] = None, name: Optional[str] = None, key: Optional[str] = None, separate: Optional[Flag] = None, type: Literal['invite', 'request'] = 'request', **kwargs: Any) -> 'responses.apps_sendRequest_response':
        '''Sends a request to another user in an app that uses VK authorization.'''

    async def updateMetaForTestingGroup(self, *, webview: str, name: str, platforms: apps_platforms_enum, group_id: Optional[int] = None, user_ids: Optional[Union[int, str]] = None, **kwargs: Any) -> 'responses.apps_created_group_response': ...

class appWidgets:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def getAppImageUploadServer(self, *, image_type: Literal['160x160', '160x240', '24x24', '50x50', '510x128'], **kwargs: Any) -> 'responses.appWidgets_getAppImageUploadServer_response':
        '''Returns a URL for uploading a photo to the community collection for community app widgets'''

    async def getAppImages(self, *, offset: Optional[int] = None, image_type: Optional[Literal['160x160', '160x240', '24x24', '50x50', '510x128']] = None, count: int = 20, **kwargs: Any) -> 'responses.appWidgets_getAppImages_response':
        '''Returns an app collection of images for community app widgets'''

    async def getGroupImageUploadServer(self, *, image_type: Literal['160x160', '160x240', '24x24', '50x50', '510x128'], **kwargs: Any) -> 'responses.appWidgets_getGroupImageUploadServer_response':
        '''Returns a URL for uploading a photo to the community collection for community app widgets'''

    async def getGroupImages(self, *, offset: Optional[int] = None, image_type: Optional[Literal['160x160', '160x240', '24x24', '50x50', '510x128']] = None, count: int = 20, **kwargs: Any) -> 'responses.appWidgets_getGroupImages_response':
        '''Returns a community collection of images for community app widgets'''

    async def getImagesById(self, *, images: str, **kwargs: Any) -> 'responses.appWidgets_getImagesById_response':
        '''Returns an image for community app widgets by its ID'''

    async def saveAppImage(self, *, hash: str, image: str, **kwargs: Any) -> 'responses.appWidgets_saveAppImage_response':
        '''Allows to save image into app collection for community app widgets'''

    async def saveGroupImage(self, *, hash: str, image: str, **kwargs: Any) -> 'responses.appWidgets_saveGroupImage_response':
        '''Allows to save image into community collection for community app widgets'''

    async def update(self, *, code: str, type: Literal['compact_list', 'cover_list', 'donation', 'list', 'match', 'matches', 'table', 'text', 'tiles'], **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows to update community app widget'''

class asr:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def checkStatus(self, *, task_id: str, **kwargs: Any) -> 'responses.asr_checkStatus_response':
        '''Returns status of the task with provided `task_id`'''

    async def getUploadUrl(self, **kwargs: Any) -> 'responses.base_getUploadServer_response':
        '''Returns the server address to [vk.ru/dev/upload_files_2|upload audio files].'''

    async def process(self, *, audio: str, model: Literal['neutral', 'spontaneous'], **kwargs: Any) -> 'responses.asr_process_response':
        '''Starts ASR task on [vk.ru/dev/upload_files_2|uploaded audio file].'''

class auth:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def restore(self, *, phone: str, last_name: str, **kwargs: Any) -> 'responses.auth_restore_response':
        '''Allows to restore account access using a code received via SMS. " This method is only available for apps with [vk.ru/dev/auth_direct|Direct authorization] access. "'''

class board:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def addTopic(self, *, group_id: int, title: str, text: Optional[str] = None, from_group: Optional[Flag] = None, attachments: Optional[str] = None, **kwargs: Any) -> 'responses.board_addTopic_response':
        '''Creates a new topic on a community's discussion board.'''

    async def closeTopic(self, *, group_id: int, topic_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Closes a topic on a community's discussion board so that comments cannot be posted.'''

    async def createComment(self, *, group_id: int, topic_id: int, message: Optional[str] = None, attachments: Optional[str] = None, from_group: Optional[Flag] = None, sticker_id: Optional[int] = None, guid: Optional[str] = None, **kwargs: Any) -> 'responses.board_createComment_response':
        '''Adds a comment on a topic on a community's discussion board.'''

    async def deleteComment(self, *, group_id: int, topic_id: int, comment_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a comment on a topic on a community's discussion board.'''

    async def deleteTopic(self, *, group_id: int, topic_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a topic from a community's discussion board.'''

    async def editComment(self, *, group_id: int, topic_id: int, comment_id: int, message: Optional[str] = None, attachments: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits a comment on a topic on a community's discussion board.'''

    async def editTopic(self, *, group_id: int, topic_id: int, title: str, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits the title of a topic on a community's discussion board.'''

    async def fixTopic(self, *, group_id: int, topic_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Pins a topic (fixes its place) to the top of a community's discussion board.'''

    async def getComments(self, *, group_id: int, topic_id: int, need_likes: Optional[Flag] = None, start_comment_id: Optional[int] = None, offset: Optional[int] = None, extended: Optional[Flag] = None, sort: Optional[Literal['asc', 'desc']] = None, count: int = 20, **kwargs: Any) -> Union['responses.board_getComments_response', 'responses.board_getComments_extended_response']:
        '''Returns a list of comments on a topic on a community's discussion board.'''

    async def getTopics(self, *, group_id: int, topic_ids: Optional[Union[int, str]] = None, order: Optional[Literal[1, 2, -1, -2, 0]] = None, offset: Optional[int] = None, extended: Optional[Flag] = None, preview: Optional[Literal[1, 2, 0]] = None, count: int = 40, preview_length: int = 90, **kwargs: Any) -> Union['responses.board_getTopics_response', 'responses.board_getTopics_extended_response']:
        '''Returns a list of topics on a community's discussion board.'''

    async def openTopic(self, *, group_id: int, topic_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Re-opens a previously closed topic on a community's discussion board.'''

    async def restoreComment(self, *, group_id: int, topic_id: int, comment_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Restores a comment deleted from a topic on a community's discussion board.'''

    async def unfixTopic(self, *, group_id: int, topic_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Unpins a pinned topic from the top of a community's discussion board.'''

class bugtracker:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def addCompanyGroupsMembers(self, *, company_id: int, user_ids: Union[int, str], company_group_ids: Union[int, str], **kwargs: Any) -> 'responses.bugtracker_addCompanyGroupsMembers_response': ...

    async def addCompanyMembers(self, *, user_ids: Union[int, str], company_id: int, **kwargs: Any) -> 'responses.bugtracker_addCompanyMembers_response': ...

    async def changeBugreportStatus(self, *, bugreport_id: int, status: Optional[int] = None, comment: Optional[str] = None, from_statuses: Optional[Union[int, str]] = None, not_in_statuses: Optional[Union[int, str]] = None, **kwargs: Any) -> 'responses.base_bool_response': ...

    async def createComment(self, *, bugreport_id: int, text: Optional[str] = None, hidden: Optional[Flag] = None, force: Optional[Flag] = None, **kwargs: Any) -> 'responses.bugtracker_createComment_response':
        '''Creates the comment to bugreport'''

    async def getBugreportById(self, *, bugreport_id: int, extended: Optional[Flag] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, **kwargs: Any) -> 'responses.bugtracker_getBugreportById_response':
        '''Returns extended bugreport data'''

    async def getCompanyGroupMembers(self, *, company_id: int, company_group_id: int, extended: Optional[Flag] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, count: int = 10, offset: int = 0, filter_name: str = '', **kwargs: Any) -> 'responses.bugtracker_getCompanyGroupMembers_response': ...

    async def getCompanyMembers(self, *, company_id: int, filter_role: Optional[Literal[0, 1]] = None, extended: Optional[Flag] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, count: int = 10, offset: int = 0, filter_name: str = '', filter_not_group: int = 0, filter_member_ids: Union[int, str] = '', extra: Flag = False, **kwargs: Any) -> 'responses.bugtracker_getCompanyMembers_response': ...

    async def getDownloadVersionUrl(self, *, product_id: int, version_id: int, ttl: int = 600, **kwargs: Any) -> 'responses.bugtracker_getDownloadVersionUrl_response': ...

    async def getProductBuildUploadServer(self, *, product_id: int, **kwargs: Any) -> 'responses.base_getUploadServer_response': ...

    async def removeCompanyGroupMember(self, *, company_id: int, user_id: int, company_group_id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def removeCompanyMember(self, *, user_id: int, company_id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def saveProductVersion(self, *, title: str, product_id: Optional[int] = None, release_notes: Optional[str] = None, visible: Optional[Flag] = None, version_id: int = 0, set_rft: Flag = False, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def setCompanyMemberRole(self, *, user_id: int, company_id: int, role: Literal[0, 1], **kwargs: Any) -> 'responses.base_ok_response': ...

    async def setProductIsOver(self, *, product_id: int, is_over: Optional[Flag] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

class calls:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def forceFinish(self, *, call_id: str, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def start(self, *, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.calls_start_response': ...

class database:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def getChairs(self, *, faculty_id: int, offset: Optional[int] = None, count: int = 100, **kwargs: Any) -> 'responses.database_getChairs_response':
        '''Returns list of chairs on a specified faculty.'''

    async def getCities(self, *, region_id: Optional[int] = None, q: Optional[str] = None, need_all: Optional[Flag] = None, offset: Optional[int] = None, count: int = 100, **kwargs: Any) -> 'responses.database_getCities_response':
        '''Returns a list of cities.'''

    async def getCitiesById(self, *, city_ids: Optional[Union[int, str]] = None, **kwargs: Any) -> 'responses.database_getCitiesById_response':
        '''Returns information about cities by their IDs.'''

    async def getCountries(self, *, need_all: Optional[Flag] = None, code: Optional[str] = None, offset: Optional[int] = None, count: int = 100, **kwargs: Any) -> 'responses.database_getCountries_response':
        '''Returns a list of countries.'''

    async def getCountriesById(self, *, country_ids: Optional[Union[int, str]] = None, **kwargs: Any) -> 'responses.database_getCountriesById_response':
        '''Returns information about countries by their IDs.'''

    async def getFaculties(self, *, university_id: int, offset: Optional[int] = None, count: int = 100, **kwargs: Any) -> 'responses.database_getFaculties_response':
        '''Returns a list of faculties (i.e., university departments).'''

    async def getMetroStations(self, *, city_id: int, offset: Optional[int] = None, count: int = 100, extended: Flag = False, **kwargs: Any) -> 'responses.database_getMetroStations_response':
        '''Get metro stations by city'''

    async def getMetroStationsById(self, *, station_ids: Optional[Union[int, str]] = None, **kwargs: Any) -> 'responses.database_getMetroStationsById_response':
        '''Get metro station by his id'''

    async def getRegions(self, *, q: Optional[str] = None, offset: Optional[int] = None, count: int = 100, **kwargs: Any) -> 'responses.database_getRegions_response':
        '''Returns a list of regions.'''

    async def getSchoolClasses(self, *, country_id: Optional[int] = None, **kwargs: Any) -> 'responses.database_getSchoolClasses_new_response':
        '''Returns a list of school classes specified for the country.'''

    async def getSchools(self, *, city_id: int, q: Optional[str] = None, offset: Optional[int] = None, count: int = 100, **kwargs: Any) -> 'responses.database_getSchools_response':
        '''Returns a list of schools.'''

    async def getUniversities(self, *, q: Optional[str] = None, city_id: Optional[int] = None, offset: Optional[int] = None, count: int = 100, **kwargs: Any) -> 'responses.database_getUniversities_response':
        '''Returns a list of higher education institutions.'''

class docs:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def add(self, *, owner_id: int, doc_id: int, access_key: Optional[str] = None, **kwargs: Any) -> 'responses.docs_add_response':
        '''Copies a document to a user's or community's document list.'''

    async def delete(self, *, owner_id: int, doc_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a user or community document.'''

    async def edit(self, *, doc_id: int, title: str, owner_id: Optional[int] = None, tags: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits a document.'''

    async def get(self, *, count: Optional[int] = None, offset: Optional[int] = None, owner_id: Optional[int] = None, type: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8] = 0, return_tags: Flag = False, **kwargs: Any) -> 'responses.docs_get_response':
        '''Returns detailed information about user or community documents.'''

    async def getById(self, *, docs: str, return_tags: Flag = False, **kwargs: Any) -> 'responses.docs_getById_response':
        '''Returns information about documents by their IDs.'''

    async def getMessagesUploadServer(self, *, peer_id: Optional[int] = None, type: Literal['audio_message', 'doc', 'graffiti'] = 'doc', **kwargs: Any) -> 'responses.docs_getUploadServer_response':
        '''Returns the server address for document upload.'''

    async def getTypes(self, *, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.docs_getTypes_response':
        '''Returns documents types available for current user.'''

    async def getUploadServer(self, *, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.docs_getUploadServer_response':
        '''Returns the server address for document upload.'''

    async def getWallUploadServer(self, *, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_getUploadServer_response':
        '''Returns the server address for document upload onto a user's or community's wall.'''

    async def restore(self, *, owner_id: int, doc_id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def save(self, *, file: str, title: Optional[str] = None, tags: Optional[str] = None, return_tags: Flag = False, **kwargs: Any) -> 'responses.docs_save_response':
        '''Saves a document after [vk.ru/dev/upload_files_2|uploading it to a server].'''

    async def search(self, *, q: Optional[str] = None, search_own: Optional[Flag] = None, offset: Optional[int] = None, return_tags: Optional[Flag] = None, count: int = 20, **kwargs: Any) -> 'responses.docs_search_response':
        '''Returns a list of documents matching the search criteria.'''

class donut:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def getFriends(self, *, owner_id: int, fields: Optional[str] = None, offset: int = 0, count: int = 10, **kwargs: Any) -> 'responses.groups_getMembers_fields_response': ...

    async def getSubscription(self, *, owner_id: int, **kwargs: Any) -> 'responses.donut_getSubscription_response': ...

    async def getSubscriptions(self, *, fields: Optional[Union['objects.base_user_group_fields', str]] = None, offset: int = 0, count: int = 10, **kwargs: Any) -> 'responses.donut_getSubscriptions_response':
        '''Returns a list of user's VK Donut subscriptions.'''

    async def isDon(self, *, owner_id: int, **kwargs: Any) -> 'responses.base_bool_response': ...

class downloadedGames:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def getPaidStatus(self, *, user_id: Optional[int] = None, **kwargs: Any) -> 'responses.downloadedGames_paid_status_response': ...

class fave:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def addArticle(self, *, url: str, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def addLink(self, *, link: str, **kwargs: Any) -> 'responses.base_ok_response':
        '''Adds a link to user faves.'''

    async def addPage(self, *, user_id: Optional[int] = None, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def addPost(self, *, owner_id: int, id: int, access_key: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def addProduct(self, *, owner_id: int, id: int, access_key: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def addTag(self, *, name: Optional[str] = None, position: Literal['back', 'front'] = 'back', **kwargs: Any) -> 'responses.fave_addTag_response': ...

    async def addVideo(self, *, owner_id: int, id: int, access_key: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def editTag(self, *, id: int, name: str, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def get(self, *, item_type: Optional[Literal['article', 'clip', 'game', 'link', 'mini_app', 'narrative', 'page', 'podcast', 'post', 'product', 'video', 'youla_product']] = None, tag_id: Optional[int] = None, offset: Optional[int] = None, fields: Optional[str] = None, is_from_snackbar: Optional[Flag] = None, extended: Flag = False, count: int = 50, **kwargs: Any) -> Union['responses.fave_get_response', 'responses.fave_get_extended_response']: ...

    async def getPages(self, *, offset: Optional[int] = None, type: Optional[Literal['groups', 'hints', 'users']] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, tag_id: Optional[int] = None, count: int = 50, **kwargs: Any) -> 'responses.fave_getPages_response': ...

    async def getTags(self, **kwargs: Any) -> 'responses.fave_getTags_response': ...

    async def markSeen(self, **kwargs: Any) -> 'responses.base_bool_response': ...

    async def removeArticle(self, *, owner_id: int, article_id: int, **kwargs: Any) -> 'responses.base_bool_response': ...

    async def removeLink(self, *, link_id: Optional[str] = None, link: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Removes link from the user's faves.'''

    async def removePage(self, *, user_id: Optional[int] = None, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def removePost(self, *, owner_id: int, id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def removeProduct(self, *, owner_id: int, id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def removeTag(self, *, id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def removeVideo(self, *, owner_id: int, id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def reorderTags(self, *, ids: Union[int, str], **kwargs: Any) -> 'responses.base_ok_response': ...

    async def setPageTags(self, *, user_id: Optional[int] = None, group_id: Optional[int] = None, tag_ids: Optional[Union[int, str]] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def setTags(self, *, item_type: Optional[Literal['article', 'clip', 'game', 'link', 'mini_app', 'narrative', 'page', 'podcast', 'post', 'product', 'video', 'youla_product']] = None, item_owner_id: Optional[int] = None, item_id: Optional[int] = None, tag_ids: Optional[Union[int, str]] = None, link_id: Optional[str] = None, link_url: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def trackPageInteraction(self, *, user_id: Optional[int] = None, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

class friends:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def add(self, *, user_id: Optional[int] = None, text: Optional[str] = None, follow: Optional[Flag] = None, **kwargs: Any) -> 'responses.friends_add_response':
        '''Approves or creates a friend request.'''

    async def addList(self, *, name: str, user_ids: Optional[Union[int, str]] = None, **kwargs: Any) -> 'responses.friends_addList_response':
        '''Creates a new friend list for the current user.'''

    async def areFriends(self, *, user_ids: Union[int, str], need_sign: Optional[Flag] = None, extended: Optional[Flag] = None, **kwargs: Any) -> Union['responses.friends_areFriends_response', 'responses.friends_areFriends_extended_response']:
        '''Checks the current user's friendship status with other specified users.'''

    async def delete(self, *, user_id: Optional[int] = None, **kwargs: Any) -> 'responses.friends_delete_response':
        '''Declines a friend request or deletes a user from the current user's friend list.'''

    async def deleteAllRequests(self, **kwargs: Any) -> 'responses.base_ok_response':
        '''Marks all incoming friend requests as viewed.'''

    async def deleteList(self, *, list_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a friend list of the current user.'''

    async def edit(self, *, user_id: int, list_ids: Optional[Union[int, str]] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits the friend lists of the selected user.'''

    async def editList(self, *, list_id: int, name: Optional[str] = None, user_ids: Optional[Union[int, str]] = None, add_user_ids: Optional[Union[int, str]] = None, delete_user_ids: Optional[Union[int, str]] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits a friend list of the current user.'''

    @overload
    async def get(self, *, fields: Union['objects.users_fields', str], user_id: Optional[int] = None, order: Optional[Literal['hints', 'mobile', 'name', 'random', 'smart']] = None, list_id: Optional[int] = None, offset: Optional[int] = None, ref: Optional[str] = None, count: int = 5000, **kwargs: Any) -> 'responses.friends_get_fields_response': ...
    @overload
    async def get(self, *, user_id: Optional[int] = None, order: Optional[Literal['hints', 'mobile', 'name', 'random', 'smart']] = None, list_id: Optional[int] = None, offset: Optional[int] = None, fields: Optional[None] = None, ref: Optional[str] = None, count: int = 5000, **kwargs: Any) -> Union['responses.friends_get_response', 'responses.friends_get_fields_response']:
        '''Returns a list of user IDs or detailed information about a user's friends.'''

    async def getAppUsers(self, **kwargs: Any) -> 'responses.friends_getAppUsers_response':
        '''Returns a list of IDs of the current user's friends who installed the application.'''

    async def getLists(self, *, user_id: Optional[int] = None, return_system: Optional[Flag] = None, **kwargs: Any) -> 'responses.friends_getLists_response':
        '''Returns a list of the user's friend lists.'''

    async def getMutual(self, *, source_uid: Optional[int] = None, target_uid: Optional[int] = None, target_uids: Optional[Union[int, str]] = None, order: Optional[str] = None, count: Optional[int] = None, offset: Optional[int] = None, need_common_count: Optional[Flag] = None, **kwargs: Any) -> Union['responses.friends_getMutual_response', 'responses.friends_getMutual_target_uids_response', 'responses.friends_getMutual_total_count_response']:
        '''Returns a list of user IDs of the mutual friends of two users.'''

    async def getOnline(self, *, user_id: Optional[int] = None, list_id: Optional[int] = None, online_mobile: Optional[Flag] = None, order: Optional[str] = None, count: Optional[int] = None, offset: Optional[int] = None, **kwargs: Any) -> Union['responses.friends_getOnline_response', 'responses.friends_getOnline_online_mobile_response', 'responses.friends_getOnline_extended_response', 'responses.friends_getOnline_online_mobile_extended_response']:
        '''Returns a list of user IDs of a user's friends who are online.'''

    async def getRecent(self, *, count: int = 100, **kwargs: Any) -> 'responses.friends_getRecent_response':
        '''Returns a list of user IDs of the current user's recently added friends.'''

    async def getRequests(self, *, offset: Optional[int] = None, extended: Optional[Flag] = None, need_mutual: Optional[Flag] = None, out: Optional[Flag] = None, sort: Optional[Literal[0, 1, 2]] = None, suggested: Optional[Flag] = None, ref: Optional[str] = None, fields: Optional[Union['objects.users_fields', str]] = None, count: int = 100, need_viewed: Flag = 0, **kwargs: Any) -> Union['responses.friends_getRequests_response', 'responses.friends_getRequests_need_mutual_response', 'responses.friends_getRequests_extended_response']:
        '''Returns information about the current user's incoming and outgoing friend requests.'''

    async def getSuggestions(self, *, filter: Optional[friends_filter_enum] = None, offset: Optional[int] = None, fields: Optional[Union['objects.users_fields', str]] = None, name_case: Optional['objects.base_name_case'] = None, count: int = 100, **kwargs: Any) -> 'responses.friends_getSuggestions_response':
        '''Returns a list of profiles of users whom the current user may know.'''

    async def search(self, *, user_id: Optional[int] = None, q: Optional[str] = None, fields: Optional[Union['objects.users_fields', str]] = None, name_case: Optional['objects.base_name_case'] = None, offset: Optional[int] = None, count: int = 20, **kwargs: Any) -> 'responses.friends_search_response':
        '''Returns a list of friends matching the search criteria.'''

class gifts:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def get(self, *, user_id: Optional[int] = None, count: Optional[int] = None, offset: Optional[int] = None, **kwargs: Any) -> 'responses.gifts_get_response':
        '''Returns a list of user gifts.'''

class groups:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def addAddress(self, *, group_id: int, title: str, address: str, city_id: int, latitude: float, longitude: float, additional_address: Optional[str] = None, metro_id: Optional[int] = None, phone: Optional[str] = None, timetable: Optional[str] = None, is_main_address: Optional[Flag] = None, work_info_status: 'objects.groups_address_work_info_status' = 'no_information', **kwargs: Any) -> 'responses.groups_addAddress_response': ...

    async def addCallbackServer(self, *, group_id: int, url: str, title: str, secret_key: Optional[str] = None, **kwargs: Any) -> 'responses.groups_addCallbackServer_response': ...

    async def addLink(self, *, group_id: int, link: str, text: Optional[str] = None, **kwargs: Any) -> 'responses.groups_addLink_response':
        '''Allows to add a link to the community.'''

    async def approveRequest(self, *, group_id: int, user_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows to approve join request to the community.'''

    async def ban(self, *, group_id: int, owner_id: Optional[int] = None, end_date: Optional[int] = None, reason: Optional[int] = None, comment: Optional[str] = None, comment_visible: Optional[Flag] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def create(self, *, title: str, description: Optional[str] = None, public_category: Optional[int] = None, public_subcategory: Optional[int] = None, subtype: Optional[Literal[0, 1, 2, 3, 4]] = None, type: Literal['event', 'group', 'public'] = 'group', **kwargs: Any) -> 'responses.groups_create_response':
        '''Creates a new community.'''

    async def deleteAddress(self, *, group_id: int, address_id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def deleteCallbackServer(self, *, group_id: int, server_id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def deleteLink(self, *, group_id: int, link_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows to delete a link from the community.'''

    async def disableOnline(self, *, group_id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def edit(self, *, group_id: int, title: Optional[str] = None, description: Optional[str] = None, screen_name: Optional[str] = None, access: Optional['objects.groups_group_access'] = None, website: Optional[str] = None, subject: Optional['objects.groups_group_subject'] = None, email: Optional[str] = None, phone: Optional[str] = None, rss: Optional[str] = None, event_start_date: Optional[int] = None, event_finish_date: Optional[int] = None, event_group_id: Optional[int] = None, public_category: Optional[int] = None, public_subcategory: Optional[int] = None, public_date: Optional[str] = None, wall: Optional['objects.groups_group_wall'] = None, topics: Optional['objects.groups_group_topics'] = None, photos: Optional['objects.groups_group_photos'] = None, video: Optional['objects.groups_group_video'] = None, audio: Optional['objects.groups_group_audio'] = None, links: Optional[Flag] = None, events: Optional[Flag] = None, places: Optional[Flag] = None, contacts: Optional[Flag] = None, docs: Optional['objects.groups_group_docs'] = None, wiki: Optional['objects.groups_group_wiki'] = None, messages: Optional[Flag] = None, articles: Optional[Flag] = None, addresses: Optional[Flag] = None, market: Optional[Flag] = None, market_buttons: Optional[str] = None, market_comments: Optional[Flag] = None, market_country: Optional[Union[int, str]] = None, market_city: Optional[Union[int, str]] = None, market_currency: Optional['objects.groups_group_market_currency'] = None, market_contact: Optional[int] = None, market_wiki: Optional[int] = None, obscene_filter: Optional[Flag] = None, obscene_stopwords: Optional[Flag] = None, toxic_filter: Optional[Flag] = None, disable_replies_from_groups: Optional[Flag] = None, obscene_words: Optional[str] = None, main_section: Optional[int] = None, secondary_section: Optional[int] = None, country: Optional[int] = None, city: Optional[int] = None, age_limits: 'objects.groups_group_age_limits' = 1, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits a community.'''

    async def editAddress(self, *, group_id: int, address_id: int, title: Optional[str] = None, address: Optional[str] = None, additional_address: Optional[str] = None, city_id: Optional[int] = None, metro_id: Optional[int] = None, latitude: Optional[float] = None, longitude: Optional[float] = None, phone: Optional[str] = None, work_info_status: Optional['objects.groups_address_work_info_status'] = None, timetable: Optional[str] = None, is_main_address: Optional[Flag] = None, **kwargs: Any) -> 'responses.groups_editAddress_response': ...

    async def editCallbackServer(self, *, group_id: int, server_id: int, url: str, title: str, secret_key: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def editLink(self, *, group_id: int, link_id: int, text: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows to edit a link in the community.'''

    async def editManager(self, *, group_id: int, user_id: int, role: Optional['objects.groups_group_role'] = None, is_call_operator: Optional[Flag] = None, is_contact: Optional[Flag] = None, contact_position: Optional[str] = None, contact_phone: Optional[str] = None, contact_email: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows to add, remove or edit the community manager.'''

    async def enableOnline(self, *, group_id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def get(self, *, user_id: Optional[int] = None, extended: Optional[Flag] = None, filter: Optional[Union['objects.groups_filter', str]] = None, fields: Optional[Union['objects.groups_fields', str]] = None, offset: Optional[int] = None, count: Optional[int] = None, **kwargs: Any) -> Union['responses.groups_get_response', 'responses.groups_get_object_extended_response']:
        '''Returns a list of the communities to which a user belongs.'''

    async def getAddresses(self, *, group_id: int, address_ids: Optional[Union[int, str]] = None, latitude: Optional[float] = None, longitude: Optional[float] = None, offset: Optional[int] = None, fields: Optional[Union['objects.address_fields', str]] = None, count: int = 10, **kwargs: Any) -> 'responses.groups_getAddresses_response':
        '''Returns a list of community addresses.'''

    async def getBanned(self, *, group_id: int, offset: Optional[int] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, owner_id: Optional[int] = None, count: int = 20, **kwargs: Any) -> 'responses.groups_getBanned_response':
        '''Returns a list of users on a community blacklist.'''

    async def getById(self, *, group_ids: Optional[Union[int, str]] = None, group_id: Optional[Union[int, str]] = None, fields: Optional[Union['objects.groups_fields', str]] = None, **kwargs: Any) -> 'responses.groups_getById_object_response':
        '''Returns information about communities by their IDs.'''

    async def getCallbackConfirmationCode(self, *, group_id: int, **kwargs: Any) -> 'responses.groups_getCallbackConfirmationCode_response':
        '''Returns Callback API confirmation code for the community.'''

    async def getCallbackServers(self, *, group_id: int, server_ids: Optional[Union[int, str]] = None, **kwargs: Any) -> 'responses.groups_getCallbackServers_response': ...

    async def getCallbackSettings(self, *, group_id: int, server_id: Optional[int] = None, **kwargs: Any) -> 'responses.groups_getCallbackSettings_response':
        '''Returns [vk.ru/dev/callback_api|Callback API] notifications settings.'''

    async def getCatalogInfo(self, *, extended: Flag = 0, subcategories: Flag = 0, **kwargs: Any) -> Union['responses.groups_getCatalogInfo_response', 'responses.groups_getCatalogInfo_extended_response']:
        '''Returns categories list for communities catalog'''

    async def getInvitedUsers(self, *, group_id: int, offset: Optional[int] = None, fields: Optional[Union['objects.users_fields', str]] = None, name_case: Optional['objects.base_name_case'] = None, count: int = 20, **kwargs: Any) -> 'responses.groups_getInvitedUsers_response':
        '''Returns invited users list of a community'''

    async def getInvites(self, *, offset: Optional[int] = None, extended: Optional[Flag] = None, count: int = 20, **kwargs: Any) -> Union['responses.groups_getInvites_response', 'responses.groups_getInvites_extended_response']:
        '''Returns a list of invitations to join communities and events.'''

    async def getLongPollServer(self, *, group_id: int, **kwargs: Any) -> 'responses.groups_getLongPollServer_response':
        '''Returns the data needed to query a Long Poll server for events'''

    async def getLongPollSettings(self, *, group_id: int, **kwargs: Any) -> 'responses.groups_getLongPollSettings_response':
        '''Returns Long Poll notification settings'''

    @overload
    async def getMembers(self, *, fields: Union['objects.users_fields', str], group_id: Optional[Union[int, str]] = None, offset: Optional[int] = None, filter: Optional[Literal['donut', 'friends', 'managers', 'unsure']] = None, sort: Literal['id_asc', 'id_desc', 'time_asc', 'time_desc'] = 'id_asc', count: int = 1000, **kwargs: Any) -> 'responses.groups_getMembers_fields_response': ...
    @overload
    async def getMembers(self, *, group_id: Optional[Union[int, str]] = None, offset: Optional[int] = None, fields: Optional[None] = None, filter: Optional[Literal['donut', 'friends', 'managers', 'unsure']] = None, sort: Literal['id_asc', 'id_desc', 'time_asc', 'time_desc'] = 'id_asc', count: int = 1000, **kwargs: Any) -> Union['responses.groups_getMembers_response', 'responses.groups_getMembers_fields_response', 'responses.groups_getMembers_filter_response']:
        '''Returns a list of community members.'''

    async def getOnlineStatus(self, *, group_id: int, **kwargs: Any) -> 'responses.groups_getOnlineStatus_response': ...

    @overload
    async def getRequests(self, *, group_id: int, fields: Union['objects.users_fields', str], offset: Optional[int] = None, count: int = 20, **kwargs: Any) -> 'responses.groups_getRequests_fields_response': ...
    @overload
    async def getRequests(self, *, group_id: int, offset: Optional[int] = None, fields: Optional[None] = None, count: int = 20, **kwargs: Any) -> Union['responses.groups_getRequests_response', 'responses.groups_getRequests_fields_response']:
        '''Returns a list of requests to the community.'''

    async def getSettings(self, *, group_id: Union[int, str], **kwargs: Any) -> 'responses.groups_getSettings_response':
        '''Returns community settings.'''

    async def getTagList(self, *, group_id: int, **kwargs: Any) -> 'responses.groups_getTagList_response':
        '''List of group's tags'''

    async def getTokenPermissions(self, **kwargs: Any) -> 'responses.groups_getTokenPermissions_response': ...

    async def invite(self, *, group_id: int, user_id: Optional[int] = None, user_ids_list: Optional[Union[int, str]] = None, **kwargs: Any) -> Union['responses.base_ok_response', 'responses.groups_invite_user_ids_list_response']:
        '''Allows to invite friends to the community.'''

    async def isMember(self, *, group_id: Union[int, str], user_id: Optional[int] = None, user_ids: Optional[Union[int, str]] = None, extended: Optional[Flag] = None, **kwargs: Any) -> Union['responses.base_bool_response', 'responses.groups_isMember_user_ids_response', 'responses.groups_isMember_extended_response', 'responses.groups_isMember_user_ids_extended_response']:
        '''Returns information specifying whether a user is a member of a community.'''

    async def join(self, *, group_id: int, not_sure: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''With this method you can join the group or public page, and also confirm your participation in an event.'''

    async def leave(self, *, group_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''With this method you can leave a group, public page, or event.'''

    async def removeUser(self, *, group_id: int, user_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Removes a user from the community.'''

    async def reorderLink(self, *, group_id: int, link_id: int, after: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows to reorder links in the community.'''

    async def search(self, *, q: str, type: Optional[Literal['event', 'group', 'page']] = None, country_id: Optional[int] = None, city_id: Optional[int] = None, future: Optional[Flag] = None, market: Optional[Flag] = None, sort: Optional[Literal[0, 1, 2, 3, 4, 5, 6]] = None, offset: Optional[int] = None, count: int = 20, **kwargs: Any) -> 'responses.groups_search_response':
        '''Returns a list of communities matching the search criteria.'''

    async def setCallbackSettings(self, *, group_id: int, server_id: Optional[int] = None, api_version: Optional[str] = None, message_new: Optional[Flag] = None, message_reply: Optional[Flag] = None, message_allow: Optional[Flag] = None, message_edit: Optional[Flag] = None, message_deny: Optional[Flag] = None, message_typing_state: Optional[Flag] = None, message_read: Optional[Flag] = None, photo_new: Optional[Flag] = None, audio_new: Optional[Flag] = None, video_new: Optional[Flag] = None, wall_reply_new: Optional[Flag] = None, wall_reply_edit: Optional[Flag] = None, wall_reply_delete: Optional[Flag] = None, wall_reply_restore: Optional[Flag] = None, wall_post_new: Optional[Flag] = None, wall_repost: Optional[Flag] = None, wall_schedule_post_new: Optional[Flag] = None, wall_schedule_post_delete: Optional[Flag] = None, board_post_new: Optional[Flag] = None, board_post_edit: Optional[Flag] = None, board_post_restore: Optional[Flag] = None, board_post_delete: Optional[Flag] = None, photo_comment_new: Optional[Flag] = None, photo_comment_edit: Optional[Flag] = None, photo_comment_delete: Optional[Flag] = None, photo_comment_restore: Optional[Flag] = None, video_comment_new: Optional[Flag] = None, video_comment_edit: Optional[Flag] = None, video_comment_delete: Optional[Flag] = None, video_comment_restore: Optional[Flag] = None, market_comment_new: Optional[Flag] = None, market_comment_edit: Optional[Flag] = None, market_comment_delete: Optional[Flag] = None, market_comment_restore: Optional[Flag] = None, market_order_new: Optional[Flag] = None, market_order_edit: Optional[Flag] = None, poll_vote_new: Optional[Flag] = None, group_join: Optional[Flag] = None, group_leave: Optional[Flag] = None, group_change_settings: Optional[Flag] = None, group_change_photo: Optional[Flag] = None, group_officers_edit: Optional[Flag] = None, user_block: Optional[Flag] = None, user_unblock: Optional[Flag] = None, lead_forms_new: Optional[Flag] = None, like_add: Optional[Flag] = None, like_remove: Optional[Flag] = None, message_event: Optional[Flag] = None, message_reaction_event: Optional[Flag] = None, donut_subscription_create: Optional[Flag] = None, donut_subscription_prolonged: Optional[Flag] = None, donut_subscription_cancelled: Optional[Flag] = None, donut_subscription_price_changed: Optional[Flag] = None, donut_subscription_expired: Optional[Flag] = None, donut_money_withdraw: Optional[Flag] = None, donut_money_withdraw_error: Optional[Flag] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Allow to set notifications settings for group.'''

    async def setLongPollSettings(self, *, group_id: int, enabled: Optional[Flag] = None, api_version: Optional[str] = None, message_new: Optional[Flag] = None, message_reply: Optional[Flag] = None, message_allow: Optional[Flag] = None, message_deny: Optional[Flag] = None, message_edit: Optional[Flag] = None, message_typing_state: Optional[Flag] = None, message_read: Optional[Flag] = None, photo_new: Optional[Flag] = None, audio_new: Optional[Flag] = None, video_new: Optional[Flag] = None, wall_reply_new: Optional[Flag] = None, wall_reply_edit: Optional[Flag] = None, wall_reply_delete: Optional[Flag] = None, wall_reply_restore: Optional[Flag] = None, wall_post_new: Optional[Flag] = None, wall_repost: Optional[Flag] = None, board_post_new: Optional[Flag] = None, board_post_edit: Optional[Flag] = None, board_post_restore: Optional[Flag] = None, board_post_delete: Optional[Flag] = None, photo_comment_new: Optional[Flag] = None, photo_comment_edit: Optional[Flag] = None, photo_comment_delete: Optional[Flag] = None, photo_comment_restore: Optional[Flag] = None, video_comment_new: Optional[Flag] = None, video_comment_edit: Optional[Flag] = None, video_comment_delete: Optional[Flag] = None, video_comment_restore: Optional[Flag] = None, market_comment_new: Optional[Flag] = None, market_comment_edit: Optional[Flag] = None, market_comment_delete: Optional[Flag] = None, market_comment_restore: Optional[Flag] = None, poll_vote_new: Optional[Flag] = None, group_join: Optional[Flag] = None, group_leave: Optional[Flag] = None, group_change_settings: Optional[Flag] = None, group_change_photo: Optional[Flag] = None, group_officers_edit: Optional[Flag] = None, user_block: Optional[Flag] = None, user_unblock: Optional[Flag] = None, like_add: Optional[Flag] = None, like_remove: Optional[Flag] = None, message_event: Optional[Flag] = None, message_reaction_event: Optional[Flag] = None, donut_subscription_create: Optional[Flag] = None, donut_subscription_prolonged: Optional[Flag] = None, donut_subscription_cancelled: Optional[Flag] = None, donut_subscription_price_changed: Optional[Flag] = None, donut_subscription_expired: Optional[Flag] = None, donut_money_withdraw: Optional[Flag] = None, donut_money_withdraw_error: Optional[Flag] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Sets Long Poll notification settings'''

    async def setSettings(self, *, group_id: int, messages: Optional[Flag] = None, bots_capabilities: Optional[Flag] = None, bots_start_button: Optional[Flag] = None, bots_add_to_chat: Optional[Flag] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def setUserNote(self, *, group_id: int, user_id: int, note: Optional[str] = None, **kwargs: Any) -> 'responses.base_bool_response':
        '''In order to save note about group participant'''

    async def tagAdd(self, *, group_id: int, tag_name: str, tag_color: Optional[Literal['454647', '45678f', '4bb34b', '5181b8', '539b9c', '5c9ce6', '63b9ba', '6bc76b', '76787a', '792ec0', '7a6c4f', '7ececf', '9e8d6b', 'a162de', 'aaaeb3', 'bbaa84', 'e64646', 'ff5c5c', 'ffa000', 'ffc107']] = None, **kwargs: Any) -> 'responses.base_bool_response':
        '''Add new group's tag'''

    async def tagBind(self, *, group_id: int, tag_id: int, user_id: int, act: Literal['bind', 'unbind'], **kwargs: Any) -> 'responses.base_bool_response':
        '''Bind or unbind group's tag to user'''

    async def tagDelete(self, *, group_id: int, tag_id: int, **kwargs: Any) -> 'responses.base_bool_response':
        '''Delete group's tag'''

    async def tagUpdate(self, *, group_id: int, tag_id: int, tag_name: str, **kwargs: Any) -> 'responses.base_bool_response':
        '''Update group's tag'''

    async def toggleMarket(self, *, group_id: int, state: 'objects.groups_market_state', ref: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def unban(self, *, group_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

class leadForms:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def create(self, *, group_id: int, name: str, title: str, description: str, questions: str, policy_link_url: str, photo: Optional[str] = None, confirmation: Optional[str] = None, site_link_url: Optional[str] = None, pixel_code: Optional[str] = None, notify_admins: Optional[Union[int, str]] = None, notify_emails: Optional[str] = None, active: Flag = 0, once_per_user: Flag = 0, **kwargs: Any) -> 'responses.leadForms_create_response': ...

    async def delete(self, *, group_id: int, form_id: int, **kwargs: Any) -> 'responses.leadForms_delete_response': ...

    async def get(self, *, group_id: int, form_id: int, **kwargs: Any) -> 'responses.leadForms_get_response': ...

    async def getLeads(self, *, group_id: int, form_id: int, next_page_token: Optional[str] = None, limit: int = 10, **kwargs: Any) -> 'responses.leadForms_getLeads_response': ...

    async def getUploadURL(self, **kwargs: Any) -> 'responses.leadForms_uploadUrl_response': ...

    async def list(self, *, group_id: int, **kwargs: Any) -> 'responses.leadForms_list_response': ...

    async def update(self, *, group_id: int, form_id: int, name: str, title: str, description: str, questions: str, policy_link_url: str, photo: Optional[str] = None, confirmation: Optional[str] = None, site_link_url: Optional[str] = None, pixel_code: Optional[str] = None, notify_admins: Optional[Union[int, str]] = None, notify_emails: Optional[str] = None, active: Flag = 0, once_per_user: Flag = 0, **kwargs: Any) -> 'responses.leadForms_create_response': ...

class likes:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def add(self, *, type: 'objects.likes_type', item_id: int, owner_id: Optional[int] = None, access_key: Optional[str] = None, from_group: Optional[Flag] = None, **kwargs: Any) -> 'responses.likes_add_response':
        '''Adds the specified object to the 'Likes' list of the current user.'''

    async def delete(self, *, type: 'objects.likes_type', item_id: int, owner_id: Optional[int] = None, access_key: Optional[str] = None, from_group: Optional[Flag] = None, **kwargs: Any) -> 'responses.likes_delete_response':
        '''Deletes the specified object from the 'Likes' list of the current user.'''

    async def getList(self, *, type: 'objects.likes_type', owner_id: Optional[int] = None, item_id: Optional[int] = None, page_url: Optional[str] = None, filter: Optional[Literal['copies', 'likes']] = None, extended: Optional[Flag] = None, offset: Optional[int] = None, count: Optional[int] = None, skip_own: Optional[Flag] = None, fields: Optional[str] = None, friends_only: Literal[0, 1, 2, 3] = 0, **kwargs: Any) -> Union['responses.likes_getList_response', 'responses.likes_getList_extended_response']:
        '''Returns a list of IDs of users who added the specified object to their 'Likes' list.'''

    async def isLiked(self, *, type: 'objects.likes_type', item_id: int, user_id: Optional[int] = None, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.likes_isLiked_response':
        '''Checks for the object in the 'Likes' list of the specified user.'''

class market:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def add(self, *, owner_id: int, name: str, description: str, category_id: int, price: Optional[float] = None, old_price: Optional[float] = None, deleted: Optional[Flag] = None, main_photo_id: Optional[int] = None, photo_ids: Optional[Union[int, str]] = None, video_ids: Optional[Union[int, str]] = None, url: Optional[str] = None, variant_ids: Optional[Union[int, str]] = None, is_main_variant: Optional[Flag] = None, dimension_width: Optional[int] = None, dimension_height: Optional[int] = None, dimension_length: Optional[int] = None, weight: Optional[int] = None, sku: Optional[str] = None, stock_amount: Optional[int] = None, **kwargs: Any) -> 'responses.market_add_response':
        '''Ads a new item to the market.'''

    async def addAlbum(self, *, owner_id: int, title: str, photo_id: Optional[int] = None, main_album: Optional[Flag] = None, is_hidden: Optional[Flag] = None, **kwargs: Any) -> 'responses.market_addAlbum_response':
        '''Creates new collection of items'''

    async def addProperty(self, *, group_id: int, title: str, **kwargs: Any) -> 'responses.market_addProperty_response':
        '''Adds property'''

    async def addPropertyVariant(self, *, group_id: int, property_id: int, title: str, **kwargs: Any) -> 'responses.market_addPropertyVariant_response':
        '''Adds property variant'''

    async def addToAlbum(self, *, owner_id: int, item_ids: Union[int, str], album_ids: Union[int, str], **kwargs: Any) -> 'responses.base_ok_response':
        '''Adds an item to one or multiple collections.'''

    async def createComment(self, *, owner_id: int, item_id: int, message: Optional[str] = None, attachments: Optional[str] = None, from_group: Optional[Flag] = None, reply_to_comment: Optional[int] = None, sticker_id: Optional[int] = None, guid: Optional[str] = None, **kwargs: Any) -> 'responses.market_createComment_response':
        '''Creates a new comment for an item.'''

    async def delete(self, *, owner_id: int, item_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes an item.'''

    async def deleteAlbum(self, *, owner_id: int, album_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a collection of items.'''

    async def deleteComment(self, *, owner_id: int, comment_id: int, **kwargs: Any) -> 'responses.base_bool_response':
        '''Deletes an item's comment'''

    async def deleteProperty(self, *, group_id: int, property_id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def deletePropertyVariant(self, *, group_id: int, variant_id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def edit(self, *, owner_id: int, item_id: int, name: Optional[str] = None, description: Optional[str] = None, category_id: Optional[int] = None, price: Optional[float] = None, old_price: Optional[float] = None, deleted: Optional[Flag] = None, main_photo_id: Optional[int] = None, photo_ids: Optional[Union[int, str]] = None, video_ids: Optional[Union[int, str]] = None, url: Optional[str] = None, variant_ids: Optional[Union[int, str]] = None, is_main_variant: Optional[Flag] = None, dimension_width: Optional[int] = None, dimension_height: Optional[int] = None, dimension_length: Optional[int] = None, weight: Optional[int] = None, sku: Optional[str] = None, stock_amount: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits an item.'''

    async def editAlbum(self, *, owner_id: int, album_id: int, title: str, photo_id: Optional[int] = None, main_album: Optional[Flag] = None, is_hidden: Optional[Flag] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits a collection of items'''

    async def editComment(self, *, owner_id: int, comment_id: int, message: Optional[str] = None, attachments: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Chages item comment's text'''

    async def editOrder(self, *, user_id: int, order_id: int, merchant_comment: Optional[str] = None, status: Optional[int] = None, track_number: Optional[str] = None, payment_status: Optional[Literal['not_paid', 'paid', 'returned']] = None, delivery_price: Optional[int] = None, width: Optional[int] = None, length: Optional[int] = None, height: Optional[int] = None, weight: Optional[int] = None, comment_for_user: Optional[str] = None, receipt_link: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edit order'''

    async def editProperty(self, *, group_id: int, property_id: int, title: str, **kwargs: Any) -> 'responses.base_ok_response':
        '''Adds property'''

    async def editPropertyVariant(self, *, group_id: int, variant_id: int, title: str, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edit property variant name'''

    async def filterCategories(self, *, category_id: Optional[int] = None, query: Optional[str] = None, count: int = 20, **kwargs: Any) -> 'responses.market_getCategories_new_response':
        '''Returns a filter list of market categories.'''

    async def get(self, *, owner_id: int, offset: Optional[int] = None, extended: Optional[Flag] = None, date_from: Optional[str] = None, date_to: Optional[str] = None, need_variants: Optional[Flag] = None, with_disabled: Optional[Flag] = None, fields: Optional[str] = None, album_id: int = 0, count: int = 100, **kwargs: Any) -> Union['responses.market_get_response', 'responses.market_get_extended_response']:
        '''Returns items list for a community.'''

    async def getAlbumById(self, *, owner_id: int, album_ids: Union[int, str], **kwargs: Any) -> 'responses.market_getAlbumById_response':
        '''Returns items album's data'''

    async def getAlbums(self, *, owner_id: int, offset: Optional[int] = None, count: int = 50, **kwargs: Any) -> 'responses.market_getAlbums_response':
        '''Returns community's market collections list.'''

    async def getById(self, *, item_ids: str, extended: Optional[Flag] = None, **kwargs: Any) -> Union['responses.market_getById_response', 'responses.market_getById_extended_response']:
        '''Returns information about market items by their ids.'''

    async def getCategories(self, *, group_id: Optional[int] = None, album_id: Optional[int] = None, **kwargs: Any) -> 'responses.market_getCategories_new_response':
        '''Returns a list of market categories.'''

    async def getComments(self, *, owner_id: int, item_id: int, need_likes: Optional[Flag] = None, start_comment_id: Optional[int] = None, extended: Optional[Flag] = None, fields: Optional[Union['objects.users_fields', str]] = None, offset: int = 0, count: int = 20, sort: Literal['asc', 'desc'] = 'asc', **kwargs: Any) -> 'responses.market_getComments_response':
        '''Returns comments list for an item.'''

    async def getGroupOrders(self, *, group_id: Optional[Union[int, str]] = None, offset: int = 0, count: int = 10, **kwargs: Any) -> 'responses.market_getGroupOrders_response':
        '''Get market orders'''

    async def getOrderById(self, *, order_id: int, user_id: Optional[int] = None, extended: Optional[Flag] = None, **kwargs: Any) -> 'responses.market_getOrderById_response':
        '''Get order'''

    async def getOrderItems(self, *, order_id: int, user_id: Optional[int] = None, offset: Optional[int] = None, count: int = 50, **kwargs: Any) -> 'responses.market_getOrderItems_response':
        '''Get market items in the order'''

    async def getOrders(self, *, extended: Optional[Flag] = None, date_from: Optional[str] = None, date_to: Optional[str] = None, offset: int = 0, count: int = 10, **kwargs: Any) -> Union['responses.market_getOrders_response', 'responses.market_getOrders_extended_response']: ...

    async def getProductPhotoUploadServer(self, *, group_id: int, **kwargs: Any) -> 'responses.base_getUploadServer_response':
        '''Returns the server address for market photo upload.'''

    async def getProperties(self, *, group_id: int, **kwargs: Any) -> 'responses.market_getProperties_response':
        '''Get properties'''

    async def groupItems(self, *, group_id: int, item_ids: Union[int, str], item_group_id: Optional[int] = None, **kwargs: Any) -> 'responses.market_groupItems_response': ...

    async def removeFromAlbum(self, *, owner_id: int, item_id: int, album_ids: Union[int, str], **kwargs: Any) -> 'responses.base_ok_response':
        '''Removes an item from one or multiple collections.'''

    async def reorderAlbums(self, *, owner_id: int, album_id: int, before: Optional[int] = None, after: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Reorders the collections list.'''

    async def reorderItems(self, *, owner_id: int, item_id: int, album_id: Optional[int] = None, before: Optional[int] = None, after: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Changes item place in a collection.'''

    async def report(self, *, owner_id: int, item_id: int, reason: Literal[0, 1, 2, 3, 4, 5, 6] = 0, **kwargs: Any) -> 'responses.base_ok_response':
        '''Sends a complaint to the item.'''

    async def reportComment(self, *, owner_id: int, comment_id: int, reason: Literal[0, 1, 2, 3, 4, 5, 6], **kwargs: Any) -> 'responses.base_ok_response':
        '''Sends a complaint to the item's comment.'''

    async def restore(self, *, owner_id: int, item_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Restores recently deleted item'''

    async def restoreComment(self, *, owner_id: int, comment_id: int, **kwargs: Any) -> 'responses.base_bool_response':
        '''Restores a recently deleted comment'''

    async def saveProductPhoto(self, *, upload_response: str, **kwargs: Any) -> 'responses.market_photo_id_response':
        '''Save market photo after upload.'''

    async def search(self, *, owner_id: int, album_id: Optional[int] = None, q: Optional[str] = None, price_from: Optional[int] = None, price_to: Optional[int] = None, offset: Optional[int] = None, status: Optional[Union[int, str]] = None, need_variants: Optional[Flag] = None, sort: Literal[0, 1, 2, 3] = 0, rev: Literal[0, 1] = 1, count: int = 20, extended: Flag = 0, **kwargs: Any) -> Union['responses.market_search_response', 'responses.market_search_extended_response']:
        '''Searches market items in a community's catalog'''

    async def searchItems(self, *, q: str, category_id: Optional[int] = None, price_from: Optional[int] = None, price_to: Optional[int] = None, country: Optional[int] = None, city: Optional[int] = None, offset: int = 0, count: int = 30, sort_by: Literal[1, 2, 3] = 3, sort_direction: Literal[0, 1] = 1, **kwargs: Any) -> 'responses.market_search_response': ...

    async def searchItemsBasic(self, *, q: str, category_id: Optional[int] = None, price_from: Optional[int] = None, price_to: Optional[int] = None, country: Optional[int] = None, city: Optional[int] = None, only_my_groups: Optional[Flag] = None, offset: int = 0, count: int = 30, sort_by: Literal[1, 2, 3] = 3, sort_direction: Literal[0, 1] = 0, **kwargs: Any) -> 'responses.market_search_basic_response': ...

    async def ungroupItems(self, *, group_id: int, item_group_id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

class messages:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def addChatUser(self, *, chat_id: int, user_id: Optional[int] = None, visible_messages_count: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Adds a new user to a chat.'''

    async def addChatUsers(self, *, chat_id: Optional[int] = None, visible_messages_count: Optional[int] = None, **kwargs: Any) -> 'responses.messages_addChatUsers_response':
        '''Adds new users to a chat.'''

    async def allowMessagesFromGroup(self, *, group_id: int, key: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows sending messages from community to the current user.'''

    async def createChat(self, *, user_ids: Optional[Union[int, str]] = None, title: Optional[str] = None, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.messages_createChat_withPeerIds_response':
        '''Creates a chat with several participants.'''

    async def delete(self, *, message_ids: Optional[Union[int, str]] = None, spam: Optional[Flag] = None, reason: Optional[int] = None, group_id: Optional[int] = None, peer_id: Optional[int] = None, cmids: Optional[Union[int, str]] = None, delete_for_all: Flag = False, **kwargs: Any) -> 'responses.messages_delete_full_response':
        '''Deletes one or more messages.'''

    async def deleteChatPhoto(self, *, chat_id: int, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.messages_deleteChatPhoto_response':
        '''Deletes a chat's cover picture.'''

    async def deleteConversation(self, *, user_id: Optional[int] = None, peer_id: Optional[int] = None, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.messages_deleteConversation_response':
        '''Deletes all private messages in a conversation.'''

    async def deleteReaction(self, *, peer_id: int, cmid: int, **kwargs: Any) -> 'responses.base_bool_response':
        '''Delete message reaction'''

    async def denyMessagesFromGroup(self, *, group_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Denies sending message from community to the current user.'''

    async def edit(self, *, peer_id: int, message: Optional[str] = None, lat: Optional[float] = None, long: Optional[float] = None, attachment: Optional[str] = None, keep_forward_messages: Optional[Flag] = None, keep_snippets: Optional[Flag] = None, group_id: Optional[int] = None, message_id: Optional[int] = None, cmid: Optional[int] = None, template: Optional[str] = None, keyboard: Optional[str] = None, dont_parse_links: Flag = False, disable_mentions: Flag = False, **kwargs: Any) -> 'responses.base_bool_response':
        '''Edits the message.'''

    async def editChat(self, *, chat_id: int, title: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits the title of a chat.'''

    async def getByConversationMessageId(self, *, peer_id: int, conversation_message_ids: Union[int, str], extended: Optional[Flag] = None, fields: Optional[Union['objects.users_fields', str]] = None, group_id: Optional[int] = None, **kwargs: Any) -> Union['responses.messages_getByConversationMessageId_response', 'responses.messages_getByConversationMessageId_extended_response']:
        '''Returns messages by their IDs within the conversation.'''

    async def getById(self, *, message_ids: Optional[Union[int, str]] = None, extended: Optional[Flag] = None, fields: Optional[Union['objects.users_fields', str]] = None, group_id: Optional[int] = None, cmids: Optional[Union[int, str]] = None, peer_id: Optional[int] = None, preview_length: int = 0, **kwargs: Any) -> Union['responses.messages_getById_response', 'responses.messages_getById_extended_response']:
        '''Returns messages by their IDs.'''

    @overload
    async def getChat(self, *, fields: Union['objects.users_fields', str], chat_id: Optional[int] = None, chat_ids: Optional[Union[int, str]] = None, name_case: Optional['objects.base_name_case'] = None, **kwargs: Any) -> 'responses.messages_getChat_fields_response': ...
    @overload
    async def getChat(self, *, chat_id: Optional[int] = None, chat_ids: Optional[Union[int, str]] = None, fields: Optional[None] = None, name_case: Optional['objects.base_name_case'] = None, **kwargs: Any) -> Union['responses.messages_getChat_response', 'responses.messages_getChat_fields_response', 'responses.messages_getChat_chat_ids_response', 'responses.messages_getChat_chat_ids_fields_response']:
        '''Returns information about a chat.'''

    async def getChatPreview(self, *, peer_id: Optional[int] = None, link: Optional[str] = None, fields: Optional[Union['objects.users_fields', str]] = None, **kwargs: Any) -> 'responses.messages_getChatPreview_response': ...

    async def getConversationMembers(self, *, peer_id: int, extended: Optional[Flag] = None, fields: Optional[Union['objects.users_fields', str]] = None, group_id: Optional[int] = None, member_ids: Optional[Union[int, str]] = None, offset: int = 0, count: int = 20, **kwargs: Any) -> 'responses.messages_getConversationMembers_response':
        '''Returns a list of IDs of users participating in a chat.'''

    async def getConversations(self, *, extended: Optional[Flag] = None, start_message_id: Optional[int] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, group_id: Optional[int] = None, offset: int = 0, count: int = 20, filter: Literal['all', 'archive', 'important', 'sorted_chats', 'unanswered', 'unread'] = 'all', **kwargs: Any) -> 'responses.messages_getConversations_response':
        '''Returns a list of the current user's conversations.'''

    async def getConversationsById(self, *, peer_ids: Union[int, str], extended: Optional[Flag] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, group_id: Optional[int] = None, **kwargs: Any) -> Union['responses.messages_getConversationsById_response', 'responses.messages_getConversationsById_extended_response']:
        '''Returns conversations by their IDs'''

    async def getHistory(self, *, offset: Optional[int] = None, user_id: Optional[int] = None, peer_id: Optional[int] = None, start_message_id: Optional[int] = None, rev: Optional[Literal[1, 0]] = None, extended: Optional[Flag] = None, fields: Optional[Union['objects.users_fields', str]] = None, group_id: Optional[int] = None, count: int = 20, **kwargs: Any) -> Union['responses.messages_getHistory_response', 'responses.messages_getHistory_extended_response']:
        '''Returns message history for the specified user or group chat.'''

    async def getHistoryAttachments(self, *, attachment_types: Optional[messages_attachment_types_enum] = None, group_id: Optional[int] = None, peer_id: Optional[int] = None, cmid: Optional[int] = None, attachment_position: Optional[int] = None, offset: Optional[int] = None, fields: Optional[Union['objects.users_fields', str]] = None, start_from: Optional[str] = None, preserve_order: Optional[Flag] = None, photo_sizes: Optional[Flag] = None, count: int = 30, extended: Flag = False, max_forwards_level: int = 45, message_video: Flag = False, media_type: Literal['app_action_games', 'app_action_mini_apps', 'audio', 'audio_message', 'clip', 'doc', 'graffiti', 'link', 'market', 'photo', 'share', 'video', 'wall'] = 'photo', **kwargs: Any) -> 'responses.messages_getHistoryAttachments_response':
        '''Returns media files from the dialog or group chat.'''

    async def getImportantMessages(self, *, offset: Optional[int] = None, start_message_id: Optional[int] = None, preview_length: Optional[int] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, extended: Optional[Flag] = None, group_id: Optional[int] = None, count: int = 20, **kwargs: Any) -> Union['responses.messages_getImportantMessages_response', 'responses.messages_getImportantMessages_extended_response']:
        '''Returns a list of user's important messages.'''

    async def getIntentUsers(self, *, intent: Literal['confirmed_notification', 'non_promo_newsletter', 'promo_newsletter'], subscribe_id: Optional[int] = None, extended: Optional[Flag] = None, name_case: Optional['objects.base_name_case'] = None, fields: Optional[str] = None, offset: int = 0, count: int = 20, **kwargs: Any) -> 'responses.messages_getIntentUsers_response': ...

    async def getInviteLink(self, *, peer_id: int, group_id: Optional[int] = None, reset: Flag = False, **kwargs: Any) -> Union['responses.messages_getInviteLink_response', 'responses.messages_getInviteLink_by_owner_response']: ...

    async def getLastActivity(self, *, user_id: int, **kwargs: Any) -> 'responses.messages_getLastActivity_response':
        '''Returns a user's current status and date of last activity.'''

    async def getLongPollHistory(self, *, ts: Optional[int] = None, pts: Optional[int] = None, preview_length: Optional[int] = None, onlines: Optional[Flag] = None, max_msg_id: Optional[int] = None, group_id: Optional[int] = None, lp_version: Optional[int] = None, credentials: Optional[Flag] = None, fields: Union['objects.users_fields', str] = 'photo,photo_medium_rec,sex,online,screen_name', events_limit: int = 1000, msgs_limit: int = 200, last_n: int = 0, extended: Flag = False, **kwargs: Any) -> 'responses.messages_getLongPollHistory_response':
        '''Returns updates in user's private messages.'''

    async def getLongPollServer(self, *, need_pts: Optional[Flag] = None, group_id: Optional[int] = None, lp_version: int = 0, **kwargs: Any) -> 'responses.messages_getLongPollServer_response':
        '''Returns data required for connection to a Long Poll server.'''

    async def getMessagesReactions(self, *, peer_id: int, cmids: Union[int, str], **kwargs: Any) -> 'responses.messages_getMessagesReactions_response':
        '''Get reaction counters for message'''

    async def getReactedPeers(self, *, peer_id: int, cmid: int, reaction_id: Optional[int] = None, **kwargs: Any) -> 'responses.messages_getReactedPeers_response':
        '''Get reacted users and counters for message'''

    async def getReactionsAssets(self, *, client_version: Optional[int] = None, **kwargs: Any) -> 'responses.messages_getReactionsAssets_response':
        '''Get assets to display message reactions'''

    async def isMessagesFromGroupAllowed(self, *, group_id: int, user_id: int, **kwargs: Any) -> 'responses.messages_isMessagesFromGroupAllowed_response':
        '''Returns information whether sending messages from the community to current user is allowed.'''

    async def joinChatByInviteLink(self, *, link: str, **kwargs: Any) -> 'responses.messages_joinChatByInviteLink_response': ...

    async def markAsAnsweredConversation(self, *, peer_id: int, group_id: Optional[int] = None, answered: Flag = True, **kwargs: Any) -> 'responses.base_ok_response':
        '''Marks and unmarks conversations as unanswered.'''

    async def markAsImportant(self, *, message_ids: Optional[Union[int, str]] = None, important: Optional[int] = None, **kwargs: Any) -> 'responses.messages_markAsImportant_deprecated_response':
        '''Marks and unmarks messages as important (starred).'''

    async def markAsImportantConversation(self, *, peer_id: int, group_id: Optional[int] = None, important: Flag = True, **kwargs: Any) -> 'responses.base_ok_response':
        '''Marks and unmarks conversations as important.'''

    async def markAsRead(self, *, peer_id: Optional[int] = None, start_message_id: Optional[int] = None, group_id: Optional[int] = None, mark_conversation_as_read: Optional[Flag] = None, up_to_cmid: Optional[int] = None, message_ids: Union[int, str] = '', **kwargs: Any) -> 'responses.base_ok_response':
        '''Marks messages as read.'''

    async def markReactionsAsRead(self, *, peer_id: int, cmids: Optional[Union[int, str]] = None, **kwargs: Any) -> 'responses.base_bool_response':
        '''Mark messages reactions as read'''

    async def pin(self, *, peer_id: int, message_id: Optional[int] = None, cmid: Optional[int] = None, **kwargs: Any) -> 'responses.messages_pin_response':
        '''Pin a message.'''

    async def removeChatUser(self, *, chat_id: int, user_id: Optional[int] = None, member_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows the current user to leave a chat or, if the current user started the chat, allows the user to remove another user from the chat.'''

    async def restore(self, *, message_id: Optional[int] = None, group_id: Optional[int] = None, cmid: Optional[int] = None, peer_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Restores a deleted message.'''

    async def search(self, *, q: Optional[str] = None, peer_id: Optional[int] = None, date: Optional[int] = None, extended: Optional[Flag] = None, fields: Optional[str] = None, group_id: Optional[int] = None, preview_length: int = 0, offset: int = 0, count: int = 20, **kwargs: Any) -> Union['responses.messages_search_response', 'responses.messages_search_extended_response']:
        '''Returns a list of the current user's private messages that match search criteria.'''

    async def searchConversations(self, *, q: Optional[str] = None, extended: Optional[Flag] = None, fields: Optional[Union['objects.users_fields', str]] = None, group_id: Optional[int] = None, count: int = 20, **kwargs: Any) -> Union['responses.messages_searchConversations_response', 'responses.messages_searchConversations_extended_response']:
        '''Returns a list of the current user's conversations that match search criteria.'''

    async def send(self, *, user_id: Optional[int] = None, random_id: Optional[int] = None, peer_id: Optional[int] = None, peer_ids: Optional[Union[int, str]] = None, domain: Optional[str] = None, chat_id: Optional[int] = None, message: Optional[str] = None, lat: Optional[float] = None, long: Optional[float] = None, attachment: Optional[str] = None, reply_to: Optional[int] = None, forward_messages: Optional[Union[int, str]] = None, forward: Optional['objects.messages_forward'] = None, sticker_id: Optional[int] = None, group_id: Optional[int] = None, keyboard: Optional['objects.messages_keyboard'] = None, template: Optional[str] = None, payload: Optional[str] = None, content_source: Optional[str] = None, subscribe_id: Optional[int] = None, dont_parse_links: Flag = False, disable_mentions: Flag = False, intent: Literal['account_update', 'bot_ad_invite', 'bot_ad_promo', 'confirmed_notification', 'customer_support', 'default', 'finance_notification', 'game_notification', 'moderated_newsletter', 'non_promo_newsletter', 'promo_newsletter', 'purchase_update'] = 'default', **kwargs: Any) -> Union['responses.messages_send_deprecated_response', 'responses.messages_send_user_ids_response']:
        '''Sends a message.'''

    async def sendMessageEventAnswer(self, *, event_id: str, user_id: int, peer_id: int, event_data: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def sendReaction(self, *, peer_id: int, cmid: int, reaction_id: int, **kwargs: Any) -> 'responses.base_bool_response':
        '''Send message reaction'''

    async def setActivity(self, *, user_id: Optional[int] = None, type: Optional[Literal['audiomessage', 'file', 'photo', 'typing', 'video']] = None, peer_id: Optional[int] = None, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Changes the status of a user as typing in a conversation.'''

    async def setChatPhoto(self, *, file: str, **kwargs: Any) -> 'responses.messages_setChatPhoto_response':
        '''Sets a previously-uploaded picture as the cover picture of a chat.'''

    async def unpin(self, *, peer_id: int, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response': ...

class newsfeed:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def addBan(self, *, user_ids: Optional[Union[int, str]] = None, group_ids: Optional[Union[int, str]] = None, **kwargs: Any) -> 'responses.base_bool_response':
        '''Prevents news from specified users and communities from appearing in the current user's newsfeed.'''

    async def deleteBan(self, *, user_ids: Optional[Union[int, str]] = None, group_ids: Optional[Union[int, str]] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows news from previously banned users and communities to be shown in the current user's newsfeed.'''

    async def deleteList(self, *, list_id: int, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def get(self, *, filters: Optional[Union['objects.newsfeed_newsfeed_item_type', str]] = None, return_banned: Optional[Flag] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, max_photos: Optional[int] = None, source_ids: Optional[str] = None, start_from: Optional[str] = None, count: Optional[int] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, section: Optional[str] = None, **kwargs: Any) -> 'responses.newsfeed_generic_response':
        '''Returns data required to show newsfeed for the current user.'''

    async def getBanned(self, *, extended: Optional[Flag] = None, fields: Optional[Union['objects.users_fields', str]] = None, name_case: Optional['objects.base_name_case'] = None, **kwargs: Any) -> Union['responses.newsfeed_getBanned_response', 'responses.newsfeed_getBanned_extended_response']:
        '''Returns a list of users and communities banned from the current user's newsfeed.'''

    async def getComments(self, *, filters: Optional[Union['objects.newsfeed_comments_filters', str]] = None, reposts: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, start_from: Optional[str] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, count: int = 30, last_comments_count: int = 0, **kwargs: Any) -> 'responses.newsfeed_getComments_response':
        '''Returns a list of comments in the current user's newsfeed.'''

    async def getLists(self, *, list_ids: Optional[Union[int, str]] = None, extended: Flag = 0, **kwargs: Any) -> Union['responses.newsfeed_getLists_response', 'responses.newsfeed_getLists_extended_response']:
        '''Returns a list of newsfeeds followed by the current user.'''

    async def getMentions(self, *, owner_id: Optional[int] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, offset: Optional[int] = None, count: int = 20, **kwargs: Any) -> 'responses.newsfeed_getMentions_response':
        '''Returns a list of posts on user walls in which the current user is mentioned.'''

    async def getRecommended(self, *, start_time: Optional[int] = None, end_time: Optional[int] = None, max_photos: Optional[int] = None, start_from: Optional[str] = None, count: Optional[int] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, **kwargs: Any) -> 'responses.newsfeed_generic_response':
        ''', Returns a list of newsfeeds recommended to the current user.'''

    async def getSuggestedSources(self, *, offset: Optional[int] = None, shuffle: Optional[Flag] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, count: int = 20, **kwargs: Any) -> 'responses.newsfeed_getSuggestedSources_response':
        '''Returns communities and users that current user is suggested to follow.'''

    async def ignoreItem(self, *, type: 'objects.newsfeed_ignore_item_type', owner_id: int = 0, item_id: int = 0, **kwargs: Any) -> 'responses.newsfeed_ignore_item_response':
        '''Hides an item from the newsfeed.'''

    async def saveList(self, *, title: str, source_ids: Union[int, str], list_id: Optional[int] = None, no_reposts: Optional[Flag] = None, **kwargs: Any) -> 'responses.newsfeed_saveList_response':
        '''Creates and edits user newsfeed lists'''

    async def search(self, *, q: Optional[str] = None, extended: Optional[Flag] = None, latitude: Optional[float] = None, longitude: Optional[float] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, start_from: Optional[str] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, count: int = 30, **kwargs: Any) -> Union['responses.newsfeed_search_response', 'responses.newsfeed_search_strict_response', 'responses.newsfeed_search_extended_response', 'responses.newsfeed_search_extended_strict_response']:
        '''Returns search results by statuses.'''

    async def unignoreItem(self, *, type: 'objects.newsfeed_ignore_item_type', track_code: Optional[str] = None, owner_id: int = 0, item_id: int = 0, **kwargs: Any) -> 'responses.base_ok_response':
        '''Returns a hidden item to the newsfeed.'''

    async def unsubscribe(self, *, type: Literal['clip', 'market', 'note', 'photo', 'post', 'topic', 'video'], item_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Unsubscribes the current user from specified newsfeeds.'''

class notes:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def add(self, *, title: str, text: str, privacy_view: str = 'all', privacy_comment: str = 'all', **kwargs: Any) -> 'responses.notes_add_response':
        '''Creates a new note for the current user.'''

    async def createComment(self, *, note_id: int, message: str, owner_id: Optional[int] = None, reply_to: Optional[int] = None, guid: Optional[str] = None, **kwargs: Any) -> 'responses.notes_createComment_response':
        '''Adds a new comment on a note.'''

    async def delete(self, *, note_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a note of the current user.'''

    async def deleteComment(self, *, comment_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a comment on a note.'''

    async def edit(self, *, note_id: int, title: str, text: str, privacy_view: str = 'all', privacy_comment: str = 'all', **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits a note of the current user.'''

    async def editComment(self, *, comment_id: int, message: str, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits a comment on a note.'''

    async def get(self, *, note_ids: Optional[Union[int, str]] = None, user_id: Optional[int] = None, offset: int = 0, count: int = 20, sort: Literal[0, 1] = 0, **kwargs: Any) -> 'responses.notes_get_response':
        '''Returns a list of notes created by a user.'''

    async def getById(self, *, note_id: int, owner_id: Optional[int] = None, need_wiki: Flag = 0, **kwargs: Any) -> 'responses.notes_getById_response':
        '''Returns a note by its ID.'''

    async def getComments(self, *, note_id: int, owner_id: Optional[int] = None, sort: Literal[0, 1] = 0, offset: int = 0, count: int = 20, **kwargs: Any) -> 'responses.notes_getComments_response':
        '''Returns a list of comments on a note.'''

    async def restoreComment(self, *, comment_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Restores a deleted comment on a note.'''

class notifications:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def get(self, *, start_from: Optional[str] = None, filters: Optional[notifications_filters_enum] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, count: int = 30, **kwargs: Any) -> 'responses.notifications_get_response':
        '''Returns a list of notifications about other users' feedback to the current user's wall posts.'''

    async def markAsViewed(self, **kwargs: Any) -> 'responses.base_bool_response':
        '''Resets the counter of new notifications about other users' feedback to the current user's wall posts.'''

    async def sendMessage(self, *, user_ids: Union[int, str], message: str, fragment: Optional[str] = None, group_id: Optional[int] = None, random_id: Optional[int] = None, sending_mode: Literal['delayed', 'delayed_push', 'immediately', 'without_push'] = 'immediately', **kwargs: Any) -> 'responses.notifications_sendMessage_response': ...

class orders:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def cancelSubscription(self, *, user_id: int, subscription_id: int, pending_cancel: Flag = 0, **kwargs: Any) -> 'responses.base_bool_response': ...

    async def changeState(self, *, order_id: int, action: Literal['cancel', 'charge', 'refund'], app_order_id: Optional[int] = None, test_mode: Optional[Flag] = None, **kwargs: Any) -> 'responses.orders_changeState_response':
        '''Changes order status.'''

    async def get(self, *, test_mode: Optional[Flag] = None, offset: int = 0, count: int = 100, **kwargs: Any) -> 'responses.orders_get_response':
        '''Returns a list of orders.'''

    async def getAmount(self, *, user_id: int, votes: str, **kwargs: Any) -> 'responses.orders_getAmount_response': ...

    async def getById(self, *, order_id: Optional[int] = None, order_ids: Optional[Union[int, str]] = None, test_mode: Optional[Flag] = None, **kwargs: Any) -> 'responses.orders_getById_response':
        '''Returns information about orders by their IDs.'''

    async def getUserSubscriptionById(self, *, user_id: int, subscription_id: int, **kwargs: Any) -> 'responses.orders_getUserSubscriptionById_response': ...

    async def getUserSubscriptions(self, *, user_id: int, **kwargs: Any) -> 'responses.orders_getUserSubscriptions_response': ...

class pages:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def clearCache(self, *, url: str, **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows to clear the cache of particular 'external' pages which may be attached to VK posts.'''

    async def get(self, *, owner_id: Optional[int] = None, page_id: Optional[int] = None, site_preview: Optional[Flag] = None, title: Optional[str] = None, need_source: Optional[Flag] = None, need_html: Optional[Flag] = None, **kwargs: Any) -> 'responses.pages_get_response':
        '''Returns information about a wiki page.'''

    async def getHistory(self, *, page_id: int, group_id: Optional[int] = None, user_id: Optional[int] = None, **kwargs: Any) -> 'responses.pages_getHistory_response':
        '''Returns a list of all previous versions of a wiki page.'''

    async def getTitles(self, *, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.pages_getTitles_response':
        '''Returns a list of wiki pages in a group.'''

    async def getVersion(self, *, version_id: int, group_id: Optional[int] = None, user_id: Optional[int] = None, need_html: Optional[Flag] = None, **kwargs: Any) -> 'responses.pages_getVersion_response':
        '''Returns the text of one of the previous versions of a wiki page.'''

    async def parseWiki(self, *, text: str, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.pages_parseWiki_response':
        '''Returns HTML representation of the wiki markup.'''

    async def save(self, *, text: Optional[str] = None, page_id: Optional[int] = None, group_id: Optional[int] = None, user_id: Optional[int] = None, title: Optional[str] = None, **kwargs: Any) -> 'responses.pages_save_response':
        '''Saves the text of a wiki page.'''

    async def saveAccess(self, *, page_id: int, group_id: Optional[int] = None, user_id: Optional[int] = None, view: Optional[Literal[0, 1, 2]] = None, edit: Optional[Literal[0, 1, 2]] = None, **kwargs: Any) -> 'responses.pages_saveAccess_response':
        '''Saves modified read and edit access settings for a wiki page.'''

class photos:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def confirmTag(self, *, photo_id: str, tag_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Confirms a tag on a photo.'''

    async def copy(self, *, owner_id: int, photo_id: int, access_key: Optional[str] = None, **kwargs: Any) -> 'responses.photos_copy_response':
        '''Allows to copy a photo to the "Saved photos" album'''

    async def createAlbum(self, *, title: str, group_id: Optional[int] = None, description: Optional[str] = None, upload_by_admins_only: Optional[Flag] = None, comments_disabled: Optional[Flag] = None, privacy_view: str = 'all', privacy_comment: str = 'all', **kwargs: Any) -> 'responses.photos_createAlbum_response':
        '''Creates an empty photo album.'''

    async def createComment(self, *, photo_id: int, owner_id: Optional[int] = None, message: Optional[str] = None, attachments: Optional[str] = None, from_group: Optional[Flag] = None, reply_to_comment: Optional[int] = None, sticker_id: Optional[int] = None, access_key: Optional[str] = None, guid: Optional[str] = None, **kwargs: Any) -> 'responses.photos_createComment_response':
        '''Adds a new comment on the photo.'''

    async def delete(self, *, owner_id: Optional[int] = None, photo_id: Optional[int] = None, photos: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a photo.'''

    async def deleteAlbum(self, *, album_id: int, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a photo album belonging to the current user.'''

    async def deleteComment(self, *, comment_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_bool_response':
        '''Deletes a comment on the photo.'''

    async def edit(self, *, photo_id: int, owner_id: Optional[int] = None, caption: Optional[str] = None, latitude: Optional[float] = None, longitude: Optional[float] = None, place_str: Optional[str] = None, foursquare_id: Optional[str] = None, delete_place: Optional[Flag] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits the caption of a photo.'''

    async def editAlbum(self, *, album_id: int, title: Optional[str] = None, description: Optional[str] = None, owner_id: Optional[int] = None, privacy_view: Optional[str] = None, privacy_comment: Optional[str] = None, upload_by_admins_only: Optional[Flag] = None, comments_disabled: Optional[Flag] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits information about a photo album.'''

    async def editComment(self, *, comment_id: int, owner_id: Optional[int] = None, message: Optional[str] = None, attachments: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits a comment on a photo.'''

    async def get(self, *, owner_id: Optional[int] = None, album_id: Optional[str] = None, photo_ids: Optional[str] = None, rev: Optional[Flag] = None, extended: Optional[Flag] = None, feed_type: Optional[str] = None, feed: Optional[int] = None, photo_sizes: Optional[Flag] = None, offset: Optional[int] = None, count: int = 50, **kwargs: Any) -> 'responses.photos_get_response':
        '''Returns a list of a user's or community's photos.'''

    async def getAlbums(self, *, owner_id: Optional[int] = None, album_ids: Optional[Union[int, str]] = None, offset: Optional[int] = None, count: Optional[int] = None, need_system: Optional[Flag] = None, need_covers: Optional[Flag] = None, photo_sizes: Optional[Flag] = None, **kwargs: Any) -> 'responses.photos_getAlbums_response':
        '''Returns a list of a user's or community's photo albums.'''

    async def getAlbumsCount(self, *, user_id: Optional[int] = None, group_id: Optional[int] = None, need_system: Optional[Flag] = None, **kwargs: Any) -> 'responses.photos_getAlbumsCount_response':
        '''Returns the number of photo albums belonging to a user or community.'''

    async def getAll(self, *, owner_id: Optional[int] = None, extended: Optional[Flag] = None, offset: Optional[int] = None, photo_sizes: Optional[Flag] = None, no_service_albums: Optional[Flag] = None, need_hidden: Optional[Flag] = None, skip_hidden: Optional[Flag] = None, count: int = 20, **kwargs: Any) -> 'responses.photos_getAll_response':
        '''Returns a list of photos belonging to a user or community, in reverse chronological order.'''

    async def getAllComments(self, *, owner_id: Optional[int] = None, album_id: Optional[int] = None, need_likes: Optional[Flag] = None, offset: Optional[int] = None, count: Optional[int] = None, **kwargs: Any) -> 'responses.photos_getAllComments_response':
        '''Returns a list of comments on a specific photo album or all albums of the user sorted in reverse chronological order.'''

    async def getById(self, *, photos: str, extended: Optional[Flag] = None, photo_sizes: Optional[Flag] = None, **kwargs: Any) -> 'responses.photos_getById_response':
        '''Returns information about photos by their IDs.'''

    async def getChatUploadServer(self, *, chat_id: int, crop_x: Optional[int] = None, crop_y: Optional[int] = None, crop_width: Optional[int] = None, **kwargs: Any) -> 'responses.base_getUploadServer_response':
        '''Returns an upload link for chat cover pictures.'''

    async def getComments(self, *, photo_id: int, owner_id: Optional[int] = None, need_likes: Optional[Flag] = None, start_comment_id: Optional[int] = None, offset: Optional[int] = None, sort: Optional[Literal['asc', 'desc']] = None, access_key: Optional[str] = None, extended: Optional[Flag] = None, fields: Optional[Union['objects.users_fields', str]] = None, count: int = 20, **kwargs: Any) -> Union['responses.photos_getComments_response', 'responses.photos_getComments_extended_response']:
        '''Returns a list of comments on a photo.'''

    async def getMarketAlbumUploadServer(self, *, group_id: int, **kwargs: Any) -> 'responses.base_getUploadServer_response':
        '''Returns the server address for market album photo upload.'''

    async def getMarketUploadServer(self, *, group_id: int, main_photo: Optional[Flag] = None, crop_x: Optional[int] = None, crop_y: Optional[int] = None, crop_width: Optional[int] = None, **kwargs: Any) -> 'responses.photos_getMarketUploadServer_response':
        '''Returns the server address for market photo upload.'''

    async def getMessagesUploadServer(self, *, peer_id: Optional[int] = None, **kwargs: Any) -> 'responses.photos_getMessagesUploadServer_response':
        '''Returns the server address for photo upload in a private message for a user.'''

    async def getNewTags(self, *, offset: Optional[int] = None, count: int = 20, **kwargs: Any) -> 'responses.photos_getNewTags_response':
        '''Returns a list of photos with tags that have not been viewed.'''

    async def getOwnerCoverPhotoUploadServer(self, *, group_id: Optional[int] = None, crop_x: int = 0, crop_y: int = 0, crop_x2: int = 795, crop_y2: int = 200, is_video_cover: Flag = False, **kwargs: Any) -> 'responses.base_getUploadServer_response':
        '''Returns the server address for owner cover upload.'''

    async def getOwnerPhotoUploadServer(self, *, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_getUploadServer_response':
        '''Returns an upload server address for a profile or community photo.'''

    async def getTags(self, *, photo_id: int, owner_id: Optional[int] = None, access_key: Optional[str] = None, **kwargs: Any) -> 'responses.photos_getTags_response':
        '''Returns a list of tags on a photo.'''

    async def getUploadServer(self, *, album_id: Optional[int] = None, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.photos_getUploadServer_response':
        '''Returns the server address for photo upload.'''

    async def getUserPhotos(self, *, user_id: Optional[int] = None, offset: Optional[int] = None, extended: Optional[Flag] = None, sort: Optional[str] = None, count: int = 20, **kwargs: Any) -> 'responses.photos_getUserPhotos_response':
        '''Returns a list of photos in which a user is tagged.'''

    async def getWallUploadServer(self, *, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.photos_getWallUploadServer_response':
        '''Returns the server address for photo upload onto a user's wall.'''

    async def makeCover(self, *, photo_id: int, owner_id: Optional[int] = None, album_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Makes a photo into an album cover.'''

    async def move(self, *, target_album_id: int, photo_ids: Union[int, str], owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Moves a photo from one album to another.'''

    async def putTag(self, *, photo_id: int, user_id: int, owner_id: Optional[int] = None, x: Optional[float] = None, y: Optional[float] = None, x2: Optional[float] = None, y2: Optional[float] = None, **kwargs: Any) -> 'responses.photos_putTag_response':
        '''Adds a tag on the photo.'''

    async def removeTag(self, *, photo_id: int, tag_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Removes a tag from a photo.'''

    async def reorderAlbums(self, *, album_id: int, owner_id: Optional[int] = None, before: Optional[int] = None, after: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Reorders the album in the list of user albums.'''

    async def reorderPhotos(self, *, photo_id: int, owner_id: Optional[int] = None, before: Optional[int] = None, after: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Reorders the photo in the list of photos of the user album.'''

    async def report(self, *, owner_id: int, photo_id: int, reason: Optional[Literal[0, 1, 2, 3, 4, 5, 6, 8]] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Reports (submits a complaint about) a photo.'''

    async def reportComment(self, *, owner_id: int, comment_id: int, reason: Optional[Literal[0, 1, 2, 3, 4, 5, 6]] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Reports (submits a complaint about) a comment on a photo.'''

    async def restore(self, *, photo_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Restores a deleted photo.'''

    async def restoreComment(self, *, comment_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_bool_response':
        '''Restores a deleted comment on a photo.'''

    async def save(self, *, album_id: Optional[int] = None, group_id: Optional[int] = None, server: Optional[int] = None, photos_list: Optional[str] = None, hash: Optional[str] = None, latitude: Optional[float] = None, longitude: Optional[float] = None, caption: Optional[str] = None, **kwargs: Any) -> 'responses.photos_save_response':
        '''Saves photos after successful uploading.'''

    async def saveMarketAlbumPhoto(self, *, group_id: int, photo: str, server: int, hash: str, **kwargs: Any) -> 'responses.photos_saveMarketAlbumPhoto_response':
        '''Saves market album photos after successful uploading.'''

    async def saveMarketPhoto(self, *, photo: str, server: int, hash: str, group_id: Optional[int] = None, crop_data: Optional[str] = None, crop_hash: Optional[str] = None, **kwargs: Any) -> 'responses.photos_saveMarketPhoto_response':
        '''Saves market photos after successful uploading.'''

    async def saveMessagesPhoto(self, *, photo: str, server: Optional[int] = None, hash: Optional[str] = None, **kwargs: Any) -> 'responses.photos_saveMessagesPhoto_response':
        '''Saves a photo after being successfully uploaded. URL obtained with [vk.ru/dev/photos.getMessagesUploadServer|photos.getMessagesUploadServer] method.'''

    async def saveOwnerCoverPhoto(self, *, response_json: Optional[str] = None, hash: Optional[str] = None, photo: Optional[str] = None, crop_x: int = 0, crop_height: int = 0, crop_y: int = 0, crop_width: int = 0, is_video_cover: Flag = False, **kwargs: Any) -> 'responses.photos_saveOwnerCoverPhoto_response':
        '''Saves cover photo after successful uploading.'''

    async def saveOwnerPhoto(self, *, server: Optional[str] = None, hash: Optional[str] = None, photo: Optional[str] = None, **kwargs: Any) -> 'responses.photos_saveOwnerPhoto_response':
        '''Saves a profile or community photo. Upload URL can be got with the [vk.ru/dev/photos.getOwnerPhotoUploadServer|photos.getOwnerPhotoUploadServer] method.'''

    async def saveWallPhoto(self, *, photo: str, user_id: Optional[int] = None, group_id: Optional[int] = None, server: Optional[int] = None, hash: Optional[str] = None, latitude: Optional[float] = None, longitude: Optional[float] = None, caption: Optional[str] = None, **kwargs: Any) -> 'responses.photos_saveWallPhoto_response':
        '''Saves a photo to a user's or community's wall after being uploaded.'''

    async def search(self, *, q: Optional[str] = None, lat: Optional[float] = None, long: Optional[float] = None, start_time: Optional[float] = None, end_time: Optional[float] = None, sort: Optional[int] = None, offset: Optional[int] = None, count: int = 100, radius: int = 5000, **kwargs: Any) -> 'responses.photos_search_response':
        '''Returns a list of photos.'''

class podcasts:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def searchPodcast(self, *, search_string: str, offset: int = 0, count: int = 20, **kwargs: Any) -> 'responses.podcasts_searchPodcast_response': ...

class polls:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def addVote(self, *, poll_id: int, answer_ids: Union[int, str], owner_id: Optional[int] = None, is_board: Optional[Flag] = None, **kwargs: Any) -> 'responses.base_bool_response':
        '''Adds the current user's vote to the selected answer in the poll.'''

    async def create(self, *, question: Optional[str] = None, is_anonymous: Optional[Flag] = None, is_multiple: Optional[Flag] = None, end_date: Optional[int] = None, owner_id: Optional[int] = None, app_id: Optional[int] = None, add_answers: Optional[str] = None, photo_id: Optional[int] = None, background_id: Optional[Literal['1', '2', '3', '4', '6', '8', '9']] = None, disable_unvote: Optional[Flag] = None, **kwargs: Any) -> 'responses.polls_create_response':
        '''Creates polls that can be attached to the users' or communities' posts.'''

    async def deleteVote(self, *, poll_id: int, owner_id: Optional[int] = None, is_board: Optional[Flag] = None, **kwargs: Any) -> 'responses.base_bool_response':
        '''Deletes the current user's vote from the selected answer in the poll.'''

    async def edit(self, *, poll_id: int, owner_id: Optional[int] = None, question: Optional[str] = None, add_answers: Optional[str] = None, edit_answers: Optional[str] = None, delete_answers: Optional[str] = None, end_date: Optional[int] = None, photo_id: Optional[int] = None, background_id: Optional[Literal['0', '1', '2', '3', '4', '6', '8', '9']] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits created polls'''

    async def getBackgrounds(self, **kwargs: Any) -> 'responses.polls_getBackgrounds_response': ...

    async def getById(self, *, poll_id: int, owner_id: Optional[int] = None, is_board: Optional[Flag] = None, extended: Optional[Flag] = None, fields: Optional[str] = None, name_case: Optional['objects.base_name_case'] = None, friends_count: int = 3, **kwargs: Any) -> 'responses.polls_getById_response':
        '''Returns detailed information about a poll by its ID.'''

    async def getPhotoUploadServer(self, *, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_getUploadServer_response': ...

    @overload
    async def getVoters(self, *, poll_id: int, answer_ids: Union[int, str], fields: Union['objects.users_fields', str], owner_id: Optional[int] = None, is_board: Optional[Flag] = None, friends_only: Optional[Flag] = None, offset: Optional[int] = None, count: Optional[int] = None, name_case: Optional['objects.base_name_case'] = None, **kwargs: Any) -> 'responses.polls_getVoters_fields_response': ...
    @overload
    async def getVoters(self, *, poll_id: int, answer_ids: Union[int, str], owner_id: Optional[int] = None, is_board: Optional[Flag] = None, friends_only: Optional[Flag] = None, offset: Optional[int] = None, count: Optional[int] = None, fields: Optional[None] = None, name_case: Optional['objects.base_name_case'] = None, **kwargs: Any) -> Union['responses.polls_getVoters_response', 'responses.polls_getVoters_fields_response']:
        '''Returns a list of IDs of users who selected specific answers in the poll.'''

    async def savePhoto(self, *, photo: Optional[str] = None, hash: Optional[str] = None, **kwargs: Any) -> 'responses.polls_savePhoto_response': ...

class prettyCards:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def create(self, *, owner_id: int, photo: str, title: str, link: str, price: Optional[str] = None, price_old: Optional[str] = None, button: Optional[str] = None, **kwargs: Any) -> 'responses.prettyCards_create_response': ...

    async def delete(self, *, owner_id: int, card_id: int, **kwargs: Any) -> 'responses.prettyCards_delete_response': ...

    async def edit(self, *, owner_id: int, card_id: int, photo: Optional[str] = None, title: Optional[str] = None, link: Optional[str] = None, price: Optional[str] = None, price_old: Optional[str] = None, button: Optional[str] = None, **kwargs: Any) -> 'responses.prettyCards_edit_response': ...

    async def get(self, *, owner_id: int, offset: int = 0, count: int = 10, **kwargs: Any) -> 'responses.prettyCards_get_response': ...

    async def getById(self, *, owner_id: int, card_ids: Union[int, str], **kwargs: Any) -> 'responses.prettyCards_getById_response': ...

    async def getUploadURL(self, **kwargs: Any) -> 'responses.prettyCards_getUploadURL_response': ...

class search:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def getHints(self, *, q: Optional[str] = None, offset: Optional[int] = None, filters: Optional[str] = None, fields: Optional[str] = None, limit: int = 9, search_global: Flag = True, **kwargs: Any) -> 'responses.search_getHints_response':
        '''Allows the programmer to do a quick search for any substring.'''

class secure:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def addAppEvent(self, *, activity_id: int, user_id: Optional[int] = None, value: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Adds user activity information to an application'''

    async def checkToken(self, *, token: Optional[str] = None, ip: Optional[str] = None, **kwargs: Any) -> 'responses.secure_checkToken_response':
        '''Checks the user authentication in 'IFrame' and 'Flash' apps using the 'access_token' parameter.'''

    async def getAppBalance(self, **kwargs: Any) -> 'responses.secure_getAppBalance_response':
        '''Returns payment balance of the application in hundredth of a vote.'''

    async def getSMSHistory(self, *, user_id: Optional[int] = None, date_from: Optional[int] = None, date_to: Optional[int] = None, limit: int = 1000, **kwargs: Any) -> 'responses.secure_getSMSHistory_response':
        '''Shows a list of SMS notifications sent by the application using [vk.ru/dev/secure.sendSMSNotification|secure.sendSMSNotification] method.'''

    async def getTransactionsHistory(self, *, type: Optional[int] = None, uid_from: Optional[int] = None, uid_to: Optional[int] = None, date_from: Optional[int] = None, date_to: Optional[int] = None, limit: int = 1000, **kwargs: Any) -> 'responses.secure_getTransactionsHistory_response':
        '''Shows history of votes transaction between users and the application.'''

    async def getUserLevel(self, *, user_ids: Union[int, str], **kwargs: Any) -> 'responses.secure_getUserLevel_response':
        '''Returns one of the previously set game levels of one or more users in the application.'''

    async def giveEventSticker(self, *, user_ids: Union[int, str], achievement_id: int, **kwargs: Any) -> 'responses.secure_giveEventSticker_response':
        '''Opens the game achievement and gives the user a sticker'''

    async def sendNotification(self, *, message: str, user_ids: Optional[Union[int, str]] = None, user_id: Optional[int] = None, notification_id: int = 0, promo_id: int = 0, **kwargs: Any) -> 'responses.secure_sendNotification_response':
        '''Sends notification to the user.'''

    async def sendSMSNotification(self, *, user_id: int, message: str, **kwargs: Any) -> 'responses.base_ok_response':
        '''Sends 'SMS' notification to a user's mobile device.'''

    async def setCounter(self, *, counters: Optional[str] = None, user_id: Optional[int] = None, counter: Optional[int] = None, increment: Optional[Flag] = None, **kwargs: Any) -> Union['responses.base_bool_response', 'responses.secure_setCounter_array_response']:
        '''Sets a counter which is shown to the user in bold in the left menu.'''

class stats:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def get(self, *, group_id: Optional[int] = None, app_id: Optional[int] = None, timestamp_from: Optional[int] = None, timestamp_to: Optional[int] = None, intervals_count: Optional[int] = None, filters: Optional[str] = None, stats_groups: Optional[str] = None, interval: Literal['all', 'day', 'month', 'week', 'year'] = 'day', extended: Flag = True, **kwargs: Any) -> 'responses.stats_get_response':
        '''Returns statistics of a community or an application.'''

    async def getPostReach(self, *, owner_id: int, post_ids: Union[int, str], **kwargs: Any) -> 'responses.stats_getPostReach_response':
        '''Returns stats for a wall post.'''

    async def trackVisitor(self, *, type: Literal['activity', 'close', 'open'] = 'open', **kwargs: Any) -> 'responses.base_ok_response': ...

class status:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def get(self, *, user_id: Optional[int] = None, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.status_get_response':
        '''Returns data required to show the status of a user or community.'''

    async def set(self, *, text: Optional[str] = None, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Sets a new status for the current user.'''

class storage:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def get(self, *, key: Optional[str] = None, keys: Optional[str] = None, user_id: Optional[int] = None, **kwargs: Any) -> 'responses.storage_get_response':
        '''Returns a value of variable with the name set by key parameter.'''

    async def getKeys(self, *, user_id: Optional[int] = None, offset: int = 0, count: int = 100, **kwargs: Any) -> 'responses.storage_getKeys_response':
        '''Returns the names of all variables.'''

    async def set(self, *, key: str, value: Optional[str] = None, user_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Saves a value of variable with the name set by 'key' parameter.'''

class store:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def addStickersToFavorite(self, *, sticker_ids: Union[int, str], **kwargs: Any) -> 'responses.base_ok_response':
        '''Adds given sticker IDs to the list of user's favorite stickers'''

    async def getFavoriteStickers(self, **kwargs: Any) -> 'responses.store_getFavoriteStickers_response': ...

    async def getProducts(self, *, type: Optional[str] = None, merchant: Optional[str] = None, section: Optional[str] = None, product_ids: Optional[Union[int, str]] = None, filters: Optional[str] = None, extended: Flag = 0, **kwargs: Any) -> 'responses.store_getProducts_response': ...

    async def getStickersKeywords(self, *, stickers_ids: Optional[Union[int, str]] = None, products_ids: Optional[Union[int, str]] = None, all_products: Optional[Flag] = None, aliases: Flag = True, need_stickers: Flag = True, **kwargs: Any) -> 'responses.store_getStickersKeywords_response': ...

    async def removeStickersFromFavorite(self, *, sticker_ids: Union[int, str], **kwargs: Any) -> 'responses.base_ok_response':
        '''Removes given sticker IDs from the list of user's favorite stickers'''

class stories:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def banOwner(self, *, owners_ids: Union[int, str], **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows to hide stories from chosen sources from current user's feed.'''

    async def delete(self, *, owner_id: Optional[int] = None, story_id: Optional[int] = None, stories: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows to delete story.'''

    async def get(self, *, owner_id: Optional[int] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, extended: Flag = False, **kwargs: Any) -> 'responses.stories_get_V5113_response':
        '''Returns stories available for current user.'''

    async def getBanned(self, *, extended: Optional[Flag] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, **kwargs: Any) -> Union['responses.stories_getBanned_response', 'responses.stories_getBanned_extended_response']:
        '''Returns list of sources hidden from current user's feed.'''

    async def getById(self, *, stories: str, fields: Optional[Union['objects.base_user_group_fields', str]] = None, extended: Flag = False, **kwargs: Any) -> 'responses.stories_getById_extended_response':
        '''Returns story by its ID.'''

    async def getDetailedStats(self, *, owner_id: int, story_id: int, **kwargs: Any) -> 'responses.stories_getStats_V5200_response': ...

    async def getPhotoUploadServer(self, *, add_to_news: Optional[Flag] = None, user_ids: Optional[Union[int, str]] = None, reply_to_story: Optional[str] = None, link_text: Optional['objects.stories_upload_link_text'] = None, link_url: Optional[str] = None, group_id: Optional[int] = None, clickable_stickers: Optional[str] = None, **kwargs: Any) -> 'responses.stories_getPhotoUploadServer_response':
        '''Returns URL for uploading a story with photo.'''

    async def getReplies(self, *, owner_id: int, story_id: int, access_key: Optional[str] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, extended: Flag = False, **kwargs: Any) -> 'responses.stories_get_V5113_response':
        '''Returns replies to the story.'''

    async def getStats(self, *, owner_id: int, story_id: int, **kwargs: Any) -> 'responses.stories_getStats_response':
        '''Returns stories available for current user.'''

    async def getVideoUploadServer(self, *, add_to_news: Optional[Flag] = None, user_ids: Optional[Union[int, str]] = None, reply_to_story: Optional[str] = None, link_text: Optional['objects.stories_upload_link_text'] = None, link_url: Optional[str] = None, group_id: Optional[int] = None, clickable_stickers: Optional[str] = None, **kwargs: Any) -> 'responses.stories_getVideoUploadServer_response':
        '''Allows to receive URL for uploading story with video.'''

    async def getViewers(self, *, story_id: int, owner_id: Optional[int] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, count: int = 100, offset: int = 0, extended: Flag = 0, **kwargs: Any) -> Union['responses.stories_getViewers_extended_V5115_response', 'responses.stories_getViewers_extended_V5115_response']:
        '''Returns a list of story viewers.'''

    async def hideAllReplies(self, *, owner_id: int, group_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Hides all replies in the last 24 hours from the user to current user's stories.'''

    async def hideReply(self, *, owner_id: int, story_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Hides the reply to the current user's story.'''

    async def save(self, *, upload_results: Optional[str] = None, upload_results_json: Optional[str] = None, extended: Optional[Flag] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, **kwargs: Any) -> 'responses.stories_save_response': ...

    async def search(self, *, q: Optional[str] = None, place_id: Optional[int] = None, latitude: Optional[float] = None, longitude: Optional[float] = None, radius: Optional[int] = None, mentioned_id: Optional[int] = None, extended: Optional[Flag] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, count: int = 20, **kwargs: Any) -> 'responses.stories_get_V5113_response': ...

    async def sendInteraction(self, *, access_key: str, message: Optional[str] = None, is_broadcast: Flag = False, is_anonymous: Flag = False, unseen_marker: Flag = False, **kwargs: Any) -> 'responses.base_ok_response': ...

    async def unbanOwner(self, *, owners_ids: Union[int, str], **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows to show stories from hidden sources in current user's feed.'''

class streaming:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def getServerUrl(self, **kwargs: Any) -> 'responses.streaming_getServerUrl_response':
        '''Allows to receive data for the connection to Streaming API.'''

    async def getStats(self, *, type: Optional[Literal['prepared', 'received']] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, interval: Literal['1h', '24h', '5m'] = '5m', **kwargs: Any) -> 'responses.streaming_getStats_response': ...

    async def getStem(self, *, word: str, **kwargs: Any) -> 'responses.streaming_getStem_response': ...

class translations:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def translate(self, *, texts: str, translation_language: str, **kwargs: Any) -> 'responses.translations_translate_response': ...

class users:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def get(self, *, user_ids: Optional[Union[int, str]] = None, fields: Optional[Union['objects.users_fields', str]] = None, name_case: Optional['objects.base_name_case'] = None, from_group_id: int = 0, **kwargs: Any) -> 'responses.users_get_response':
        '''Returns detailed information on users.'''

    @overload
    async def getFollowers(self, *, fields: Union['objects.users_fields', str], user_id: Optional[int] = None, offset: Optional[int] = None, name_case: Optional['objects.base_name_case'] = None, count: int = 100, **kwargs: Any) -> 'responses.users_getFollowers_fields_response': ...
    @overload
    async def getFollowers(self, *, user_id: Optional[int] = None, offset: Optional[int] = None, fields: Optional[None] = None, name_case: Optional['objects.base_name_case'] = None, count: int = 100, **kwargs: Any) -> Union['responses.users_getFollowers_response', 'responses.users_getFollowers_fields_response']:
        '''Returns a list of IDs of followers of the user in question, sorted by date added, most recent first.'''

    async def getSubscriptions(self, *, user_id: Optional[int] = None, extended: Optional[Flag] = None, offset: Optional[int] = None, fields: Optional[Union['objects.users_fields', str]] = None, count: int = 20, **kwargs: Any) -> Union['responses.users_getSubscriptions_response', 'responses.users_getSubscriptions_extended_response']:
        '''Returns a list of IDs of users and communities followed by the user.'''

    async def report(self, *, user_id: int, type: Literal['advertisement', 'advertisment', 'fraud', 'insult', 'porn', 'spam'], comment: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Reports (submits a complain about) a user.'''

    async def search(self, *, q: Optional[str] = None, sort: Optional[Literal[0, 1]] = None, offset: Optional[int] = None, fields: Optional[Union['objects.users_fields', str]] = None, city: Optional[int] = None, city_id: Optional[int] = None, country: Optional[int] = None, country_id: Optional[int] = None, hometown: Optional[str] = None, university_country: Optional[int] = None, university: Optional[int] = None, university_year: Optional[int] = None, university_faculty: Optional[int] = None, university_chair: Optional[int] = None, sex: Optional[Literal[0, 1, 2]] = None, status: Optional[Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]] = None, age_from: Optional[int] = None, age_to: Optional[int] = None, birth_day: Optional[int] = None, birth_month: Optional[int] = None, birth_year: Optional[int] = None, online: Optional[Flag] = None, has_photo: Optional[Flag] = None, school_country: Optional[int] = None, school_city: Optional[int] = None, school_class: Optional[int] = None, school: Optional[int] = None, school_year: Optional[int] = None, religion: Optional[str] = None, company: Optional[str] = None, position: Optional[str] = None, group_id: Optional[int] = None, from_list: Optional[str] = None, screen_ref: Optional[str] = None, count: int = 20, from_group_id: int = 0, **kwargs: Any) -> 'responses.users_search_response':
        '''Returns a list of users matching the search criteria.'''

class utils:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def checkLink(self, *, url: str, **kwargs: Any) -> 'responses.utils_checkLink_response':
        '''Checks whether a link is blocked in VK.'''

    async def deleteFromLastShortened(self, *, key: str, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes shortened link from user's list.'''

    async def getLastShortenedLinks(self, *, count: int = 10, offset: int = 0, **kwargs: Any) -> 'responses.utils_getLastShortenedLinks_response':
        '''Returns a list of user's shortened links.'''

    async def getLinkStats(self, *, key: str, access_key: Optional[str] = None, source: Literal['vk_cc', 'vk_link'] = 'vk_cc', interval: Literal['day', 'forever', 'hour', 'month', 'week'] = 'day', intervals_count: int = 1, extended: Flag = False, **kwargs: Any) -> Union['responses.utils_getLinkStats_response', 'responses.utils_getLinkStats_extended_response']:
        '''Returns stats data for shortened link.'''

    async def getServerTime(self, **kwargs: Any) -> 'responses.utils_getServerTime_response':
        '''Returns the current time of the VK server.'''

    async def getShortLink(self, *, url: str, private: Flag = False, **kwargs: Any) -> 'responses.utils_getShortLink_response':
        '''Allows to receive a link shortened via vk.cc.'''

    async def resolveScreenName(self, *, screen_name: str, **kwargs: Any) -> 'responses.utils_resolveScreenName_response':
        '''Detects a type of object (e.g., user, community, application) and its ID by screen name.'''

class video:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def add(self, *, video_id: int, owner_id: int, target_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Adds a video to a user or community page.'''

    async def addAlbum(self, *, group_id: Optional[int] = None, title: Optional[str] = None, privacy: Optional[video_privacy_enum] = None, **kwargs: Any) -> 'responses.video_addAlbum_response':
        '''Creates an empty album for videos.'''

    async def addToAlbum(self, *, owner_id: int, video_id: int, target_id: Optional[int] = None, album_id: Optional[int] = None, album_ids: Optional[Union[int, str]] = None, **kwargs: Any) -> Union['responses.base_ok_response', 'responses.video_changeVideoAlbums_response']: ...

    async def createComment(self, *, video_id: int, owner_id: Optional[int] = None, message: Optional[str] = None, attachments: Optional[str] = None, from_group: Optional[Flag] = None, reply_to_comment: Optional[int] = None, sticker_id: Optional[int] = None, guid: Optional[str] = None, track_code: Optional[str] = None, **kwargs: Any) -> 'responses.video_createComment_response':
        '''Adds a new comment on a video.'''

    async def delete(self, *, video_id: int, owner_id: Optional[int] = None, target_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a video from a user or community page.'''

    async def deleteAlbum(self, *, album_id: int, group_id: Optional[int] = None, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a video album.'''

    async def deleteComment(self, *, comment_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a comment on a video.'''

    async def edit(self, *, video_id: int, owner_id: Optional[int] = None, name: Optional[str] = None, desc: Optional[str] = None, privacy_view: Optional[str] = None, privacy_comment: Optional[str] = None, no_comments: Optional[Flag] = None, repeat: Optional[Flag] = None, ord_info: Optional[str] = None, **kwargs: Any) -> 'responses.video_edit_response':
        '''Edits information about a video on a user or community page.'''

    async def editAlbum(self, *, album_id: int, group_id: Optional[int] = None, title: Optional[str] = None, privacy: Optional[video_privacy_enum] = None, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits the title of a video album.'''

    async def editComment(self, *, comment_id: int, owner_id: Optional[int] = None, message: Optional[str] = None, attachments: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits the text of a comment on a video.'''

    async def get(self, *, owner_id: Optional[int] = None, videos: Optional[str] = None, album_id: Optional[int] = None, offset: Optional[int] = None, extended: Optional[Flag] = None, fields: Optional[str] = None, count: int = 100, sort_album: Literal[0, 1] = 0, **kwargs: Any) -> 'responses.video_get_response':
        '''Returns detailed information about videos.'''

    async def getAlbumById(self, *, album_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.video_getAlbumById_response':
        '''Returns video album info'''

    async def getAlbums(self, *, owner_id: Optional[int] = None, offset: Optional[int] = None, extended: Optional[Flag] = None, count: int = 50, need_system: Flag = 0, **kwargs: Any) -> Union['responses.video_getAlbums_response', 'responses.video_getAlbums_extended_response']:
        '''Returns a list of video albums owned by a user or community.'''

    async def getAlbumsByVideo(self, *, owner_id: int, video_id: int, target_id: Optional[int] = None, extended: Flag = 0, **kwargs: Any) -> Union['responses.video_getAlbumsByVideo_response', 'responses.video_getAlbumsByVideo_extended_response']: ...

    async def getComments(self, *, video_id: int, owner_id: Optional[int] = None, need_likes: Optional[Flag] = None, start_comment_id: Optional[int] = None, offset: Optional[int] = None, extended: Optional[Flag] = None, fields: Optional[str] = None, comment_id: Optional[int] = None, count: int = 20, sort: Literal['asc', 'desc', 'interest'] = 'asc', thread_items_count: int = 0, **kwargs: Any) -> Union['responses.video_getComments_response', 'responses.video_getComments_extended_response']:
        '''Returns a list of comments on a video.'''

    async def getLongPollServer(self, *, video_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.video_getLongPollServer_response': ...

    async def liveGetCategories(self, **kwargs: Any) -> 'responses.video_liveGetCategories_response': ...

    async def removeFromAlbum(self, *, owner_id: int, video_id: int, target_id: Optional[int] = None, album_id: Optional[int] = None, album_ids: Optional[Union[int, str]] = None, **kwargs: Any) -> Union['responses.base_ok_response', 'responses.video_changeVideoAlbums_response']: ...

    async def reorderAlbums(self, *, album_id: int, owner_id: Optional[int] = None, before: Optional[int] = None, after: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Reorders the album in the list of user video albums.'''

    async def reorderVideos(self, *, owner_id: int, video_id: int, target_id: Optional[int] = None, before_owner_id: Optional[int] = None, before_video_id: Optional[int] = None, after_owner_id: Optional[int] = None, after_video_id: Optional[int] = None, album_id: int = -2, **kwargs: Any) -> 'responses.base_ok_response':
        '''Reorders the video in the video album.'''

    async def report(self, *, owner_id: int, video_id: int, reason: Optional[Literal[0, 1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 27, 41, 42, 43, 101]] = None, comment: Optional[str] = None, search_query: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Reports (submits a complaint about) a video.'''

    async def reportComment(self, *, owner_id: int, comment_id: int, reason: Optional[Literal[0, 1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 27, 41, 42, 43, 101]] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Reports (submits a complaint about) a comment on a video.'''

    async def restore(self, *, video_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Restores a previously deleted video.'''

    async def restoreComment(self, *, comment_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_bool_response':
        '''Restores a previously deleted comment on a video.'''

    async def save(self, *, name: Optional[str] = None, description: Optional[str] = None, is_private: Optional[Flag] = None, wallpost: Optional[Flag] = None, link: Optional[str] = None, group_id: Optional[int] = None, album_id: Optional[int] = None, privacy_view: Optional[str] = None, privacy_comment: Optional[str] = None, no_comments: Optional[Flag] = None, repeat: Optional[Flag] = None, compression: Optional[Flag] = None, ord_info: Optional[str] = None, **kwargs: Any) -> 'responses.video_save_response':
        '''Returns a server address (required for upload) and video data.'''

    async def search(self, *, q: Optional[str] = None, sort: Optional[Literal[1, 2, 0]] = None, hd: Optional[int] = None, adult: Optional[Flag] = None, live: Optional[Flag] = None, filters: Optional[video_filters_enum] = None, search_own: Optional[Flag] = None, offset: Optional[int] = None, longer: Optional[int] = None, shorter: Optional[int] = None, owner_id: Optional[int] = None, fields: Optional[str] = None, count: int = 20, extended: Flag = 0, **kwargs: Any) -> Union['responses.video_search_response', 'responses.video_search_extended_response']:
        '''Returns a list of videos under the set search criterion.'''

    async def startStreaming(self, *, video_id: Optional[int] = None, name: Optional[str] = None, description: Optional[str] = None, wallpost: Optional[Flag] = None, group_id: Optional[int] = None, privacy_view: Optional[str] = None, privacy_comment: Optional[str] = None, no_comments: Optional[Flag] = None, category_id: Optional[int] = None, publish: Optional[Flag] = None, **kwargs: Any) -> 'responses.video_startStreaming_response': ...

    async def stopStreaming(self, *, group_id: Optional[int] = None, video_id: Optional[int] = None, **kwargs: Any) -> 'responses.video_stopStreaming_response': ...

    async def unpinComment(self, *, owner_id: int, comment_id: int, **kwargs: Any) -> 'responses.base_ok_response':
        '''Unpin comment of a video.'''

class wall:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def checkCopyrightLink(self, *, link: str, **kwargs: Any) -> 'responses.base_bool_response': ...

    async def closeComments(self, *, owner_id: int, post_id: int, **kwargs: Any) -> 'responses.base_bool_response': ...

    async def createComment(self, *, post_id: int, owner_id: Optional[int] = None, from_group: Optional[int] = None, message: Optional[str] = None, reply_to_comment: Optional[int] = None, attachments: Optional[str] = None, sticker_id: Optional[int] = None, guid: Optional[str] = None, **kwargs: Any) -> 'responses.wall_createComment_response':
        '''Adds a comment to a post on a user wall or community wall.'''

    async def delete(self, *, owner_id: Optional[int] = None, post_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a post from a user wall or community wall.'''

    async def deleteComment(self, *, comment_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Deletes a comment on a post on a user wall or community wall.'''

    async def edit(self, *, post_id: int, owner_id: Optional[int] = None, friends_only: Optional[Flag] = None, message: Optional[str] = None, attachments: Optional[str] = None, services: Optional[str] = None, signed: Optional[Flag] = None, publish_date: Optional[int] = None, lat: Optional[float] = None, long: Optional[float] = None, place_id: Optional[int] = None, mark_as_ads: Optional[Flag] = None, close_comments: Optional[Flag] = None, donut_paid_duration: Optional[int] = None, poster_bkg_id: Optional[int] = None, poster_bkg_owner_id: Optional[int] = None, poster_bkg_access_hash: Optional[str] = None, copyright: Optional[str] = None, topic_id: Optional[Literal[0, 1, 7, 12, 16, 19, 21, 23, 25, 26, 32, 43]] = None, **kwargs: Any) -> 'responses.wall_edit_response':
        '''Edits a post on a user wall or community wall.'''

    async def editAdsStealth(self, *, post_id: int, owner_id: Optional[int] = None, message: Optional[str] = None, attachments: Optional[str] = None, signed: Optional[Flag] = None, lat: Optional[float] = None, long: Optional[float] = None, place_id: Optional[int] = None, link_button: Optional[str] = None, link_title: Optional[str] = None, link_image: Optional[str] = None, link_video: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Allows to edit hidden post.'''

    async def editComment(self, *, comment_id: int, owner_id: Optional[int] = None, message: Optional[str] = None, attachments: Optional[str] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Edits a comment on a user wall or community wall.'''

    async def get(self, *, domain: Optional[Union[int, str]] = None, offset: Optional[int] = None, count: Optional[int] = None, filter: Optional['objects.wall_get_filter'] = None, extended: Optional[Flag] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, **kwargs: Any) -> Union['responses.wall_get_response', 'responses.wall_get_extended_response']:
        '''Returns a list of posts on a user wall or community wall.'''

    async def getById(self, *, posts: str, extended: Optional[Flag] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, copy_history_depth: int = 2, **kwargs: Any) -> Union['responses.wall_getById_response', 'responses.wall_getById_extended_response']:
        '''Returns a list of posts from user or community walls by their IDs.'''

    async def getComment(self, *, comment_id: int, owner_id: Optional[int] = None, extended: Optional[Flag] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, **kwargs: Any) -> Union['responses.wall_getComment_response', 'responses.wall_getComment_extended_response']:
        '''Returns a comment on a post on a user wall or community wall.'''

    async def getComments(self, *, owner_id: Optional[int] = None, post_id: Optional[int] = None, need_likes: Optional[Flag] = None, start_comment_id: Optional[int] = None, offset: Optional[int] = None, count: Optional[int] = None, sort: Optional[Literal['asc', 'desc', 'smart']] = None, preview_length: Optional[int] = None, extended: Optional[Flag] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, comment_id: Optional[int] = None, thread_items_count: int = 0, **kwargs: Any) -> Union['responses.wall_getComments_response', 'responses.wall_getComments_extended_response']:
        '''Returns a list of comments on a post on a user wall or community wall.'''

    async def getReposts(self, *, owner_id: Optional[int] = None, post_id: Optional[int] = None, offset: Optional[int] = None, count: int = 20, **kwargs: Any) -> 'responses.wall_getReposts_response':
        '''Returns information about reposts of a post on user wall or community wall.'''

    async def openComments(self, *, owner_id: int, post_id: int, **kwargs: Any) -> 'responses.base_bool_response': ...

    async def parseAttachedLink(self, *, links: str, fields: Optional[str] = None, name_case: Optional['objects.base_name_case'] = None, extended: Flag = False, **kwargs: Any) -> 'responses.wall_parseAttachedLink_response': ...

    async def pin(self, *, post_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Pins the post on wall.'''

    async def post(self, *, owner_id: Optional[int] = None, friends_only: Optional[Flag] = None, from_group: Optional[Flag] = None, message: Optional[str] = None, attachments: Optional[str] = None, services: Optional[str] = None, signed: Optional[Flag] = None, publish_date: Optional[int] = None, lat: Optional[float] = None, long: Optional[float] = None, place_id: Optional[int] = None, post_id: Optional[int] = None, guid: Optional[str] = None, link_title: Optional[str] = None, link_photo_id: Optional[str] = None, close_comments: Optional[Flag] = None, donut_paid_duration: Optional[int] = None, mute_notifications: Optional[Flag] = None, copyright: Optional[str] = None, mark_as_ads: Flag = False, **kwargs: Any) -> 'responses.wall_post_response':
        '''Adds a new post on a user wall or community wall. Can also be used to publish suggested or scheduled posts.'''

    async def postAdsStealth(self, *, owner_id: int, message: Optional[str] = None, attachments: Optional[str] = None, signed: Optional[Flag] = None, lat: Optional[float] = None, long: Optional[float] = None, place_id: Optional[int] = None, guid: Optional[str] = None, link_button: Optional[str] = None, link_title: Optional[str] = None, link_image: Optional[str] = None, link_video: Optional[str] = None, **kwargs: Any) -> 'responses.wall_postAdsStealth_response':
        '''Allows to create hidden post which will not be shown on the community's wall and can be used for creating an ad with type "Community post".'''

    async def reportComment(self, *, owner_id: int, comment_id: int, reason: Literal[0, 1, 2, 3, 4, 5, 6, 8, 11], **kwargs: Any) -> 'responses.base_ok_response':
        '''Reports (submits a complaint about) a comment on a post on a user wall or community wall.'''

    async def reportPost(self, *, owner_id: int, post_id: int, reason: Literal[0, 1, 2, 3, 4, 5, 6, 8, 11], **kwargs: Any) -> 'responses.base_ok_response':
        '''Reports (submits a complaint about) a post on a user wall or community wall.'''

    async def repost(self, *, object: str, message: Optional[str] = None, group_id: Optional[int] = None, mute_notifications: Optional[Flag] = None, mark_as_ads: Flag = False, **kwargs: Any) -> 'responses.wall_repost_response':
        '''Reposts (copies) an object to a user wall or community wall.'''

    async def restore(self, *, owner_id: Optional[int] = None, post_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Restores a post deleted from a user wall or community wall.'''

    async def restoreComment(self, *, comment_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Restores a comment deleted from a user wall or community wall.'''

    async def search(self, *, domain: Optional[Union[int, str]] = None, query: Optional[str] = None, owners_only: Optional[Flag] = None, extended: Optional[Flag] = None, fields: Optional[Union['objects.base_user_group_fields', str]] = None, count: int = 20, offset: int = 0, **kwargs: Any) -> Union['responses.wall_search_response', 'responses.wall_search_extended_response']:
        '''Allows to search posts on user or community walls.'''

    async def unpin(self, *, post_id: int, owner_id: Optional[int] = None, **kwargs: Any) -> 'responses.base_ok_response':
        '''Unpins the post on wall.'''

class widgets:
    def __getattr__(self, __name: str) -> _VkMethod: ...

    async def getComments(self, *, widget_api_id: Optional[int] = None, url: Optional[str] = None, page_id: Optional[str] = None, fields: Optional[Union['objects.users_fields', str]] = None, order: str = 'date', offset: int = 0, count: int = 10, **kwargs: Any) -> 'responses.widgets_getComments_response':
        '''Gets a list of comments for the page added through the [vk.ru/dev/Comments|Comments widget].'''

    async def getPages(self, *, widget_api_id: Optional[int] = None, order: str = 'friend_likes', period: str = 'week', offset: int = 0, count: int = 10, **kwargs: Any) -> 'responses.widgets_getPages_response':
        '''Gets a list of application/site pages where the [vk.ru/dev/Comments|Comments widget] or [vk.ru/dev/Like|Like widget] is installed.'''

