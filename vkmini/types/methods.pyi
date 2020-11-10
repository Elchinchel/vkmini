from typing import Any, Dict, List

class account:
    def ban(self, owner_id: int) -> Any: ...
    def changePassword(self, restore_sid: str, change_password_hash: str, old_password: str, new_password: str) -> Any:
        '''Changes a user password after access is successfully restored with the [vk.com/dev/auth.restore|auth.restore] method.'''
    def getActiveOffers(self, offset: int = 0, count: int = 100) -> Any:
        '''Returns a list of active ads (offers) which executed by the user will bring him/her respective number of votes to his balance in the application.'''
    def getAppPermissions(self, user_id: int) -> Any:
        '''Gets settings of the user in this application.'''
    def getBanned(self, offset: int, count: int = 20) -> Any:
        '''Returns a user's blacklist.'''
    def getCounters(self, filter: List[str]) -> Any:
        '''Returns non-null values of user counters.'''
    def getInfo(self, fields: List[str]) -> Any:
        '''Returns current account info.'''
    def getProfileInfo(self) -> Any:
        '''Returns the current account info.'''
    def getPushSettings(self, device_id: str) -> Any:
        '''Gets settings of push notifications.'''
    def registerDevice(self, token: str, device_model: str, device_year: int, device_id: str, system_version: str, settings: str, sandbox: bool = 0) -> Any:
        '''Subscribes an iOS/Android/Windows Phone-based device to receive push notifications'''
    def saveProfileInfo(self, first_name: str, last_name: str, maiden_name: str, screen_name: str, cancel_request_id: int, sex: int, relation: int, relation_partner_id: int, bdate: str, bdate_visibility: int, home_town: str, country_id: int, city_id: int, status: str) -> Any:
        '''Edits current profile info.'''
    def setInfo(self, name: str, value: str) -> Any:
        '''Allows to edit the current account info.'''
    def setNameInMenu(self, user_id: int, name: str) -> Any:
        '''Sets an application screen name (up to 17 characters), that is shown to the user in the left menu.'''
    def setOffline(self) -> Any:
        '''Marks a current user as offline.'''
    def setOnline(self, voip: bool) -> Any:
        '''Marks the current user as online for 15 minutes.'''
    def setPushSettings(self, device_id: str, settings: str, key: str, value: List[str]) -> Any:
        '''Change push settings.'''
    def setSilenceMode(self, device_id: str, time: int, peer_id: int, sound: int) -> Any:
        '''Mutes push notifications for the set period of time.'''
    def unban(self, owner_id: int) -> Any: ...
    def unregisterDevice(self, device_id: str, sandbox: bool = 0) -> Any:
        '''Unsubscribes a device from push notifications.'''

class ads:
    def addOfficeUsers(self, account_id: int, data: Dict[str, Any]) -> Any:
        '''Adds managers and/or supervisors to advertising account.'''
    def checkLink(self, account_id: int, link_type: str, link_url: str, campaign_id: int) -> Any:
        '''Allows to check the ad link.'''
    def createAds(self, account_id: int, data: str) -> Any:
        '''Creates ads.'''
    def createCampaigns(self, account_id: int, data: str) -> Any:
        '''Creates advertising campaigns.'''
    def createClients(self, account_id: int, data: str) -> Any:
        '''Creates clients of an advertising agency.'''
    def createTargetGroup(self, account_id: int, client_id: int, name: str, lifetime: int, target_pixel_id: int, target_pixel_rules: str) -> Any:
        '''Creates a group to re-target ads for users who visited advertiser's site (viewed information about the product, registered, etc.).'''
    def deleteAds(self, account_id: int, ids: str) -> Any:
        '''Archives ads.'''
    def deleteCampaigns(self, account_id: int, ids: str) -> Any:
        '''Archives advertising campaigns.'''
    def deleteClients(self, account_id: int, ids: str) -> Any:
        '''Archives clients of an advertising agency.'''
    def deleteTargetGroup(self, account_id: int, client_id: int, target_group_id: int) -> Any:
        '''Deletes a retarget group.'''
    def getAccounts(self) -> Any:
        '''Returns a list of advertising accounts.'''
    def getAds(self, account_id: int, ad_ids: str, campaign_ids: str, client_id: int, include_deleted: bool, only_deleted: bool, limit: int, offset: int) -> Any:
        '''Returns number of ads.'''
    def getAdsLayout(self, account_id: int, ad_ids: str, campaign_ids: str, client_id: int, include_deleted: bool, limit: int, offset: int) -> Any:
        '''Returns descriptions of ad layouts.'''
    def getAdsTargeting(self, account_id: int, ad_ids: str, campaign_ids: str, client_id: int, include_deleted: bool, limit: int, offset: int) -> Any:
        '''Returns ad targeting parameters.'''
    def getBudget(self, account_id: int) -> Any:
        '''Returns current budget of the advertising account.'''
    def getCampaigns(self, account_id: int, client_id: int, include_deleted: bool, campaign_ids: str, fields: List[str]) -> Any:
        '''Returns a list of campaigns in an advertising account.'''
    def getCategories(self, lang: str) -> Any:
        '''Returns a list of possible ad categories.'''
    def getClients(self, account_id: int) -> Any:
        '''Returns a list of advertising agency's clients.'''
    def getDemographics(self, account_id: int, ids_type: str, ids: str, period: str, date_from: str, date_to: str) -> Any:
        '''Returns demographics for ads or campaigns.'''
    def getFloodStats(self, account_id: int) -> Any:
        '''Returns information about current state of a counter — number of remaining runs of methods and time to the next counter nulling in seconds.'''
    def getLookalikeRequests(self, account_id: int, client_id: int, requests_ids: str, offset: int = 0, limit: int = 10, sort_by: str = 'id') -> Any: ...
    def getMusicians(self, artist_name: str) -> Any: ...
    def getOfficeUsers(self, account_id: int) -> Any:
        '''Returns a list of managers and supervisors of advertising account.'''
    def getPostsReach(self, account_id: int, ids_type: str, ids: str) -> Any:
        '''Returns detailed statistics of promoted posts reach from campaigns and ads.'''
    def getRejectionReason(self, account_id: int, ad_id: int) -> Any:
        '''Returns a reason of ad rejection for pre-moderation.'''
    def getStatistics(self, account_id: int, ids_type: str, ids: str, period: str, date_from: str, date_to: str, stats_fields: List[str]) -> Any:
        '''Returns statistics of performance indicators for ads, campaigns, clients or the whole account.'''
    def getSuggestions(self, section: str, ids: str, q: str, country: int, cities: str, lang: str) -> Any:
        '''Returns a set of auto-suggestions for various targeting parameters.'''
    def getTargetGroups(self, account_id: int, client_id: int, extended: bool) -> Any:
        '''Returns a list of target groups.'''
    def getTargetingStats(self, account_id: int, client_id: int, criteria: str, ad_id: int, ad_format: int, ad_platform: str, ad_platform_no_wall: str, ad_platform_no_ad_network: str, link_url: str, link_domain: str, need_precise: bool) -> Any:
        '''Returns the size of targeting audience, and also recommended values for CPC and CPM.'''
    def getUploadURL(self, ad_format: int, icon: int) -> Any:
        '''Returns URL to upload an ad photo to.'''
    def getVideoUploadURL(self) -> Any:
        '''Returns URL to upload an ad video to.'''
    def importTargetContacts(self, account_id: int, client_id: int, target_group_id: int, contacts: str) -> Any:
        '''Imports a list of advertiser's contacts to count VK registered users against the target group.'''
    def removeOfficeUsers(self, account_id: int, ids: str) -> Any:
        '''Removes managers and/or supervisors from advertising account.'''
    def updateAds(self, account_id: int, data: str) -> Any:
        '''Edits ads.'''
    def updateCampaigns(self, account_id: int, data: str) -> Any:
        '''Edits advertising campaigns.'''
    def updateClients(self, account_id: int, data: str) -> Any:
        '''Edits clients of an advertising agency.'''
    def updateOfficeUsers(self, account_id: int, data: Dict[str, Any]) -> Any:
        '''Adds managers and/or supervisors to advertising account.'''
    def updateTargetGroup(self, account_id: int, client_id: int, target_group_id: int, name: str, domain: str, lifetime: int, target_pixel_id: int, target_pixel_rules: str) -> Any:
        '''Edits a retarget group.'''

class adsweb:
    def getAdCategories(self, office_id: int) -> Any: ...
    def getAdUnitCode(self) -> Any: ...
    def getAdUnits(self, office_id: int, sites_ids: str, ad_units_ids: str, fields: str, limit: int = None, offset: int = 0) -> Any: ...
    def getFraudHistory(self, office_id: int, sites_ids: str, limit: int = None, offset: int = 0) -> Any: ...
    def getSites(self, office_id: int, sites_ids: str, fields: str, limit: int = None, offset: int = 0) -> Any: ...
    def getStatistics(self, office_id: int, ids_type: str, ids: str, period: str, date_from: str, date_to: str, fields: str, page_id: str, limit: int = None) -> Any: ...

class appWidgets:
    def getAppImageUploadServer(self, image_type: str) -> Any:
        '''Returns a URL for uploading a photo to the community collection for community app widgets'''
    def getAppImages(self, offset: int, image_type: str, count: int = 20) -> Any:
        '''Returns an app collection of images for community app widgets'''
    def getGroupImageUploadServer(self, image_type: str) -> Any:
        '''Returns a URL for uploading a photo to the community collection for community app widgets'''
    def getGroupImages(self, offset: int, image_type: str, count: int = 20) -> Any:
        '''Returns a community collection of images for community app widgets'''
    def getImagesById(self, images: List[str]) -> Any:
        '''Returns an image for community app widgets by its ID'''
    def saveAppImage(self, hash: str, image: str) -> Any:
        '''Allows to save image into app collection for community app widgets'''
    def saveGroupImage(self, hash: str, image: str) -> Any:
        '''Allows to save image into community collection for community app widgets'''
    def update(self, code: str, type: str) -> Any:
        '''Allows to update community app widget'''

class apps:
    def deleteAppRequests(self) -> Any:
        '''Deletes all request notifications from the current app.'''
    def get(self, app_id: int, app_ids: List[str], fields: Dict[str, Any], name_case: str, platform: str = 'web', extended: bool = 0, return_friends: bool = 0) -> Any:
        '''Returns applications data.'''
    def getCatalog(self, sort: str, offset: int, platform: str, extended: bool, return_friends: bool, fields: Dict[str, Any], name_case: str, q: str, genre_id: int, filter: str, count: int = 100) -> Any:
        '''Returns a list of applications (apps) available to users in the App Catalog.'''
    def getFriendsList(self, fields: Dict[str, Any], extended: bool = 0, count: int = 20, offset: int = 0, type: str = 'invite') -> Any:
        '''Creates friends list for requests and invites in current app.'''
    def getLeaderboard(self, type: str, extended: bool = 0) -> Any:
        '''Returns players rating in the game.'''
    def getScopes(self, type: str = 'user') -> Any:
        '''Returns scopes for auth'''
    def getScore(self, user_id: int) -> Any:
        '''Returns user score in app'''
    def promoHasActiveGift(self, promo_id: int, user_id: int) -> Any: ...
    def promoUseGift(self, promo_id: int, user_id: int) -> Any: ...
    def sendRequest(self, user_id: int, text: str, name: str, key: str, separate: bool, type: str = 'request') -> Any:
        '''Sends a request to another user in an app that uses VK authorization.'''

class auth:
    def checkPhone(self, phone: str, client_id: int, client_secret: str, auth_by_phone: bool) -> Any:
        '''Checks a user's phone number for correctness.'''
    def restore(self, phone: str, last_name: str) -> Any:
        '''Allows to restore account access using a code received via SMS. " This method is only available for apps with [vk.com/dev/auth_direct|Direct authorization] access. "'''

class board:
    def addTopic(self, group_id: int, title: str, text: str, from_group: bool, attachments: List[str]) -> Any:
        '''Creates a new topic on a community's discussion board.'''
    def closeTopic(self, group_id: int, topic_id: int) -> Any:
        '''Closes a topic on a community's discussion board so that comments cannot be posted.'''
    def createComment(self, group_id: int, topic_id: int, message: str, attachments: List[str], from_group: bool, sticker_id: int, guid: str) -> Any:
        '''Adds a comment on a topic on a community's discussion board.'''
    def deleteComment(self, group_id: int, topic_id: int, comment_id: int) -> Any:
        '''Deletes a comment on a topic on a community's discussion board.'''
    def deleteTopic(self, group_id: int, topic_id: int) -> Any:
        '''Deletes a topic from a community's discussion board.'''
    def editComment(self, group_id: int, topic_id: int, comment_id: int, message: str, attachments: List[str]) -> Any:
        '''Edits a comment on a topic on a community's discussion board.'''
    def editTopic(self, group_id: int, topic_id: int, title: str) -> Any:
        '''Edits the title of a topic on a community's discussion board.'''
    def fixTopic(self, group_id: int, topic_id: int) -> Any:
        '''Pins a topic (fixes its place) to the top of a community's discussion board.'''
    def getComments(self, group_id: int, topic_id: int, need_likes: bool, start_comment_id: int, offset: int, extended: bool, sort: str, count: int = 20) -> Any:
        '''Returns a list of comments on a topic on a community's discussion board.'''
    def getTopics(self, group_id: int, topic_ids: List[int], order: int, offset: int, extended: bool, preview: int, count: int = 40, preview_length: int = 90) -> Any:
        '''Returns a list of topics on a community's discussion board.'''
    def openTopic(self, group_id: int, topic_id: int) -> Any:
        '''Re-opens a previously closed topic on a community's discussion board.'''
    def restoreComment(self, group_id: int, topic_id: int, comment_id: int) -> Any:
        '''Restores a comment deleted from a topic on a community's discussion board.'''
    def unfixTopic(self, group_id: int, topic_id: int) -> Any:
        '''Unpins a pinned topic from the top of a community's discussion board.'''

class database:
    def getChairs(self, faculty_id: int, offset: int, count: int = 100) -> Any:
        '''Returns list of chairs on a specified faculty.'''
    def getCities(self, country_id: int, region_id: int, q: str, need_all: bool, offset: int, count: int = 100) -> Any:
        '''Returns a list of cities.'''
    def getCitiesById(self, city_ids: List[int]) -> Any:
        '''Returns information about cities by their IDs.'''
    def getCountries(self, need_all: bool, code: str, offset: int, count: int = 100) -> Any:
        '''Returns a list of countries.'''
    def getCountriesById(self, country_ids: List[int]) -> Any:
        '''Returns information about countries by their IDs.'''
    def getFaculties(self, university_id: int, offset: int, count: int = 100) -> Any:
        '''Returns a list of faculties (i.e., university departments).'''
    def getMetroStations(self, city_id: int, offset: int, count: int = 100, extended: bool = False) -> Any:
        '''Get metro stations by city'''
    def getMetroStationsById(self, station_ids: List[int]) -> Any:
        '''Get metro station by his id'''
    def getRegions(self, country_id: int, q: str, offset: int, count: int = 100) -> Any:
        '''Returns a list of regions.'''
    def getSchoolClasses(self, country_id: int) -> Any:
        '''Returns a list of school classes specified for the country.'''
    def getSchools(self, q: str, city_id: int, offset: int, count: int = 100) -> Any:
        '''Returns a list of schools.'''
    def getUniversities(self, q: str, country_id: int, city_id: int, offset: int, count: int = 100) -> Any:
        '''Returns a list of higher education institutions.'''

class docs:
    def add(self, owner_id: int, doc_id: int, access_key: str) -> Any:
        '''Copies a document to a user's or community's document list.'''
    def delete(self, owner_id: int, doc_id: int) -> Any:
        '''Deletes a user or community document.'''
    def edit(self, owner_id: int, doc_id: int, title: str, tags: List[str]) -> Any:
        '''Edits a document.'''
    def get(self, count: int, offset: int, owner_id: int, type: int = 0, return_tags: bool = False) -> Any:
        '''Returns detailed information about user or community documents.'''
    def getById(self, docs: List[str], return_tags: bool = False) -> Any:
        '''Returns information about documents by their IDs.'''
    def getMessagesUploadServer(self, peer_id: int, type: str = 'doc') -> Any:
        '''Returns the server address for document upload.'''
    def getTypes(self, owner_id: int) -> Any:
        '''Returns documents types available for current user.'''
    def getUploadServer(self, group_id: int) -> Any:
        '''Returns the server address for document upload.'''
    def getWallUploadServer(self, group_id: int) -> Any:
        '''Returns the server address for document upload onto a user's or community's wall.'''
    def save(self, file: str, title: str, tags: str, return_tags: bool = False) -> Any:
        '''Saves a document after [vk.com/dev/upload_files_2|uploading it to a server].'''
    def search(self, q: str, search_own: bool, offset: int, return_tags: bool, count: int = 20) -> Any:
        '''Returns a list of documents matching the search criteria.'''

class downloadedGames:
    def getPaidStatus(self, user_id: int) -> Any: ...

class fave:
    def addArticle(self, url: str) -> Any: ...
    def addLink(self, link: str) -> Any:
        '''Adds a link to user faves.'''
    def addPage(self, user_id: int, group_id: int) -> Any: ...
    def addPost(self, owner_id: int, id: int, access_key: str) -> Any: ...
    def addProduct(self, owner_id: int, id: int, access_key: str) -> Any: ...
    def addTag(self, name: str, position: str = 'back') -> Any: ...
    def addVideo(self, owner_id: int, id: int, access_key: str) -> Any: ...
    def editTag(self, id: int, name: str) -> Any: ...
    def get(self, item_type: str, tag_id: int, offset: int, fields: str, is_from_snackbar: bool, extended: bool = False, count: int = 50) -> Any: ...
    def getPages(self, offset: int, type: str, fields: Dict[str, Any], tag_id: int, count: int = 50) -> Any: ...
    def getTags(self) -> Any: ...
    def markSeen(self) -> Any: ...
    def removeArticle(self, owner_id: int, article_id: int) -> Any: ...
    def removeLink(self, link_id: str, link: str) -> Any:
        '''Removes link from the user's faves.'''
    def removePage(self, user_id: int, group_id: int) -> Any: ...
    def removePost(self, owner_id: int, id: int) -> Any: ...
    def removeProduct(self, owner_id: int, id: int) -> Any: ...
    def removeTag(self, id: int) -> Any: ...
    def removeVideo(self, owner_id: int, id: int) -> Any: ...
    def reorderTags(self, ids: List[int]) -> Any: ...
    def setPageTags(self, user_id: int, group_id: int, tag_ids: List[int]) -> Any: ...
    def setTags(self, item_type: str, item_owner_id: int, item_id: int, tag_ids: List[int], link_id: str, link_url: str) -> Any: ...
    def trackPageInteraction(self, user_id: int, group_id: int) -> Any: ...

class friends:
    def add(self, user_id: int, text: str, follow: bool) -> Any:
        '''Approves or creates a friend request.'''
    def addList(self, name: str, user_ids: List[int]) -> Any:
        '''Creates a new friend list for the current user.'''
    def areFriends(self, user_ids: List[int], need_sign: bool, extended: bool) -> Any:
        '''Checks the current user's friendship status with other specified users.'''
    def delete(self, user_id: int) -> Any:
        '''Declines a friend request or deletes a user from the current user's friend list.'''
    def deleteAllRequests(self) -> Any:
        '''Marks all incoming friend requests as viewed.'''
    def deleteList(self, list_id: int) -> Any:
        '''Deletes a friend list of the current user.'''
    def edit(self, user_id: int, list_ids: List[int]) -> Any:
        '''Edits the friend lists of the selected user.'''
    def editList(self, name: str, list_id: int, user_ids: List[int], add_user_ids: List[int], delete_user_ids: List[int]) -> Any:
        '''Edits a friend list of the current user.'''
    def get(self, user_id: int, order: str, list_id: int, offset: int, fields: Dict[str, Any], name_case: str, ref: str, count: int = 5000) -> Any:
        '''Returns a list of user IDs or detailed information about a user's friends.'''
    def getAppUsers(self) -> Any:
        '''Returns a list of IDs of the current user's friends who installed the application.'''
    def getByPhones(self, phones: List[str], fields: Dict[str, Any]) -> Any:
        '''Returns a list of the current user's friends whose phone numbers, validated or specified in a profile, are in a given list.'''
    def getLists(self, user_id: int, return_system: bool) -> Any:
        '''Returns a list of the user's friend lists.'''
    def getMutual(self, source_uid: int, target_uid: int, target_uids: List[int], order: str, count: int, offset: int) -> Any:
        '''Returns a list of user IDs of the mutual friends of two users.'''
    def getOnline(self, user_id: int, list_id: int, online_mobile: bool, order: str, count: int, offset: int) -> Any:
        '''Returns a list of user IDs of a user's friends who are online.'''
    def getRecent(self, count: int = 100) -> Any:
        '''Returns a list of user IDs of the current user's recently added friends.'''
    def getRequests(self, offset: int, extended: bool, need_mutual: bool, out: bool, sort: int, suggested: bool, ref: str, fields: Dict[str, Any], count: int = 100, need_viewed: bool = 0) -> Any:
        '''Returns information about the current user's incoming and outgoing friend requests.'''
    def getSuggestions(self, filter: List[str], offset: int, fields: Dict[str, Any], name_case: str, count: int = 500) -> Any:
        '''Returns a list of profiles of users whom the current user may know.'''
    def search(self, user_id: int, q: str, fields: Dict[str, Any], offset: int, name_case: str = 'Nom', count: int = 20) -> Any:
        '''Returns a list of friends matching the search criteria.'''

class gifts:
    def get(self, user_id: int, count: int, offset: int) -> Any:
        '''Returns a list of user gifts.'''

class groups:
    def addAddress(self, group_id: int, title: str, address: str, additional_address: str, country_id: int, city_id: int, metro_id: int, latitude: float, longitude: float, phone: str, timetable: str, is_main_address: bool, work_info_status: str = 'no_information') -> Any: ...
    def addCallbackServer(self, group_id: int, url: str, title: str, secret_key: str) -> Any: ...
    def addLink(self, group_id: int, link: str, text: str) -> Any:
        '''Allows to add a link to the community.'''
    def approveRequest(self, group_id: int, user_id: int) -> Any:
        '''Allows to approve join request to the community.'''
    def ban(self, group_id: int, owner_id: int, end_date: int, reason: int, comment: str, comment_visible: bool) -> Any: ...
    def create(self, title: str, description: str, public_category: int, subtype: int, type: str = 'group') -> Any:
        '''Creates a new community.'''
    def deleteAddress(self, group_id: int, address_id: int) -> Any: ...
    def deleteCallbackServer(self, group_id: int, server_id: int) -> Any: ...
    def deleteLink(self, group_id: int, link_id: int) -> Any:
        '''Allows to delete a link from the community.'''
    def disableOnline(self, group_id: int) -> Any: ...
    def edit(self, group_id: int, title: str, description: str, screen_name: str, access: int, website: str, subject: str, email: str, phone: str, rss: str, event_start_date: int, event_finish_date: int, event_group_id: int, public_category: int, public_subcategory: int, public_date: str, wall: int, topics: int, photos: int, video: int, audio: int, links: bool, events: bool, places: bool, contacts: bool, docs: int, wiki: int, messages: bool, articles: bool, addresses: bool, market: bool, market_comments: bool, market_country: List[int], market_city: List[int], market_currency: int, market_contact: int, market_wiki: int, obscene_filter: bool, obscene_stopwords: bool, obscene_words: List[str], main_section: int, secondary_section: int, country: int, city: int, age_limits: int = 1) -> Any:
        '''Edits a community.'''
    def editAddress(self, group_id: int, address_id: int, title: str, address: str, additional_address: str, country_id: int, city_id: int, metro_id: int, latitude: float, longitude: float, phone: str, work_info_status: str, timetable: str, is_main_address: bool) -> Any: ...
    def editCallbackServer(self, group_id: int, server_id: int, url: str, title: str, secret_key: str) -> Any: ...
    def editLink(self, group_id: int, link_id: int, text: str) -> Any:
        '''Allows to edit a link in the community.'''
    def editManager(self, group_id: int, user_id: int, role: str, is_contact: bool, contact_position: str, contact_phone: str, contact_email: str) -> Any:
        '''Allows to add, remove or edit the community manager.'''
    def enableOnline(self, group_id: int) -> Any: ...
    def get(self, user_id: int, extended: bool, filter: Dict[str, Any], fields: Dict[str, Any], offset: int, count: int) -> Any:
        '''Returns a list of the communities to which a user belongs.'''
    def getAddresses(self, group_id: int, address_ids: List[int], latitude: float, longitude: float, offset: int, fields: Dict[str, Any], count: int = 10) -> Any:
        '''Returns a list of community addresses.'''
    def getBanned(self, group_id: int, offset: int, fields: Dict[str, Any], owner_id: int, count: int = 20) -> Any:
        '''Returns a list of users on a community blacklist.'''
    def getById(self, group_ids: List[str], group_id: str, fields: Dict[str, Any]) -> Any:
        '''Returns information about communities by their IDs.'''
    def getCallbackConfirmationCode(self, group_id: int) -> Any:
        '''Returns Callback API confirmation code for the community.'''
    def getCallbackServers(self, group_id: int, server_ids: List[int]) -> Any: ...
    def getCallbackSettings(self, group_id: int, server_id: int) -> Any:
        '''Returns [vk.com/dev/callback_api|Callback API] notifications settings.'''
    def getCatalog(self, category_id: int, subcategory_id: int) -> Any:
        '''Returns communities list for a catalog category.'''
    def getCatalogInfo(self, extended: bool = 0, subcategories: bool = 0) -> Any:
        '''Returns categories list for communities catalog'''
    def getInvitedUsers(self, group_id: int, offset: int, fields: Dict[str, Any], name_case: str, count: int = 20) -> Any:
        '''Returns invited users list of a community'''
    def getInvites(self, offset: int, extended: bool, count: int = 20) -> Any:
        '''Returns a list of invitations to join communities and events.'''
    def getLongPollServer(self, group_id: int) -> Any:
        '''Returns the data needed to query a Long Poll server for events'''
    def getLongPollSettings(self, group_id: int) -> Any:
        '''Returns Long Poll notification settings'''
    def getMembers(self, group_id: str, offset: int, fields: Dict[str, Any], filter: str, sort: str = 'id_asc', count: int = 1000) -> Any:
        '''Returns a list of community members.'''
    def getRequests(self, group_id: int, offset: int, fields: Dict[str, Any], count: int = 20) -> Any:
        '''Returns a list of requests to the community.'''
    def getSettings(self, group_id: int) -> Any:
        '''Returns community settings.'''
    def getTagList(self, group_id: int) -> Any:
        '''List of group's tags'''
    def getTokenPermissions(self) -> Any: ...
    def invite(self, group_id: int, user_id: int) -> Any:
        '''Allows to invite friends to the community.'''
    def isMember(self, group_id: str, user_id: int, user_ids: List[int], extended: bool) -> Any:
        '''Returns information specifying whether a user is a member of a community.'''
    def join(self, group_id: int, not_sure: str) -> Any:
        '''With this method you can join the group or public page, and also confirm your participation in an event.'''
    def leave(self, group_id: int) -> Any:
        '''With this method you can leave a group, public page, or event.'''
    def removeUser(self, group_id: int, user_id: int) -> Any:
        '''Removes a user from the community.'''
    def reorderLink(self, group_id: int, link_id: int, after: int) -> Any:
        '''Allows to reorder links in the community.'''
    def search(self, q: str, type: str, country_id: int, city_id: int, future: bool, market: bool, sort: int, offset: int, count: int = 20) -> Any:
        '''Returns a list of communities matching the search criteria.'''
    def setCallbackSettings(self, group_id: int, server_id: int, api_version: str, message_new: bool, message_reply: bool, message_allow: bool, message_edit: bool, message_deny: bool, message_typing_state: bool, photo_new: bool, audio_new: bool, video_new: bool, wall_reply_new: bool, wall_reply_edit: bool, wall_reply_delete: bool, wall_reply_restore: bool, wall_post_new: bool, wall_repost: bool, board_post_new: bool, board_post_edit: bool, board_post_restore: bool, board_post_delete: bool, photo_comment_new: bool, photo_comment_edit: bool, photo_comment_delete: bool, photo_comment_restore: bool, video_comment_new: bool, video_comment_edit: bool, video_comment_delete: bool, video_comment_restore: bool, market_comment_new: bool, market_comment_edit: bool, market_comment_delete: bool, market_comment_restore: bool, poll_vote_new: bool, group_join: bool, group_leave: bool, group_change_settings: bool, group_change_photo: bool, group_officers_edit: bool, user_block: bool, user_unblock: bool, lead_forms_new: bool, like_add: bool, like_remove: bool, message_event: bool) -> Any:
        '''Allow to set notifications settings for group.'''
    def setLongPollSettings(self, group_id: int, enabled: bool, api_version: str, message_new: bool, message_reply: bool, message_allow: bool, message_deny: bool, message_edit: bool, message_typing_state: bool, photo_new: bool, audio_new: bool, video_new: bool, wall_reply_new: bool, wall_reply_edit: bool, wall_reply_delete: bool, wall_reply_restore: bool, wall_post_new: bool, wall_repost: bool, board_post_new: bool, board_post_edit: bool, board_post_restore: bool, board_post_delete: bool, photo_comment_new: bool, photo_comment_edit: bool, photo_comment_delete: bool, photo_comment_restore: bool, video_comment_new: bool, video_comment_edit: bool, video_comment_delete: bool, video_comment_restore: bool, market_comment_new: bool, market_comment_edit: bool, market_comment_delete: bool, market_comment_restore: bool, poll_vote_new: bool, group_join: bool, group_leave: bool, group_change_settings: bool, group_change_photo: bool, group_officers_edit: bool, user_block: bool, user_unblock: bool, like_add: bool, like_remove: bool, message_event: bool) -> Any:
        '''Sets Long Poll notification settings'''
    def setSettings(self, group_id: int, messages: bool, bots_capabilities: bool, bots_start_button: bool, bots_add_to_chat: bool) -> Any: ...
    def setUserNote(self, group_id: int, user_id: int, note: str) -> Any:
        '''In order to save note about group participant'''
    def tagAdd(self, group_id: int, tag_name: str, tag_color: str) -> Any:
        '''Add new group's tag'''
    def tagBind(self, group_id: int, tag_id: int, user_id: int, act: str) -> Any:
        '''Bind or unbind group's tag to user'''
    def tagDelete(self, group_id: int, tag_id: int) -> Any:
        '''Delete group's tag'''
    def tagUpdate(self, group_id: int, tag_id: int, tag_name: str) -> Any:
        '''Update group's tag'''
    def toggleMarket(self, group_id: int, state: str) -> Any: ...
    def unban(self, group_id: int, owner_id: int) -> Any: ...

class leads:
    def checkUser(self, lead_id: int, test_result: int, age: int, country: str, test_mode: bool = 0, auto_start: bool = 0) -> Any:
        '''Checks if the user can start the lead.'''
    def complete(self, vk_sid: str, secret: str, comment: str) -> Any:
        '''Completes the lead started by user.'''
    def getStats(self, lead_id: int, secret: str, date_start: str, date_end: str) -> Any:
        '''Returns lead stats data.'''
    def getUsers(self, offer_id: int, secret: str, offset: int, status: int, reverse: bool, count: int = 100) -> Any:
        '''Returns a list of last user actions for the offer.'''
    def metricHit(self, data: str) -> Any:
        '''Counts the metric event.'''
    def start(self, lead_id: int, secret: str, uid: int = 0, aid: int = 0, test_mode: bool = 0, force: bool = 0) -> Any:
        '''Creates new session for the user passing the offer.'''

class likes:
    def add(self, type: str, owner_id: int, item_id: int, access_key: str) -> Any:
        '''Adds the specified object to the 'Likes' list of the current user.'''
    def delete(self, type: str, owner_id: int, item_id: int, access_key: str) -> Any:
        '''Deletes the specified object from the 'Likes' list of the current user.'''
    def getList(self, type: str, owner_id: int, item_id: int, page_url: str, filter: str, extended: bool, offset: int, count: int, skip_own: bool, friends_only: int = 0) -> Any:
        '''Returns a list of IDs of users who added the specified object to their 'Likes' list.'''
    def isLiked(self, user_id: int, type: str, owner_id: int, item_id: int) -> Any:
        '''Checks for the object in the 'Likes' list of the specified user.'''

class market:
    def add(self, owner_id: int, name: str, description: str, category_id: int, price: float, old_price: float, deleted: bool, main_photo_id: int, photo_ids: List[int], url: str, dimension_width: int, dimension_height: int, dimension_length: int, weight: int) -> Any:
        '''Ads a new item to the market.'''
    def addAlbum(self, owner_id: int, title: str, photo_id: int, main_album: bool) -> Any:
        '''Creates new collection of items'''
    def addToAlbum(self, owner_id: int, item_id: int, album_ids: List[int]) -> Any:
        '''Adds an item to one or multiple collections.'''
    def createComment(self, owner_id: int, item_id: int, message: str, attachments: List[str], from_group: bool, reply_to_comment: int, sticker_id: int, guid: str) -> Any:
        '''Creates a new comment for an item.'''
    def delete(self, owner_id: int, item_id: int) -> Any:
        '''Deletes an item.'''
    def deleteAlbum(self, owner_id: int, album_id: int) -> Any:
        '''Deletes a collection of items.'''
    def deleteComment(self, owner_id: int, comment_id: int) -> Any:
        '''Deletes an item's comment'''
    def edit(self, owner_id: int, item_id: int, name: str, description: str, category_id: int, price: float, deleted: bool, main_photo_id: int, photo_ids: List[int], url: str) -> Any:
        '''Edits an item.'''
    def editAlbum(self, owner_id: int, album_id: int, title: str, photo_id: int, main_album: bool) -> Any:
        '''Edits a collection of items'''
    def editComment(self, owner_id: int, comment_id: int, message: str, attachments: List[str]) -> Any:
        '''Chages item comment's text'''
    def editOrder(self, user_id: int, order_id: int, merchant_comment: str, status: int) -> Any:
        '''Edit order'''
    def get(self, owner_id: int, offset: int, extended: bool, album_id: int = 0, count: int = 100) -> Any:
        '''Returns items list for a community.'''
    def getAlbumById(self, owner_id: int, album_ids: List[int]) -> Any:
        '''Returns items album's data'''
    def getAlbums(self, owner_id: int, offset: int, count: int = 50) -> Any:
        '''Returns community's collections list.'''
    def getById(self, item_ids: List[str], extended: bool) -> Any:
        '''Returns information about market items by their ids.'''
    def getCategories(self, offset: int, count: int = 10) -> Any:
        '''Returns a list of market categories.'''
    def getComments(self, owner_id: int, item_id: int, need_likes: bool, start_comment_id: int, extended: bool, fields: Dict[str, Any], offset: int = 0, count: int = 20, sort: str = 'asc') -> Any:
        '''Returns comments list for an item.'''
    def getGroupOrders(self, group_id: int, offset: int = 0, count: int = 10) -> Any:
        '''Get market orders'''
    def getOrderById(self, user_id: int, order_id: int, extended: bool) -> Any:
        '''Get order'''
    def getOrderItems(self, order_id: int, offset: int, count: int = 50) -> Any:
        '''Get market items in the order'''
    def getOrders(self, extended: bool, offset: int = 0, count: int = 10) -> Any: ...
    def removeFromAlbum(self, owner_id: int, item_id: int, album_ids: List[int]) -> Any:
        '''Removes an item from one or multiple collections.'''
    def reorderAlbums(self, owner_id: int, album_id: int, before: int, after: int) -> Any:
        '''Reorders the collections list.'''
    def reorderItems(self, owner_id: int, album_id: int, item_id: int, before: int, after: int) -> Any:
        '''Changes item place in a collection.'''
    def report(self, owner_id: int, item_id: int, reason: int = 0) -> Any:
        '''Sends a complaint to the item.'''
    def reportComment(self, owner_id: int, comment_id: int, reason: int) -> Any:
        '''Sends a complaint to the item's comment.'''
    def restore(self, owner_id: int, item_id: int) -> Any:
        '''Restores recently deleted item'''
    def restoreComment(self, owner_id: int, comment_id: int) -> Any:
        '''Restores a recently deleted comment'''
    def search(self, owner_id: int, q: str, price_from: int, price_to: int, offset: int, album_id: int = 0, sort: int = 0, rev: int = 1, count: int = 20, extended: bool = '0', status: int = 0) -> Any:
        '''Searches market items in a community's catalog'''

class messages:
    def addChatUser(self, chat_id: int, user_id: int, visible_messages_count: int) -> Any:
        '''Adds a new user to a chat.'''
    def allowMessagesFromGroup(self, group_id: int, key: str) -> Any:
        '''Allows sending messages from community to the current user.'''
    def createChat(self, user_ids: List[int], title: str, group_id: int) -> Any:
        '''Creates a chat with several participants.'''
    def delete(self, message_ids: List[int], spam: bool, group_id: int, delete_for_all: bool = False) -> Any:
        '''Deletes one or more messages.'''
    def deleteChatPhoto(self, chat_id: int, group_id: int) -> Any:
        '''Deletes a chat's cover picture.'''
    def deleteConversation(self, user_id: int, peer_id: int, group_id: int) -> Any:
        '''Deletes all private messages in a conversation.'''
    def denyMessagesFromGroup(self, group_id: int) -> Any:
        '''Denies sending message from community to the current user.'''
    def edit(self, peer_id: int, message: str, lat: float, long: float, attachment: str, keep_forward_messages: bool, keep_snippets: bool, group_id: int, message_id: int, conversation_message_id: int, template: str, keyboard: str, dont_parse_links: bool = False) -> Any:
        '''Edits the message.'''
    def editChat(self, chat_id: int, title: str) -> Any:
        '''Edits the title of a chat.'''
    def getByConversationMessageId(self, peer_id: int, conversation_message_ids: List[int], extended: bool, fields: Dict[str, Any], group_id: int) -> Any:
        '''Returns messages by their IDs within the conversation.'''
    def getById(self, message_ids: List[int], extended: bool, fields: Dict[str, Any], group_id: int, preview_length: int = 0) -> Any:
        '''Returns messages by their IDs.'''
    def getChatPreview(self, peer_id: int, link: str, fields: Dict[str, Any]) -> Any: ...
    def getConversationMembers(self, peer_id: int, fields: Dict[str, Any], group_id: int) -> Any:
        '''Returns a list of IDs of users participating in a chat.'''
    def getConversations(self, extended: bool, start_message_id: int, fields: Dict[str, Any], group_id: int, offset: int = 0, count: int = 20, filter: str = 'all') -> Any:
        '''Returns a list of the current user's conversations.'''
    def getConversationsById(self, peer_ids: List[int], extended: bool, fields: Dict[str, Any], group_id: int) -> Any:
        '''Returns conversations by their IDs'''
    def getHistory(self, offset: int, user_id: int, peer_id: int, start_message_id: int, rev: int, extended: bool, fields: Dict[str, Any], group_id: int, count: int = 20) -> Any:
        '''Returns message history for the specified user or group chat.'''
    def getHistoryAttachments(self, peer_id: int, start_from: str, photo_sizes: bool, fields: Dict[str, Any], group_id: int, preserve_order: bool, media_type: str = 'photo', count: int = 30, max_forwards_level: int = 45) -> Any:
        '''Returns media files from the dialog or group chat.'''
    def getImportantMessages(self, offset: int, start_message_id: int, preview_length: int, fields: Dict[str, Any], extended: bool, group_id: int, count: int = 20) -> Any:
        '''Returns a list of user's important messages.'''
    def getInviteLink(self, peer_id: int, group_id: int, reset: bool = False) -> Any: ...
    def getLastActivity(self, user_id: int) -> Any:
        '''Returns a user's current status and date of last activity.'''
    def getLongPollHistory(self, ts: int, pts: int, preview_length: int, onlines: bool, fields: Dict[str, Any], max_msg_id: int, group_id: int, lp_version: int, credentials: bool, events_limit: int = 1000, msgs_limit: int = 200, last_n: int = 0) -> Any:
        '''Returns updates in user's private messages.'''
    def getLongPollServer(self, need_pts: bool, group_id: int, lp_version: int = 0) -> Any:
        '''Returns data required for connection to a Long Poll server.'''
    def isMessagesFromGroupAllowed(self, group_id: int, user_id: int) -> Any:
        '''Returns information whether sending messages from the community to current user is allowed.'''
    def joinChatByInviteLink(self, link: str) -> Any: ...
    def markAsAnsweredConversation(self, peer_id: int, group_id: int, answered: bool = 1) -> Any:
        '''Marks and unmarks conversations as unanswered.'''
    def markAsImportant(self, message_ids: List[int], important: int) -> Any:
        '''Marks and unmarks messages as important (starred).'''
    def markAsImportantConversation(self, peer_id: int, group_id: int, important: bool = 1) -> Any:
        '''Marks and unmarks conversations as important.'''
    def markAsRead(self, message_ids: List[int], peer_id: int, start_message_id: int, group_id: int, mark_conversation_as_read: bool) -> Any:
        '''Marks messages as read.'''
    def pin(self, peer_id: int, message_id: int) -> Any:
        '''Pin a message.'''
    def removeChatUser(self, chat_id: int, user_id: int, member_id: int) -> Any:
        '''Allows the current user to leave a chat or, if the current user started the chat, allows the user to remove another user from the chat.'''
    def restore(self, message_id: int, group_id: int) -> Any:
        '''Restores a deleted message.'''
    def search(self, q: str, peer_id: int, date: int, extended: bool, fields: List[str], group_id: int, preview_length: int = 0, offset: int = 0, count: int = 20) -> Any:
        '''Returns a list of the current user's private messages that match search criteria.'''
    def searchConversations(self, q: str, extended: bool, fields: Dict[str, Any], group_id: int, count: int = 20) -> Any:
        '''Returns a list of the current user's conversations that match search criteria.'''
    def send(self, user_id: int, random_id: int, peer_id: int, domain: str, chat_id: int, user_ids: List[int], message: str, lat: float, long: float, attachment: str, reply_to: int, forward_messages: List[int], sticker_id: int, group_id: int, keyboard: str, template: str, payload: str, subscribe_id: int, dont_parse_links: bool = False, disable_mentions: bool = False, intent: str = 'default') -> Any:
        '''Sends a message.'''
    def sendMessageEventAnswer(self, event_id: str, user_id: int, peer_id: int, event_data: str) -> Any: ...
    def setActivity(self, user_id: int, type: str, peer_id: int, group_id: int) -> Any:
        '''Changes the status of a user as typing in a conversation.'''
    def setChatPhoto(self, file: str) -> Any:
        '''Sets a previously-uploaded picture as the cover picture of a chat.'''
    def unpin(self, peer_id: int, group_id: int) -> Any: ...

class newsfeed:
    def addBan(self, user_ids: List[int], group_ids: List[int]) -> Any:
        '''Prevents news from specified users and communities from appearing in the current user's newsfeed.'''
    def deleteBan(self, user_ids: List[int], group_ids: List[int]) -> Any:
        '''Allows news from previously banned users and communities to be shown in the current user's newsfeed.'''
    def deleteList(self, list_id: int) -> Any: ...
    def get(self, filters: Dict[str, Any], return_banned: bool, start_time: int, end_time: int, max_photos: int, source_ids: str, start_from: str, count: int, fields: Dict[str, Any], section: str) -> Any:
        '''Returns data required to show newsfeed for the current user.'''
    def getBanned(self, extended: bool, fields: Dict[str, Any], name_case: str) -> Any:
        '''Returns a list of users and communities banned from the current user's newsfeed.'''
    def getComments(self, filters: Dict[str, Any], reposts: str, start_time: int, end_time: int, start_from: str, fields: Dict[str, Any], count: int = 30, last_comments_count: int = 0) -> Any:
        '''Returns a list of comments in the current user's newsfeed.'''
    def getLists(self, list_ids: List[int], extended: bool = 0) -> Any:
        '''Returns a list of newsfeeds followed by the current user.'''
    def getMentions(self, owner_id: int, start_time: int, end_time: int, offset: int, count: int = 20) -> Any:
        '''Returns a list of posts on user walls in which the current user is mentioned.'''
    def getRecommended(self, start_time: int, end_time: int, max_photos: int, start_from: str, count: int, fields: Dict[str, Any]) -> Any:
        ''', Returns a list of newsfeeds recommended to the current user.'''
    def getSuggestedSources(self, offset: int, shuffle: bool, fields: Dict[str, Any], count: int = 20) -> Any:
        '''Returns communities and users that current user is suggested to follow.'''
    def ignoreItem(self, type: str, owner_id: int, item_id: int) -> Any:
        '''Hides an item from the newsfeed.'''
    def saveList(self, list_id: int, title: str, source_ids: List[int], no_reposts: bool) -> Any:
        '''Creates and edits user newsfeed lists'''
    def search(self, q: str, extended: bool, latitude: float, longitude: float, start_time: int, end_time: int, start_from: str, fields: Dict[str, Any], count: int = 30) -> Any:
        '''Returns search results by statuses.'''
    def unignoreItem(self, type: str, owner_id: int, item_id: int, track_code: str) -> Any:
        '''Returns a hidden item to the newsfeed.'''
    def unsubscribe(self, type: str, owner_id: int, item_id: int) -> Any:
        '''Unsubscribes the current user from specified newsfeeds.'''

class notes:
    def add(self, title: str, text: str, privacy_view: List[str], privacy_comment: List[str]) -> Any:
        '''Creates a new note for the current user.'''
    def createComment(self, note_id: int, owner_id: int, reply_to: int, message: str, guid: str) -> Any:
        '''Adds a new comment on a note.'''
    def delete(self, note_id: int) -> Any:
        '''Deletes a note of the current user.'''
    def deleteComment(self, comment_id: int, owner_id: int) -> Any:
        '''Deletes a comment on a note.'''
    def edit(self, note_id: int, title: str, text: str, privacy_view: List[str], privacy_comment: List[str]) -> Any:
        '''Edits a note of the current user.'''
    def editComment(self, comment_id: int, owner_id: int, message: str) -> Any:
        '''Edits a comment on a note.'''
    def get(self, note_ids: List[int], user_id: int, offset: int = 0, count: int = 20, sort: int = 0) -> Any:
        '''Returns a list of notes created by a user.'''
    def getById(self, note_id: int, owner_id: int, need_wiki: bool = 0) -> Any:
        '''Returns a note by its ID.'''
    def getComments(self, note_id: int, owner_id: int, sort: int = 0, offset: int = 0, count: int = 20) -> Any:
        '''Returns a list of comments on a note.'''
    def restoreComment(self, comment_id: int, owner_id: int) -> Any:
        '''Restores a deleted comment on a note.'''

class notifications:
    def get(self, start_from: str, filters: List[str], start_time: int, end_time: int, count: int = 30) -> Any:
        '''Returns a list of notifications about other users' feedback to the current user's wall posts.'''
    def markAsViewed(self) -> Any:
        '''Resets the counter of new notifications about other users' feedback to the current user's wall posts.'''
    def sendMessage(self, user_ids: List[int], message: str, fragment: str, group_id: int, random_id: int) -> Any: ...

class orders:
    def cancelSubscription(self, user_id: int, subscription_id: int, pending_cancel: bool = 0) -> Any: ...
    def changeState(self, order_id: int, action: str, app_order_id: int, test_mode: bool) -> Any:
        '''Changes order status.'''
    def get(self, test_mode: bool, offset: int = 0, count: int = 100) -> Any:
        '''Returns a list of orders.'''
    def getAmount(self, user_id: int, votes: List[str]) -> Any: ...
    def getById(self, order_id: int, order_ids: List[int], test_mode: bool) -> Any:
        '''Returns information about orders by their IDs.'''
    def getUserSubscriptionById(self, user_id: int, subscription_id: int) -> Any: ...
    def getUserSubscriptions(self, user_id: int) -> Any: ...
    def updateSubscription(self, user_id: int, subscription_id: int, price: int) -> Any: ...

class pages:
    def clearCache(self, url: str) -> Any:
        '''Allows to clear the cache of particular 'external' pages which may be attached to VK posts.'''
    def get(self, owner_id: int, page_id: int, site_preview: bool, title: str, need_source: bool, need_html: bool) -> Any:
        '''Returns information about a wiki page.'''
    def getHistory(self, page_id: int, group_id: int, user_id: int) -> Any:
        '''Returns a list of all previous versions of a wiki page.'''
    def getTitles(self, group_id: int) -> Any:
        '''Returns a list of wiki pages in a group.'''
    def getVersion(self, version_id: int, group_id: int, user_id: int, need_html: bool) -> Any:
        '''Returns the text of one of the previous versions of a wiki page.'''
    def parseWiki(self, text: str, group_id: int) -> Any:
        '''Returns HTML representation of the wiki markup.'''
    def save(self, text: str, page_id: int, group_id: int, user_id: int, title: str) -> Any:
        '''Saves the text of a wiki page.'''
    def saveAccess(self, page_id: int, group_id: int, user_id: int, view: int, edit: int) -> Any:
        '''Saves modified read and edit access settings for a wiki page.'''

class photos:
    def confirmTag(self, owner_id: int, photo_id: str, tag_id: int) -> Any:
        '''Confirms a tag on a photo.'''
    def copy(self, owner_id: int, photo_id: int, access_key: str) -> Any:
        '''Allows to copy a photo to the "Saved photos" album'''
    def createAlbum(self, title: str, group_id: int, description: str, privacy_view: List[str], privacy_comment: List[str], upload_by_admins_only: bool, comments_disabled: bool) -> Any:
        '''Creates an empty photo album.'''
    def createComment(self, owner_id: int, photo_id: int, message: str, attachments: List[str], from_group: bool, reply_to_comment: int, sticker_id: int, access_key: str, guid: str) -> Any:
        '''Adds a new comment on the photo.'''
    def delete(self, owner_id: int, photo_id: int) -> Any:
        '''Deletes a photo.'''
    def deleteAlbum(self, album_id: int, group_id: int) -> Any:
        '''Deletes a photo album belonging to the current user.'''
    def deleteComment(self, owner_id: int, comment_id: int) -> Any:
        '''Deletes a comment on the photo.'''
    def edit(self, owner_id: int, photo_id: int, caption: str, latitude: float, longitude: float, place_str: str, foursquare_id: str, delete_place: bool) -> Any:
        '''Edits the caption of a photo.'''
    def editAlbum(self, album_id: int, title: str, description: str, owner_id: int, privacy_view: List[str], privacy_comment: List[str], upload_by_admins_only: bool, comments_disabled: bool) -> Any:
        '''Edits information about a photo album.'''
    def editComment(self, owner_id: int, comment_id: int, message: str, attachments: List[str]) -> Any:
        '''Edits a comment on a photo.'''
    def get(self, owner_id: int, album_id: str, photo_ids: List[str], rev: bool, extended: bool, feed_type: str, feed: int, photo_sizes: bool, offset: int, count: int = 50) -> Any:
        '''Returns a list of a user's or community's photos.'''
    def getAlbums(self, owner_id: int, album_ids: List[int], offset: int, count: int, need_system: bool, need_covers: bool, photo_sizes: bool) -> Any:
        '''Returns a list of a user's or community's photo albums.'''
    def getAlbumsCount(self, user_id: int, group_id: int) -> Any:
        '''Returns the number of photo albums belonging to a user or community.'''
    def getAll(self, owner_id: int, extended: bool, offset: int, photo_sizes: bool, no_service_albums: bool, need_hidden: bool, skip_hidden: bool, count: int = 20) -> Any:
        '''Returns a list of photos belonging to a user or community, in reverse chronological order.'''
    def getAllComments(self, owner_id: int, album_id: int, need_likes: bool, offset: int, count: int) -> Any:
        '''Returns a list of comments on a specific photo album or all albums of the user sorted in reverse chronological order.'''
    def getById(self, photos: List[str], extended: bool, photo_sizes: bool) -> Any:
        '''Returns information about photos by their IDs.'''
    def getChatUploadServer(self, chat_id: int, crop_x: int, crop_y: int, crop_width: int) -> Any:
        '''Returns an upload link for chat cover pictures.'''
    def getComments(self, owner_id: int, photo_id: int, need_likes: bool, start_comment_id: int, offset: int, sort: str, access_key: str, extended: bool, fields: Dict[str, Any], count: int = '20') -> Any:
        '''Returns a list of comments on a photo.'''
    def getMarketAlbumUploadServer(self, group_id: int) -> Any:
        '''Returns the server address for market album photo upload.'''
    def getMarketUploadServer(self, group_id: int, main_photo: bool, crop_x: int, crop_y: int, crop_width: int) -> Any:
        '''Returns the server address for market photo upload.'''
    def getMessagesUploadServer(self, peer_id: int) -> Any:
        '''Returns the server address for photo upload in a private message for a user.'''
    def getNewTags(self, offset: int, count: int = 20) -> Any:
        '''Returns a list of photos with tags that have not been viewed.'''
    def getOwnerCoverPhotoUploadServer(self, group_id: int, crop_x: int = 0, crop_y: int = 0, crop_x2: int = 795, crop_y2: int = 200) -> Any:
        '''Returns the server address for owner cover upload.'''
    def getOwnerPhotoUploadServer(self, owner_id: int) -> Any:
        '''Returns an upload server address for a profile or community photo.'''
    def getTags(self, owner_id: int, photo_id: int, access_key: str) -> Any:
        '''Returns a list of tags on a photo.'''
    def getUploadServer(self, group_id: int, album_id: int) -> Any:
        '''Returns the server address for photo upload.'''
    def getUserPhotos(self, user_id: int, offset: int, extended: bool, sort: str, count: int = 20) -> Any:
        '''Returns a list of photos in which a user is tagged.'''
    def getWallUploadServer(self, group_id: int) -> Any:
        '''Returns the server address for photo upload onto a user's wall.'''
    def makeCover(self, owner_id: int, photo_id: int, album_id: int) -> Any:
        '''Makes a photo into an album cover.'''
    def move(self, owner_id: int, target_album_id: int, photo_id: int) -> Any:
        '''Moves a photo from one album to another.'''
    def putTag(self, owner_id: int, photo_id: int, user_id: int, x: float, y: float, x2: float, y2: float) -> Any:
        '''Adds a tag on the photo.'''
    def removeTag(self, owner_id: int, photo_id: int, tag_id: int) -> Any:
        '''Removes a tag from a photo.'''
    def reorderAlbums(self, owner_id: int, album_id: int, before: int, after: int) -> Any:
        '''Reorders the album in the list of user albums.'''
    def reorderPhotos(self, owner_id: int, photo_id: int, before: int, after: int) -> Any:
        '''Reorders the photo in the list of photos of the user album.'''
    def report(self, owner_id: int, photo_id: int, reason: int) -> Any:
        '''Reports (submits a complaint about) a photo.'''
    def reportComment(self, owner_id: int, comment_id: int, reason: int) -> Any:
        '''Reports (submits a complaint about) a comment on a photo.'''
    def restore(self, owner_id: int, photo_id: int) -> Any:
        '''Restores a deleted photo.'''
    def restoreComment(self, owner_id: int, comment_id: int) -> Any:
        '''Restores a deleted comment on a photo.'''
    def save(self, album_id: int, group_id: int, server: int, photos_list: str, hash: str, latitude: float, longitude: float, caption: str) -> Any:
        '''Saves photos after successful uploading.'''
    def saveMarketAlbumPhoto(self, group_id: int, photo: str, server: int, hash: str) -> Any:
        '''Saves market album photos after successful uploading.'''
    def saveMarketPhoto(self, group_id: int, photo: str, server: int, hash: str, crop_data: str, crop_hash: str) -> Any:
        '''Saves market photos after successful uploading.'''
    def saveMessagesPhoto(self, photo: str, server: int, hash: str) -> Any:
        '''Saves a photo after being successfully uploaded. URL obtained with [vk.com/dev/photos.getMessagesUploadServer|photos.getMessagesUploadServer] method.'''
    def saveOwnerCoverPhoto(self, hash: str, photo: str) -> Any:
        '''Saves cover photo after successful uploading.'''
    def saveOwnerPhoto(self, server: str, hash: str, photo: str) -> Any:
        '''Saves a profile or community photo. Upload URL can be got with the [vk.com/dev/photos.getOwnerPhotoUploadServer|photos.getOwnerPhotoUploadServer] method.'''
    def saveWallPhoto(self, user_id: int, group_id: int, photo: str, server: int, hash: str, latitude: float, longitude: float, caption: str) -> Any:
        '''Saves a photo to a user's or community's wall after being uploaded.'''
    def search(self, q: str, lat: float, long: float, start_time: int, end_time: int, sort: int, offset: int, count: int = 100, radius: int = 5000) -> Any:
        '''Returns a list of photos.'''

class podcasts:
    def clearRecentSearches(self) -> Any: ...
    def getPopular(self) -> Any: ...
    def getRecentSearchRequests(self) -> Any: ...
    def search(self, search_string: str, offset: int, count: int) -> Any: ...

class polls:
    def addVote(self, owner_id: int, poll_id: int, answer_ids: List[int], is_board: bool) -> Any:
        '''Adds the current user's vote to the selected answer in the poll.'''
    def create(self, question: str, is_anonymous: bool, is_multiple: bool, end_date: int, owner_id: int, add_answers: str, photo_id: int, background_id: str, disable_unvote: bool) -> Any:
        '''Creates polls that can be attached to the users' or communities' posts.'''
    def deleteVote(self, owner_id: int, poll_id: int, answer_id: int, is_board: bool) -> Any:
        '''Deletes the current user's vote from the selected answer in the poll.'''
    def edit(self, owner_id: int, poll_id: int, question: str, add_answers: str, edit_answers: str, delete_answers: str, end_date: int, photo_id: int, background_id: str) -> Any:
        '''Edits created polls'''
    def getById(self, owner_id: int, is_board: bool, poll_id: int, extended: bool, fields: List[str], friends_count: int = 3, name_case: str = 'nom') -> Any:
        '''Returns detailed information about a poll by its ID.'''
    def getVoters(self, owner_id: int, poll_id: int, answer_ids: List[int], is_board: bool, friends_only: bool, offset: int, count: int, fields: Dict[str, Any], name_case: str) -> Any:
        '''Returns a list of IDs of users who selected specific answers in the poll.'''

class prettyCards:
    def create(self, owner_id: int, photo: str, title: str, link: str, price: str, price_old: str, button: str) -> Any: ...
    def delete(self, owner_id: int, card_id: int) -> Any: ...
    def edit(self, owner_id: int, card_id: int, photo: str, title: str, link: str, price: str, price_old: str, button: str) -> Any: ...
    def get(self, owner_id: int, offset: int = 0, count: int = 10) -> Any: ...
    def getById(self, owner_id: int, card_ids: List[int]) -> Any: ...
    def getUploadURL(self) -> Any: ...

class search:
    def getHints(self, q: str, offset: int, filters: List[str], fields: List[str], limit: int = 9, search_global: bool = 1) -> Any:
        '''Allows the programmer to do a quick search for any substring.'''

class secure:
    def addAppEvent(self, user_id: int, activity_id: int, value: int) -> Any:
        '''Adds user activity information to an application'''
    def checkToken(self, token: str, ip: str) -> Any:
        '''Checks the user authentication in 'IFrame' and 'Flash' apps using the 'access_token' parameter.'''
    def getAppBalance(self) -> Any:
        '''Returns payment balance of the application in hundredth of a vote.'''
    def getSMSHistory(self, user_id: int, date_from: int, date_to: int, limit: int = 1000) -> Any:
        '''Shows a list of SMS notifications sent by the application using [vk.com/dev/secure.sendSMSNotification|secure.sendSMSNotification] method.'''
    def getTransactionsHistory(self, type: int, uid_from: int, uid_to: int, date_from: int, date_to: int, limit: int = 1000) -> Any:
        '''Shows history of votes transaction between users and the application.'''
    def getUserLevel(self, user_ids: List[int]) -> Any:
        '''Returns one of the previously set game levels of one or more users in the application.'''
    def giveEventSticker(self, user_ids: List[int], achievement_id: int) -> Any:
        '''Opens the game achievement and gives the user a sticker'''
    def sendNotification(self, user_ids: List[int], user_id: int, message: str) -> Any:
        '''Sends notification to the user.'''
    def sendSMSNotification(self, user_id: int, message: str) -> Any:
        '''Sends 'SMS' notification to a user's mobile device.'''
    def setCounter(self, counters: List[str], user_id: int, counter: int, increment: bool) -> Any:
        '''Sets a counter which is shown to the user in bold in the left menu.'''

class stats:
    def get(self, group_id: int, app_id: int, timestamp_from: int, timestamp_to: int, intervals_count: int, filters: List[str], stats_groups: List[str], interval: str = 'day', extended: bool = True) -> Any:
        '''Returns statistics of a community or an application.'''
    def getPostReach(self, owner_id: str, post_ids: List[int]) -> Any:
        '''Returns stats for a wall post.'''
    def trackVisitor(self, id: str) -> Any: ...

class status:
    def get(self, user_id: int, group_id: int) -> Any:
        '''Returns data required to show the status of a user or community.'''
    def set(self, text: str, group_id: int) -> Any:
        '''Sets a new status for the current user.'''

class storage:
    def get(self, key: str, keys: List[str], user_id: int) -> Any:
        '''Returns a value of variable with the name set by key parameter.'''
    def getKeys(self, user_id: int, offset: int = 0, count: int = 100) -> Any:
        '''Returns the names of all variables.'''
    def set(self, key: str, value: str, user_id: int) -> Any:
        '''Saves a value of variable with the name set by 'key' parameter.'''

class stories:
    def banOwner(self, owners_ids: List[int]) -> Any:
        '''Allows to hide stories from chosen sources from current user's feed.'''
    def delete(self, owner_id: int, story_id: int, stories: List[str]) -> Any:
        '''Allows to delete story.'''
    def get(self, owner_id: int, fields: Dict[str, Any], extended: bool = False) -> Any:
        '''Returns stories available for current user.'''
    def getBanned(self, extended: bool, fields: Dict[str, Any]) -> Any:
        '''Returns list of sources hidden from current user's feed.'''
    def getById(self, stories: List[str], fields: Dict[str, Any], extended: bool = False) -> Any:
        '''Returns story by its ID.'''
    def getPhotoUploadServer(self, add_to_news: bool, user_ids: List[int], reply_to_story: str, link_text: str, link_url: str, group_id: int, clickable_stickers: str) -> Any:
        '''Returns URL for uploading a story with photo.'''
    def getReplies(self, owner_id: int, story_id: int, access_key: str, fields: Dict[str, Any], extended: bool = False) -> Any:
        '''Returns replies to the story.'''
    def getStats(self, owner_id: int, story_id: int) -> Any:
        '''Returns stories available for current user.'''
    def getVideoUploadServer(self, add_to_news: bool, user_ids: List[int], reply_to_story: str, link_text: str, link_url: str, group_id: int, clickable_stickers: str) -> Any:
        '''Allows to receive URL for uploading story with video.'''
    def getViewers(self, owner_id: int, story_id: int, count: int = 100, offset: int = 0, extended: bool = 0) -> Any:
        '''Returns a list of story viewers.'''
    def hideAllReplies(self, owner_id: int, group_id: int) -> Any:
        '''Hides all replies in the last 24 hours from the user to current user's stories.'''
    def hideReply(self, owner_id: int, story_id: int) -> Any:
        '''Hides the reply to the current user's story.'''
    def save(self, upload_results: List[str]) -> Any: ...
    def search(self, q: str, place_id: int, latitude: float, longitude: float, radius: int, mentioned_id: int, extended: bool, fields: List[str], count: int = 20) -> Any: ...
    def sendInteraction(self, access_key: str, message: str, is_broadcast: bool = False, is_anonymous: bool = False, unseen_marker: bool = False) -> Any: ...
    def unbanOwner(self, owners_ids: List[int]) -> Any:
        '''Allows to show stories from hidden sources in current user's feed.'''

class streaming:
    def getServerUrl(self) -> Any:
        '''Allows to receive data for the connection to Streaming API.'''
    def setSettings(self, monthly_tier: str) -> Any: ...

class users:
    def get(self, user_ids: List[str], fields: Dict[str, Any], name_case: str) -> Any:
        '''Returns detailed information on users.'''
    def getFollowers(self, user_id: int, offset: int, fields: Dict[str, Any], name_case: str, count: int = 100) -> Any:
        '''Returns a list of IDs of followers of the user in question, sorted by date added, most recent first.'''
    def getSubscriptions(self, user_id: int, extended: bool, offset: int, fields: Dict[str, Any], count: int = 20) -> Any:
        '''Returns a list of IDs of users and communities followed by the user.'''
    def report(self, user_id: int, type: str, comment: str) -> Any:
        '''Reports (submits a complain about) a user.'''
    def search(self, q: str, sort: int, offset: int, fields: Dict[str, Any], city: int, country: int, hometown: str, university_country: int, university: int, university_year: int, university_faculty: int, university_chair: int, sex: int, status: int, age_from: int, age_to: int, birth_day: int, birth_month: int, birth_year: int, online: bool, has_photo: bool, school_country: int, school_city: int, school_class: int, school: int, school_year: int, religion: str, company: str, position: str, group_id: int, from_list: List[str], count: int = 20) -> Any:
        '''Returns a list of users matching the search criteria.'''

class utils:
    def checkLink(self, url: str) -> Any:
        '''Checks whether a link is blocked in VK.'''
    def deleteFromLastShortened(self, key: str) -> Any:
        '''Deletes shortened link from user's list.'''
    def getLastShortenedLinks(self, count: int = 10, offset: int = 0) -> Any:
        '''Returns a list of user's shortened links.'''
    def getLinkStats(self, key: str, access_key: str, source: str = 'vk_cc', interval: str = 'day', intervals_count: int = 1, extended: bool = False) -> Any:
        '''Returns stats data for shortened link.'''
    def getServerTime(self) -> Any:
        '''Returns the current time of the VK server.'''
    def getShortLink(self, url: str, private: bool = False) -> Any:
        '''Allows to receive a link shortened via vk.cc.'''
    def resolveScreenName(self, screen_name: str) -> Any:
        '''Detects a type of object (e.g., user, community, application) and its ID by screen name.'''

class video:
    def add(self, target_id: int, video_id: int, owner_id: int) -> Any:
        '''Adds a video to a user or community page.'''
    def addAlbum(self, group_id: int, title: str, privacy: List[str]) -> Any:
        '''Creates an empty album for videos.'''
    def addToAlbum(self, target_id: int, album_id: int, album_ids: List[int], owner_id: int, video_id: int) -> Any: ...
    def createComment(self, owner_id: int, video_id: int, message: str, attachments: List[str], from_group: bool, reply_to_comment: int, sticker_id: int, guid: str) -> Any:
        '''Adds a new comment on a video.'''
    def delete(self, video_id: int, owner_id: int, target_id: int) -> Any:
        '''Deletes a video from a user or community page.'''
    def deleteAlbum(self, group_id: int, album_id: int) -> Any:
        '''Deletes a video album.'''
    def deleteComment(self, owner_id: int, comment_id: int) -> Any:
        '''Deletes a comment on a video.'''
    def edit(self, owner_id: int, video_id: int, name: str, desc: str, privacy_view: List[str], privacy_comment: List[str], no_comments: bool, repeat: bool) -> Any:
        '''Edits information about a video on a user or community page.'''
    def editAlbum(self, group_id: int, album_id: int, title: str, privacy: List[str]) -> Any:
        '''Edits the title of a video album.'''
    def editComment(self, owner_id: int, comment_id: int, message: str, attachments: List[str]) -> Any:
        '''Edits the text of a comment on a video.'''
    def get(self, owner_id: int, videos: List[str], album_id: int, offset: int, extended: bool, count: int = 100) -> Any:
        '''Returns detailed information about videos.'''
    def getAlbumById(self, owner_id: int, album_id: int) -> Any:
        '''Returns video album info'''
    def getAlbums(self, owner_id: int, offset: int, extended: bool, count: int = 50, need_system: bool = 0) -> Any:
        '''Returns a list of video albums owned by a user or community.'''
    def getAlbumsByVideo(self, target_id: int, owner_id: int, video_id: int, extended: bool = 0) -> Any: ...
    def getComments(self, owner_id: int, video_id: int, need_likes: bool, start_comment_id: int, offset: int, sort: str, extended: bool, fields: List[str], count: int = 20) -> Any:
        '''Returns a list of comments on a video.'''
    def removeFromAlbum(self, target_id: int, album_id: int, album_ids: List[int], owner_id: int, video_id: int) -> Any: ...
    def reorderAlbums(self, owner_id: int, album_id: int, before: int, after: int) -> Any:
        '''Reorders the album in the list of user video albums.'''
    def reorderVideos(self, target_id: int, album_id: int, owner_id: int, video_id: int, before_owner_id: int, before_video_id: int, after_owner_id: int, after_video_id: int) -> Any:
        '''Reorders the video in the video album.'''
    def report(self, owner_id: int, video_id: int, reason: int, comment: str, search_query: str) -> Any:
        '''Reports (submits a complaint about) a video.'''
    def reportComment(self, owner_id: int, comment_id: int, reason: int) -> Any:
        '''Reports (submits a complaint about) a comment on a video.'''
    def restore(self, video_id: int, owner_id: int) -> Any:
        '''Restores a previously deleted video.'''
    def restoreComment(self, owner_id: int, comment_id: int) -> Any:
        '''Restores a previously deleted comment on a video.'''
    def save(self, name: str, description: str, is_private: bool, wallpost: bool, link: str, group_id: int, album_id: int, privacy_view: List[str], privacy_comment: List[str], no_comments: bool, repeat: bool, compression: bool) -> Any:
        '''Returns a server address (required for upload) and video data.'''
    def search(self, q: str, sort: int, hd: int, adult: bool, filters: List[str], search_own: bool, offset: int, longer: int, shorter: int, count: int = 20, extended: bool = 0) -> Any:
        '''Returns a list of videos under the set search criterion.'''

class wall:
    def checkCopyrightLink(self, link: str) -> Any: ...
    def closeComments(self, owner_id: int, post_id: int) -> Any: ...
    def createComment(self, owner_id: int, post_id: int, from_group: int, message: str, reply_to_comment: int, attachments: List[str], sticker_id: int, guid: str) -> Any:
        '''Adds a comment to a post on a user wall or community wall.'''
    def delete(self, owner_id: int, post_id: int) -> Any:
        '''Deletes a post from a user wall or community wall.'''
    def deleteComment(self, owner_id: int, comment_id: int) -> Any:
        '''Deletes a comment on a post on a user wall or community wall.'''
    def edit(self, owner_id: int, post_id: int, friends_only: bool, message: str, attachments: List[str], services: str, signed: bool, publish_date: int, lat: float, long: float, place_id: int, mark_as_ads: bool, close_comments: bool, poster_bkg_id: int, poster_bkg_owner_id: int, poster_bkg_access_hash: str, copyright: str) -> Any:
        '''Edits a post on a user wall or community wall.'''
    def editAdsStealth(self, owner_id: int, post_id: int, message: str, attachments: List[str], signed: bool, lat: float, long: float, place_id: int, link_button: str, link_title: str, link_image: str, link_video: str) -> Any:
        '''Allows to edit hidden post.'''
    def editComment(self, owner_id: int, comment_id: int, message: str, attachments: List[str]) -> Any:
        '''Edits a comment on a user wall or community wall.'''
    def get(self, owner_id: int, domain: str, offset: int, count: int, filter: str, extended: bool, fields: Dict[str, Any]) -> Any:
        '''Returns a list of posts on a user wall or community wall.'''
    def getById(self, posts: List[str], extended: bool, fields: Dict[str, Any], copy_history_depth: int = 2) -> Any:
        '''Returns a list of posts from user or community walls by their IDs.'''
    def getComment(self, owner_id: int, comment_id: int, extended: bool, fields: Dict[str, Any]) -> Any:
        '''Returns a comment on a post on a user wall or community wall.'''
    def getComments(self, owner_id: int, post_id: int, need_likes: bool, start_comment_id: int, offset: int, count: int, sort: str, preview_length: int, extended: bool, fields: Dict[str, Any], comment_id: int, thread_items_count: int = 0) -> Any:
        '''Returns a list of comments on a post on a user wall or community wall.'''
    def getReposts(self, owner_id: int, post_id: int, offset: int, count: int = 20) -> Any:
        '''Returns information about reposts of a post on user wall or community wall.'''
    def openComments(self, owner_id: int, post_id: int) -> Any: ...
    def pin(self, owner_id: int, post_id: int) -> Any:
        '''Pins the post on wall.'''
    def post(self, owner_id: int, friends_only: bool, from_group: bool, message: str, attachments: List[str], services: str, signed: bool, publish_date: int, lat: float, long: float, place_id: int, post_id: int, guid: str, close_comments: bool, mute_notifications: bool, copyright: str, mark_as_ads: bool = False) -> Any:
        '''Adds a new post on a user wall or community wall. Can also be used to publish suggested or scheduled posts.'''
    def postAdsStealth(self, owner_id: int, message: str, attachments: List[str], signed: bool, lat: float, long: float, place_id: int, guid: str, link_button: str, link_title: str, link_image: str, link_video: str) -> Any:
        '''Allows to create hidden post which will not be shown on the community's wall and can be used for creating an ad with type "Community post".'''
    def reportComment(self, owner_id: int, comment_id: int, reason: int) -> Any:
        '''Reports (submits a complaint about) a comment on a post on a user wall or community wall.'''
    def reportPost(self, owner_id: int, post_id: int, reason: int) -> Any:
        '''Reports (submits a complaint about) a post on a user wall or community wall.'''
    def repost(self, object: str, message: str, group_id: int, mute_notifications: bool, mark_as_ads: bool = False) -> Any:
        '''Reposts (copies) an object to a user wall or community wall.'''
    def restore(self, owner_id: int, post_id: int) -> Any:
        '''Restores a post deleted from a user wall or community wall.'''
    def restoreComment(self, owner_id: int, comment_id: int) -> Any:
        '''Restores a comment deleted from a user wall or community wall.'''
    def search(self, owner_id: int, domain: str, query: str, owners_only: bool, extended: bool, fields: Dict[str, Any], count: int = 20, offset: int = 0) -> Any:
        '''Allows to search posts on user or community walls.'''
    def unpin(self, owner_id: int, post_id: int) -> Any:
        '''Unpins the post on wall.'''

class widgets:
    def getComments(self, widget_api_id: int, url: str, page_id: str, fields: Dict[str, Any], order: str = 'date', offset: int = 0, count: int = 10) -> Any:
        '''Gets a list of comments for the page added through the [vk.com/dev/Comments|Comments widget].'''
    def getPages(self, widget_api_id: int, order: str = 'friend_likes', period: str = 'week', offset: int = 0, count: int = 10) -> Any:
        '''Gets a list of application/site pages where the [vk.com/dev/Comments|Comments widget] or [vk.com/dev/Like|Like widget] is installed.'''
