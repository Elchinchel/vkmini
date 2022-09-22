class VkResponseException(Exception):
    request_data: dict
    error_code: int
    error_msg: str
    error_data: dict

    def __new__(cls, error: dict, request_data: dict = {}):
        obj = Exception.__new__(_error_map.get(error['error_code'], cls))
        obj.__init__(error, request_data)
        return obj

    def __reduce_ex__(self, _):
        return self.__class__, (self.error_data, self.request_data)

    def __init__(self, error: dict, request_data: dict = {}):
        self.error_code = error['error_code']
        self.error_msg = error['error_msg']
        self.request_data = request_data
        self.error_data = error

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.error_code})'

    def __str__(self) -> str:
        info = f'Ошибка ВК #{self.error_code}: {self.error_msg}'
        if self.request_data:
            info += f'\nПараметры запроса: {self.request_data}'
        return info

    def get_short_str(self) -> str:
        return f'#{self.error_code}: {self.error_msg}'


class NetworkError(Exception):
    '''Ошибка сети при выполнении запроса'''
    code: int

    def __init__(self, code: int):
        self.code = code


class TokenInvalid(VkResponseException):
    '''
    Общая ошибка недействительного токена для групп, пользователей
    и приложений (коды 5, 27, 28)
    '''


class VkErrorUnknown(VkResponseException):  # общая ошибка
    '''(код 1) Unknown error occurred'''

class VkErrorDisabled(VkResponseException):  # общая ошибка
    '''(код 2) Application is disabled. Enable your application or use test mode'''

class VkErrorMethod(VkResponseException):  # общая ошибка
    '''(код 3) Unknown method passed'''

class VkErrorSignature(VkResponseException):  # общая ошибка
    '''(код 4) Incorrect signature'''

class VkErrorAuth(TokenInvalid):  # общая ошибка
    '''(код 5) User authorization failed'''

class VkErrorTooMany(VkResponseException):  # общая ошибка
    '''(код 6) Too many requests per second'''

class VkErrorPermission(VkResponseException):  # общая ошибка
    '''(код 7) Permission to perform this action is denied'''

class VkErrorRequest(VkResponseException):  # общая ошибка
    '''(код 8) Invalid request'''

class VkErrorFlood(VkResponseException):  # общая ошибка
    '''(код 9) Flood control'''

class VkErrorServer(VkResponseException):  # общая ошибка
    '''(код 10) Internal server error'''

class VkErrorEnabledInTest(VkResponseException):  # общая ошибка
    '''(код 11) In test mode application should be disabled or user should be authorized'''

class VkErrorCompile(VkResponseException):
    '''(код 12) Unable to compile code'''

class VkErrorRuntime(VkResponseException):
    '''(код 13) Runtime error occurred during code invocation'''

class VkErrorCaptcha(VkResponseException):  # общая ошибка
    '''(код 14) Captcha needed'''

class VkErrorAccess(VkResponseException):  # общая ошибка
    '''(код 15) Access denied'''

class VkErrorAuthHttps(VkResponseException):  # общая ошибка
    '''(код 16) HTTP authorization failed'''

class VkErrorAuthValidation(VkResponseException):  # общая ошибка
    '''(код 17) Validation required'''

class VkErrorUserDeleted(VkResponseException):  # общая ошибка
    '''(код 18) User was deleted or banned'''

class VkErrorBlocked(VkResponseException):
    '''(код 19) Content blocked'''

class VkErrorMethodPermission(VkResponseException):  # общая ошибка
    '''(код 20) Permission to perform this action is denied for non-standalone applications'''

class VkErrorMethodAds(VkResponseException):  # общая ошибка
    '''(код 21) Permission to perform this action is allowed only for standalone and OpenAPI applications'''

class VkErrorUpload(VkResponseException):
    '''(код 22) Upload error'''

class VkErrorMethodDisabled(VkResponseException):  # общая ошибка
    '''(код 23) This method was disabled'''

class VkErrorNeedConfirmation(VkResponseException):  # общая ошибка
    '''(код 24) Confirmation required'''

class VkErrorNeedTokenConfirmation(VkResponseException):  # общая ошибка
    '''(код 25) Token confirmation required'''

class VkErrorGroupAuth(TokenInvalid):  # общая ошибка
    '''(код 27) Group authorization failed'''

class VkErrorAppAuth(TokenInvalid):  # общая ошибка
    '''(код 28) Application authorization failed'''

class VkErrorRateLimit(VkResponseException):  # общая ошибка
    '''(код 29) Rate limit reached'''

class VkErrorPrivateProfile(VkResponseException):  # общая ошибка
    '''(код 30) This profile is private'''

class VkErrorNotImplementedYet(VkResponseException):  # общая ошибка
    '''(код 33) Not implemented yet'''

class VkErrorClientUpdateNeeded(VkResponseException):
    '''(код 35) Client update needed'''

class VkErrorParam(VkResponseException):  # общая ошибка
    '''(код 100) One of the parameters specified was missing or invalid'''

class VkErrorParamApiId(VkResponseException):  # общая ошибка
    '''(код 101) Invalid application API ID'''

class VkErrorLimits(VkResponseException):
    '''(код 103) Out of limits'''

class VkErrorNotFound(VkResponseException):
    '''(код 104) Not found'''

class VkErrorSaveFile(VkResponseException):
    '''(код 105) Couldn't save file'''

class VkErrorActionFailed(VkResponseException):
    '''(код 106) Unable to process action'''

class VkErrorParamUserId(VkResponseException):  # общая ошибка
    '''(код 113) Invalid user id'''

class VkErrorParamAlbumId(VkResponseException):
    '''(код 114) Invalid album id'''

class VkErrorParamServer(VkResponseException):
    '''(код 118) Invalid server'''

class VkErrorParamTitle(VkResponseException):
    '''(код 119) Invalid title'''

class VkErrorParamHash(VkResponseException):
    '''(код 121) Invalid hash'''

class VkErrorParamPhotos(VkResponseException):
    '''(код 122) Invalid photos'''

class VkErrorParamGroupId(VkResponseException):
    '''(код 125) Invalid group id'''

class VkErrorParamPhoto(VkResponseException):
    '''(код 129) Invalid photo'''

class VkErrorParamPageId(VkResponseException):
    '''(код 140) Page not found'''

class VkErrorAccessPage(VkResponseException):
    '''(код 141) Access to page denied'''

class VkErrorMobileNotActivated(VkResponseException):
    '''(код 146) The mobile number of the user is unknown'''

class VkErrorInsufficientFunds(VkResponseException):
    '''(код 147) Application has insufficient funds'''

class VkErrorAccessMenu(VkResponseException):
    '''(код 148) Access to the menu of the user denied'''

class VkErrorParamTimestamp(VkResponseException):  # общая ошибка
    '''(код 150) Invalid timestamp'''

class VkErrorFriendsListId(VkResponseException):
    '''(код 171) Invalid list id'''

class VkErrorFriendsListLimit(VkResponseException):
    '''(код 173) Reached the maximum number of lists'''

class VkErrorFriendsAddYourself(VkResponseException):
    '''(код 174) Cannot add user himself as friend'''

class VkErrorFriendsAddInEnemy(VkResponseException):
    '''(код 175) Cannot add this user to friends as they have put you on their blacklist'''

class VkErrorFriendsAddEnemy(VkResponseException):
    '''(код 176) Cannot add this user to friends as you put him on blacklist'''

class VkErrorFriendsAddNotFound(VkResponseException):
    '''(код 177) Cannot add this user to friends as user not found'''

class VkErrorParamNoteId(VkResponseException):
    '''(код 180) Note not found'''

class VkErrorAccessNote(VkResponseException):
    '''(код 181) Access to note denied'''

class VkErrorAccessNoteComment(VkResponseException):
    '''(код 182) You can't comment this note'''

class VkErrorAccessComment(VkResponseException):
    '''(код 183) Access to comment denied'''

class VkErrorAccessAlbum(VkResponseException):  # общая ошибка
    '''(код 200) Access denied'''

class VkErrorAccessAudio(VkResponseException):  # общая ошибка
    '''(код 201) Access denied'''

class VkErrorAccessGroup(VkResponseException):  # общая ошибка
    '''(код 203) Access to group denied'''

class VkErrorAccessVideo(VkResponseException):
    '''(код 204) Access denied'''

class VkErrorAccessMarket(VkResponseException):
    '''(код 205) Access denied'''

class VkErrorWallAccessPost(VkResponseException):
    '''(код 210) Access to wall's post denied'''

class VkErrorWallAccessComment(VkResponseException):
    '''(код 211) Access to wall's comment denied'''

class VkErrorWallAccessReplies(VkResponseException):
    '''(код 212) Access to post comments denied'''

class VkErrorWallAccessAddReply(VkResponseException):
    '''(код 213) Access to status replies denied'''

class VkErrorWallAddPost(VkResponseException):
    '''(код 214) Access to adding post denied'''

class VkErrorWallAdsPublished(VkResponseException):
    '''(код 219) Advertisement post was recently added'''

class VkErrorWallTooManyRecipients(VkResponseException):
    '''(код 220) Too many recipients'''

class VkErrorStatusNoAudio(VkResponseException):
    '''(код 221) User disabled track name broadcast'''

class VkErrorWallLinksForbidden(VkResponseException):
    '''(код 222) Hyperlinks are forbidden'''

class VkErrorWallReplyOwnerFlood(VkResponseException):
    '''(код 223) Too many replies'''

class VkErrorWallAdsPostLimitReached(VkResponseException):
    '''(код 224) Too many ads posts'''

class VkErrorPollsAccess(VkResponseException):
    '''(код 250) Access to poll denied'''

class VkErrorPollsPollId(VkResponseException):
    '''(код 251) Invalid poll id'''

class VkErrorPollsAnswerId(VkResponseException):
    '''(код 252) Invalid answer id'''

class VkErrorPollsAccessWithoutVote(VkResponseException):
    '''(код 253) Access denied, please vote first'''

class VkErrorAccessGroups(VkResponseException):
    '''(код 260) Access to the groups list is denied due to the user's privacy settings'''

class VkErrorAlbumFull(VkResponseException):  # общая ошибка
    '''(код 300) This album is full'''

class VkErrorAlbumsLimit(VkResponseException):
    '''(код 302) Albums number limit is reached'''

class VkErrorVotesPermission(VkResponseException):  # общая ошибка
    '''(код 500) Permission denied. You must enable votes processing in application settings'''

class VkErrorVotes(VkResponseException):
    '''(код 503) Not enough votes'''

class VkErrorAdsPermission(VkResponseException):  # общая ошибка
    '''(код 600) Permission denied. You have no access to operations specified with given object(s)'''

class VkErrorWeightedFlood(VkResponseException):
    '''(код 601) Permission denied. You have requested too many actions this day. Try later.'''

class VkErrorAdsPartialSuccess(VkResponseException):
    '''(код 602) Some part of the request has not been completed'''

class VkErrorAdsSpecific(VkResponseException):  # общая ошибка
    '''(код 603) Some ads error occured'''

class VkErrorAdsObjectDeleted(VkResponseException):
    '''(код 629) Object deleted'''

class VkErrorGroupChangeCreator(VkResponseException):
    '''(код 700) Cannot edit creator role'''

class VkErrorGroupNotInClub(VkResponseException):
    '''(код 701) User should be in club'''

class VkErrorGroupTooManyOfficers(VkResponseException):
    '''(код 702) Too many officers in club'''

class VkErrorGroupNeed2fa(VkResponseException):
    '''(код 703) You need to enable 2FA for this action'''

class VkErrorGroupHostNeed2fa(VkResponseException):
    '''(код 704) User needs to enable 2FA for this action'''

class VkErrorGroupTooManyAddresses(VkResponseException):
    '''(код 706) Too many addresses in club'''

class VkErrorGroupAppIsNotInstalledInCommunity(VkResponseException):
    '''(код 711) Application is not installed in community'''

class VkErrorGroupInviteLinksNotValid(VkResponseException):
    '''(код 714) Invite link is invalid - expired, deleted or not exists'''

class VkErrorVideoAlreadyAdded(VkResponseException):
    '''(код 800) This video is already added'''

class VkErrorVideoCommentsClosed(VkResponseException):
    '''(код 801) Comments for this video are closed'''

class VkErrorMessagesUserBlocked(VkResponseException):
    '''(код 900) Can't send messages for users from blacklist'''

class VkErrorMessagesDenySend(VkResponseException):
    '''(код 901) Can't send messages for users without permission'''

class VkErrorMessagesPrivacy(VkResponseException):
    '''(код 902) Can't send messages to this user due to their privacy settings'''

class VkErrorMessagesTooOldPts(VkResponseException):
    '''(код 907) Value of ts or pts is too old'''

class VkErrorMessagesTooNewPts(VkResponseException):
    '''(код 908) Value of ts or pts is too new'''

class VkErrorMessagesEditExpired(VkResponseException):
    '''(код 909) Can't edit this message, because it's too old'''

class VkErrorMessagesTooBig(VkResponseException):
    '''(код 910) Can't sent this message, because it's too big'''

class VkErrorMessagesKeyboardInvalid(VkResponseException):
    '''(код 911) Keyboard format is invalid'''

class VkErrorMessagesChatBotFeature(VkResponseException):
    '''(код 912) This is a chat bot feature, change this status in settings'''

class VkErrorMessagesTooLongForwards(VkResponseException):
    '''(код 913) Too many forwarded messages'''

class VkErrorMessagesTooLongMessage(VkResponseException):
    '''(код 914) Message is too long'''

class VkErrorMessagesChatUserNoAccess(VkResponseException):
    '''(код 917) You don't have access to this chat'''

class VkErrorMessagesCantSeeInviteLink(VkResponseException):
    '''(код 919) You can't see invite link for this chat'''

class VkErrorMessagesEditKindDisallowed(VkResponseException):
    '''(код 920) Can't edit this kind of message'''

class VkErrorMessagesCantFwd(VkResponseException):
    '''(код 921) Can't forward these messages'''

class VkErrorMessagesCantDeleteForAll(VkResponseException):
    '''(код 924) Can't delete this message for everybody'''

class VkErrorMessagesChatNotAdmin(VkResponseException):
    '''(код 925) You are not admin of this chat'''

class VkErrorMessagesChatNotExist(VkResponseException):
    '''(код 927) Chat does not exist'''

class VkErrorMessagesCantChangeInviteLink(VkResponseException):
    '''(код 931) You can't change invite link for this chat'''

class VkErrorMessagesGroupPeerAccess(VkResponseException):
    '''(код 932) Your community can't interact with this peer'''

class VkErrorMessagesChatUserNotInChat(VkResponseException):
    '''(код 935) User not found in chat'''

class VkErrorMessagesContactNotFound(VkResponseException):
    '''(код 936) Contact not found'''

class VkErrorMessagesMessageRequestAlreadySent(VkResponseException):
    '''(код 939) Message request already sent'''

class VkErrorMessagesTooManyPosts(VkResponseException):
    '''(код 940) Too many posts in messages'''

class VkErrorMessagesCantPinOneTimeStory(VkResponseException):
    '''(код 942) Cannot pin one-time story'''

class VkErrorMessagesIntentCantUse(VkResponseException):
    '''(код 943) Cannot use this intent'''

class VkErrorMessagesIntentLimitOverflow(VkResponseException):
    '''(код 944) Limits overflow for this intent'''

class VkErrorMessagesChatDisabled(VkResponseException):
    '''(код 945) Chat was disabled'''

class VkErrorMessagesChatUnsupported(VkResponseException):
    '''(код 946) Chat not supported'''

class VkErrorMessagesMemberAccessToGroupDenied(VkResponseException):
    '''(код 947) Can't add user to chat, because user has no access to group'''

class VkErrorMessagesCantEditPinnedYet(VkResponseException):
    '''(код 949) Can't edit pinned message yet'''

class VkErrorMessagesPeerBlockedReasonByTime(VkResponseException):
    '''(код 950) Can't send message, reply timed out'''

class VkErrorParamPhone(VkResponseException):
    '''(код 1000) Invalid phone number'''

class VkErrorPhoneAlreadyUsed(VkResponseException):
    '''(код 1004) This phone number is used by another user'''

class VkErrorAuthFloodError(VkResponseException):
    '''(код 1105) Too many auth attempts, try again later'''

class VkErrorAuthDelay(VkResponseException):
    '''(код 1112) Processing.. Try later'''

class VkErrorParamDocId(VkResponseException):
    '''(код 1150) Invalid document id'''

class VkErrorParamDocDeleteAccess(VkResponseException):
    '''(код 1151) Access to document deleting is denied'''

class VkErrorParamDocTitle(VkResponseException):
    '''(код 1152) Invalid document title'''

class VkErrorParamDocAccess(VkResponseException):
    '''(код 1153) Access to document is denied'''

class VkErrorPhotoChanged(VkResponseException):
    '''(код 1160) Original photo was changed'''

class VkErrorTooManyLists(VkResponseException):
    '''(код 1170) Too many feed lists'''

class VkErrorAppsAlreadyUnlocked(VkResponseException):
    '''(код 1251) This achievement is already unlocked'''

class VkErrorAppsSubscriptionNotFound(VkResponseException):
    '''(код 1256) Subscription not found'''

class VkErrorAppsSubscriptionInvalidStatus(VkResponseException):
    '''(код 1257) Subscription is in invalid status'''

class VkErrorInvalidAddress(VkResponseException):
    '''(код 1260) Invalid screen name'''

class VkErrorCommunitiesCatalogDisabled(VkResponseException):
    '''(код 1310) Catalog is not available for this user'''

class VkErrorCommunitiesCategoriesDisabled(VkResponseException):
    '''(код 1311) Catalog categories are not available for this user'''

class VkErrorMarketRestoreTooLate(VkResponseException):
    '''(код 1400) Too late for restore'''

class VkErrorMarketCommentsClosed(VkResponseException):
    '''(код 1401) Comments for this market are closed'''

class VkErrorMarketAlbumNotFound(VkResponseException):
    '''(код 1402) Album not found'''

class VkErrorMarketItemNotFound(VkResponseException):
    '''(код 1403) Item not found'''

class VkErrorMarketItemAlreadyAdded(VkResponseException):
    '''(код 1404) Item already added to album'''

class VkErrorMarketTooManyItems(VkResponseException):
    '''(код 1405) Too many items'''

class VkErrorMarketTooManyItemsInAlbum(VkResponseException):
    '''(код 1406) Too many items in album'''

class VkErrorMarketTooManyAlbums(VkResponseException):
    '''(код 1407) Too many albums'''

class VkErrorMarketItemHasBadLinks(VkResponseException):
    '''(код 1408) Item has bad links in description'''

class VkErrorMarketShopNotEnabled(VkResponseException):
    '''(код 1409) Shop not enabled'''

class VkErrorMarketVariantNotFound(VkResponseException):
    '''(код 1416) Variant not found'''

class VkErrorMarketPropertyNotFound(VkResponseException):
    '''(код 1417) Property not found'''

class VkErrorMarketGroupingMustContainMoreThanOneItem(VkResponseException):
    '''(код 1425) Grouping must have two or more items'''

class VkErrorMarketGroupingItemsMustHaveDistinctProperties(VkResponseException):
    '''(код 1426) Item must have distinct properties'''

class VkErrorMarketOrdersNoCartItems(VkResponseException):
    '''(код 1427) Cart is empty'''

class VkErrorMarketInvalidDimensions(VkResponseException):
    '''(код 1429) Specify width, length, height and weight all together'''

class VkErrorMarketCantChangeVkpayStatus(VkResponseException):
    '''(код 1430) VK Pay status can not be changed'''

class VkErrorMarketShopAlreadyEnabled(VkResponseException):
    '''(код 1431) Market was already enabled in this group'''

class VkErrorMarketShopAlreadyDisabled(VkResponseException):
    '''(код 1432) Market was already disabled in this group'''

class VkErrorMarketPhotosCropInvalidFormat(VkResponseException):
    '''(код 1433) Invalid image crop format'''

class VkErrorMarketPhotosCropOverflow(VkResponseException):
    '''(код 1434) Crop bottom right corner is outside of the image'''

class VkErrorMarketPhotosCropSizeTooLow(VkResponseException):
    '''(код 1435) Crop size is less than the minimum'''

class VkErrorStoryExpired(VkResponseException):
    '''(код 1600) Story has already expired'''

class VkErrorStoryIncorrectReplyPrivacy(VkResponseException):
    '''(код 1602) Incorrect reply privacy'''

class VkErrorPrettyCardsCardNotFound(VkResponseException):
    '''(код 1900) Card not found'''

class VkErrorPrettyCardsTooManyCards(VkResponseException):
    '''(код 1901) Too many cards'''

class VkErrorPrettyCardsCardIsConnectedToPost(VkResponseException):
    '''(код 1902) Card is connected to post'''

class VkErrorCallbackApiServersLimit(VkResponseException):
    '''(код 2000) Servers number limit is reached'''

class VkErrorWallCheckLinkCantDetermineSource(VkResponseException):
    '''(код 3102) Specified link is incorrect (can't find source)'''

class VkErrorRecaptcha(VkResponseException):  # общая ошибка
    '''(код 3300) Recaptcha needed'''

class VkErrorPhoneValidationNeed(VkResponseException):  # общая ошибка
    '''(код 3301) Phone validation needed'''

class VkErrorPasswordValidationNeed(VkResponseException):  # общая ошибка
    '''(код 3302) Password validation needed'''

class VkErrorOtpValidationNeed(VkResponseException):  # общая ошибка
    '''(код 3303) Otp app validation needed'''

class VkErrorEmailConfirmationNeed(VkResponseException):  # общая ошибка
    '''(код 3304) Email confirmation needed'''

class VkErrorAssertVotes(VkResponseException):  # общая ошибка
    '''(код 3305) Assert votes'''

class VkErrorTokenExtensionRequired(VkResponseException):  # общая ошибка
    '''(код 3609) Token extension required'''

class VkErrorUserDeactivated(VkResponseException):  # общая ошибка
    '''(код 3610) User is deactivated'''

class VkErrorUserServiceDeactivated(VkResponseException):  # общая ошибка
    '''(код 3611) Service is deactivated for user'''

class VkErrorFaveAliexpressTag(VkResponseException):
    '''(код 3800) Can't set AliExpress tag to this type of object'''


_error_map = {
    1: VkErrorUnknown,
    2: VkErrorDisabled,
    3: VkErrorMethod,
    4: VkErrorSignature,
    5: VkErrorAuth,
    6: VkErrorTooMany,
    7: VkErrorPermission,
    8: VkErrorRequest,
    9: VkErrorFlood,
    10: VkErrorServer,
    11: VkErrorEnabledInTest,
    12: VkErrorCompile,
    13: VkErrorRuntime,
    14: VkErrorCaptcha,
    15: VkErrorAccess,
    16: VkErrorAuthHttps,
    17: VkErrorAuthValidation,
    18: VkErrorUserDeleted,
    19: VkErrorBlocked,
    20: VkErrorMethodPermission,
    21: VkErrorMethodAds,
    22: VkErrorUpload,
    23: VkErrorMethodDisabled,
    24: VkErrorNeedConfirmation,
    25: VkErrorNeedTokenConfirmation,
    27: VkErrorGroupAuth,
    28: VkErrorAppAuth,
    29: VkErrorRateLimit,
    30: VkErrorPrivateProfile,
    33: VkErrorNotImplementedYet,
    35: VkErrorClientUpdateNeeded,
    100: VkErrorParam,
    101: VkErrorParamApiId,
    103: VkErrorLimits,
    104: VkErrorNotFound,
    105: VkErrorSaveFile,
    106: VkErrorActionFailed,
    113: VkErrorParamUserId,
    114: VkErrorParamAlbumId,
    118: VkErrorParamServer,
    119: VkErrorParamTitle,
    121: VkErrorParamHash,
    122: VkErrorParamPhotos,
    125: VkErrorParamGroupId,
    129: VkErrorParamPhoto,
    140: VkErrorParamPageId,
    141: VkErrorAccessPage,
    146: VkErrorMobileNotActivated,
    147: VkErrorInsufficientFunds,
    148: VkErrorAccessMenu,
    150: VkErrorParamTimestamp,
    171: VkErrorFriendsListId,
    173: VkErrorFriendsListLimit,
    174: VkErrorFriendsAddYourself,
    175: VkErrorFriendsAddInEnemy,
    176: VkErrorFriendsAddEnemy,
    177: VkErrorFriendsAddNotFound,
    180: VkErrorParamNoteId,
    181: VkErrorAccessNote,
    182: VkErrorAccessNoteComment,
    183: VkErrorAccessComment,
    200: VkErrorAccessAlbum,
    201: VkErrorAccessAudio,
    203: VkErrorAccessGroup,
    204: VkErrorAccessVideo,
    205: VkErrorAccessMarket,
    210: VkErrorWallAccessPost,
    211: VkErrorWallAccessComment,
    212: VkErrorWallAccessReplies,
    213: VkErrorWallAccessAddReply,
    214: VkErrorWallAddPost,
    219: VkErrorWallAdsPublished,
    220: VkErrorWallTooManyRecipients,
    221: VkErrorStatusNoAudio,
    222: VkErrorWallLinksForbidden,
    223: VkErrorWallReplyOwnerFlood,
    224: VkErrorWallAdsPostLimitReached,
    250: VkErrorPollsAccess,
    251: VkErrorPollsPollId,
    252: VkErrorPollsAnswerId,
    253: VkErrorPollsAccessWithoutVote,
    260: VkErrorAccessGroups,
    300: VkErrorAlbumFull,
    302: VkErrorAlbumsLimit,
    500: VkErrorVotesPermission,
    503: VkErrorVotes,
    600: VkErrorAdsPermission,
    601: VkErrorWeightedFlood,
    602: VkErrorAdsPartialSuccess,
    603: VkErrorAdsSpecific,
    629: VkErrorAdsObjectDeleted,
    700: VkErrorGroupChangeCreator,
    701: VkErrorGroupNotInClub,
    702: VkErrorGroupTooManyOfficers,
    703: VkErrorGroupNeed2fa,
    704: VkErrorGroupHostNeed2fa,
    706: VkErrorGroupTooManyAddresses,
    711: VkErrorGroupAppIsNotInstalledInCommunity,
    714: VkErrorGroupInviteLinksNotValid,
    800: VkErrorVideoAlreadyAdded,
    801: VkErrorVideoCommentsClosed,
    900: VkErrorMessagesUserBlocked,
    901: VkErrorMessagesDenySend,
    902: VkErrorMessagesPrivacy,
    907: VkErrorMessagesTooOldPts,
    908: VkErrorMessagesTooNewPts,
    909: VkErrorMessagesEditExpired,
    910: VkErrorMessagesTooBig,
    911: VkErrorMessagesKeyboardInvalid,
    912: VkErrorMessagesChatBotFeature,
    913: VkErrorMessagesTooLongForwards,
    914: VkErrorMessagesTooLongMessage,
    917: VkErrorMessagesChatUserNoAccess,
    919: VkErrorMessagesCantSeeInviteLink,
    920: VkErrorMessagesEditKindDisallowed,
    921: VkErrorMessagesCantFwd,
    924: VkErrorMessagesCantDeleteForAll,
    925: VkErrorMessagesChatNotAdmin,
    927: VkErrorMessagesChatNotExist,
    931: VkErrorMessagesCantChangeInviteLink,
    932: VkErrorMessagesGroupPeerAccess,
    935: VkErrorMessagesChatUserNotInChat,
    936: VkErrorMessagesContactNotFound,
    939: VkErrorMessagesMessageRequestAlreadySent,
    940: VkErrorMessagesTooManyPosts,
    942: VkErrorMessagesCantPinOneTimeStory,
    943: VkErrorMessagesIntentCantUse,
    944: VkErrorMessagesIntentLimitOverflow,
    945: VkErrorMessagesChatDisabled,
    946: VkErrorMessagesChatUnsupported,
    947: VkErrorMessagesMemberAccessToGroupDenied,
    949: VkErrorMessagesCantEditPinnedYet,
    950: VkErrorMessagesPeerBlockedReasonByTime,
    1000: VkErrorParamPhone,
    1004: VkErrorPhoneAlreadyUsed,
    1105: VkErrorAuthFloodError,
    1112: VkErrorAuthDelay,
    1150: VkErrorParamDocId,
    1151: VkErrorParamDocDeleteAccess,
    1152: VkErrorParamDocTitle,
    1153: VkErrorParamDocAccess,
    1160: VkErrorPhotoChanged,
    1170: VkErrorTooManyLists,
    1251: VkErrorAppsAlreadyUnlocked,
    1256: VkErrorAppsSubscriptionNotFound,
    1257: VkErrorAppsSubscriptionInvalidStatus,
    1260: VkErrorInvalidAddress,
    1310: VkErrorCommunitiesCatalogDisabled,
    1311: VkErrorCommunitiesCategoriesDisabled,
    1400: VkErrorMarketRestoreTooLate,
    1401: VkErrorMarketCommentsClosed,
    1402: VkErrorMarketAlbumNotFound,
    1403: VkErrorMarketItemNotFound,
    1404: VkErrorMarketItemAlreadyAdded,
    1405: VkErrorMarketTooManyItems,
    1406: VkErrorMarketTooManyItemsInAlbum,
    1407: VkErrorMarketTooManyAlbums,
    1408: VkErrorMarketItemHasBadLinks,
    1409: VkErrorMarketShopNotEnabled,
    1416: VkErrorMarketVariantNotFound,
    1417: VkErrorMarketPropertyNotFound,
    1425: VkErrorMarketGroupingMustContainMoreThanOneItem,
    1426: VkErrorMarketGroupingItemsMustHaveDistinctProperties,
    1427: VkErrorMarketOrdersNoCartItems,
    1429: VkErrorMarketInvalidDimensions,
    1430: VkErrorMarketCantChangeVkpayStatus,
    1431: VkErrorMarketShopAlreadyEnabled,
    1432: VkErrorMarketShopAlreadyDisabled,
    1433: VkErrorMarketPhotosCropInvalidFormat,
    1434: VkErrorMarketPhotosCropOverflow,
    1435: VkErrorMarketPhotosCropSizeTooLow,
    1600: VkErrorStoryExpired,
    1602: VkErrorStoryIncorrectReplyPrivacy,
    1900: VkErrorPrettyCardsCardNotFound,
    1901: VkErrorPrettyCardsTooManyCards,
    1902: VkErrorPrettyCardsCardIsConnectedToPost,
    2000: VkErrorCallbackApiServersLimit,
    3102: VkErrorWallCheckLinkCantDetermineSource,
    3300: VkErrorRecaptcha,
    3301: VkErrorPhoneValidationNeed,
    3302: VkErrorPasswordValidationNeed,
    3303: VkErrorOtpValidationNeed,
    3304: VkErrorEmailConfirmationNeed,
    3305: VkErrorAssertVotes,
    3609: VkErrorTokenExtensionRequired,
    3610: VkErrorUserDeactivated,
    3611: VkErrorUserServiceDeactivated,
    3800: VkErrorFaveAliexpressTag,
}

# для совместимости со старыми версиями
RateLimit = VkErrorRateLimit
FloodControl = VkErrorFlood
CaptchaNeeded = VkErrorCaptcha
TooManyRequests = VkErrorTooMany
