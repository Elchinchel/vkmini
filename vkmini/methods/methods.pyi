# TODO: Do.


from typing import Literal, Union, List


class Flag(bool, int):
    pass


class messages:
    def send(
        peer_id: int,
        message: str,
        attachment: str,
        reply_to: int,
        forward_messages: List[int],
        sticker_id: int,
        group_id: int,
        keyboard: str,
        template: str,
        payload: str,
        disable_mentions: Union[bool, Literal[0, 1]],
        dont_parse_links: Union[bool, Literal[0, 1]],
        random_id: int
    ) -> Union[int, dict]: ...


# class Messages():
#     addChatUser = 'messages.addChatUser'
#     allowMessagesFromGroup = 'messages.allowMessagesFromGroup'
#     createChat = 'messages.createChat'
#     delete = 'messages.delete'
#     deleteChatPhoto = 'messages.deleteChatPhoto'
#     deleteConversation = 'messages.deleteConversation'
#     denyMessagesFromGroup = 'messages.denyMessagesFromGroup'
#     edit = 'messages.edit'
#     editChat = 'messages.editChat'
#     getByConversationMessageId = 'messages.getByConversationMessageId'
#     getById = 'messages.getById'
#     getChat = 'messages.getChat'
#     getChatPreview = 'messages.getChatPreview'
#     getConversationMembers = 'messages.getConversationMembers'
#     getConversations = 'messages.getConversations'
#     getConversationsById = 'messages.getConversationsById'
#     getHistory = 'messages.getHistory'
#     getHistoryAttachments = 'messages.getHistoryAttachments'
#     getImportantMessages = 'messages.getImportantMessages'
#     getInviteLink = 'messages.getInviteLink'
#     getLastActivity = 'messages.getLastActivity'
#     getLongPollHistory = 'messages.getLongPollHistory'
#     getLongPollServer = 'messages.getLongPollServer'
#     isMessagesFromGroupAllowed = 'messages.isMessagesFromGroupAllowed'
#     joinChatByInviteLink = 'messages.joinChatByInviteLink'
#     markAsAnsweredConversation = 'messages.markAsAnsweredConversation'
#     markAsImportant = 'messages.markAsImportant'
#     markAsImportantConversation = 'messages.markAsImportantConversation'
#     markAsRead = 'messages.markAsRead'
#     pin = 'messages.pin'
#     removeChatUser = 'messages.removeChatUser'
#     restore = 'messages.restore'
#     search = 'messages.search'
#     searchConversations = 'messages.searchConversations'
#     send = 'messages.send'
#     setActivity = 'messages.setActivity'
#     setChatPhoto = 'messages.setChatPhoto'
#     unpin = 'messages.unpin'
