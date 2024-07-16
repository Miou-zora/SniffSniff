from scapy.all import sniff, Raw, IP, ICMP # pylint: disable=no-name-in-module
from colorama import Fore, Back, Style
from CustomDataWrapper import Data, Buffer
from ProtocolBuilder import ProtocolBuilder
from Misc import * # pylint: disable=unused-wildcard-import
import struct


all_message = {
1468: "PaginationAnswerAbstractMessage",
7777: "NetworkDataContainerMessage",
1939: "ProtocolRequired",
3098: "LoginQueueStatusMessage",
4838: "QueueStatusMessage",
7923: "ConsoleMessage",
9802: "ConsoleEndMessage",
869: "ConsoleCommandsListMessage",
5586: "HelloConnectMessage",
7628: "CredentialsAcknowledgementMessage",
8872: "NicknameRegistrationMessage",
590: "AccountLinkRequiredMessage",
4482: "NicknameRefusedMessage",
8083: "NicknameAcceptedMessage",
6104: "IdentificationSuccessMessage",
5352: "ForceAccountErrorMessage",
25: "ForceAccountStatusMessage",
3224: "IdentificationSuccessWithLoginTokenMessage",
4567: "IdentificationFailedMessage",
8668: "IdentificationFailedBannedMessage",
4124: "IdentificationFailedForBadVersionMessage",
9500: "ServersListMessage",
4424: "ServerStatusUpdateMessage",
4944: "SelectedServerDataMessage",
7269: "SelectedServerDataExtendedMessage",
277: "SelectedServerRefusedMessage",
2291: "AcquaintanceSearchErrorMessage",
8632: "AcquaintanceServerListMessage",
2491: "MigratedServerListMessage",
708: "HelloGameMessage",
7505: "AuthenticationTicketAcceptedMessage",
5922: "AuthenticationTicketRefusedMessage",
3137: "AlreadyConnectedMessage",
2295: "AccountLoggingKickedMessage",
2673: "ReloginTokenStatusMessage",
154: "ServerSettingsMessage",
9337: "ServerSessionConstantsMessage",
8385: "ServerOptionalFeaturesMessage",
8908: "AccountCapabilitiesMessage",
3339: "TrustStatusMessage",
4545: "AccountInformationsUpdateMessage",
5336: "AccountSubscriptionElapsedDurationMessage",
5970: "CheckFileRequestMessage",
2579: "RawDataMessage",
6041: "GameActionItemListMessage",
8509: "GameActionItemAddMessage",
5525: "GameActionItemConsumedMessage",
7317: "CharacterCanBeCreatedResultMessage",
5979: "CharacterCreationResultMessage",
5348: "CharacterDeletionPrepareMessage",
4351: "CharacterDeletionErrorMessage",
2208: "CharacterNameSuggestionSuccessMessage",
5371: "CharacterNameSuggestionFailureMessage",
8016: "CharactersListMessage",
9633: "CharactersListWithRemodelingMessage",
7643: "CharactersListErrorMessage",
4299: "CharacterSelectedSuccessMessage",
4050: "CharacterSelectedForceMessage",
1596: "CharacterSelectedErrorMessage",
1024: "PopupWarningMessage",
2757: "PopupWarningClosedMessage",
7499: "BasicDateMessage",
4945: "BasicTimeMessage",
3938: "AlmanachCalendarDateMessage",
2887: "BasicNoOperationMessage",
9375: "BasicAckMessage",
5943: "SystemMessageDisplayMessage",
3766: "TextInformationMessage",
999: "OnConnectionEventMessage",
1324: "SetCharacterRestrictionsMessage",
9259: "ServerExperienceModificatorMessage",
3451: "CharacterCapabilitiesMessage",
605: "CharacterLoadingCompleteMessage",
1595: "GameContextCreateMessage",
223: "GameContextCreateErrorMessage",
1821: "GameContextDestroyMessage",
3496: "GameContextRemoveElementMessage",
5405: "GameContextRemoveMultipleElementsMessage",
7775: "GameContextRemoveElementWithEventMessage",
1167: "GameContextRemoveMultipleElementsWithEventsMessage",
5362: "GameContextMoveElementMessage",
7368: "GameContextMoveMultipleElementsMessage",
7865: "GameContextRefreshEntityLookMessage",
6322: "GameMapNoMovementMessage",
6493: "GameMapMovementMessage",
779: "GameCautiousMapMovementMessage",
8741: "GameMapChangeOrientationMessage",
3256: "GameMapChangeOrientationsMessage",
4: "GameEntityDispositionMessage",
7948: "GameEntitiesDispositionMessage",
2619: "GameEntityDispositionErrorMessage",
3997: "GameRefreshMonsterBoostsMessage",
3860: "PlayerStatusUpdateErrorMessage",
3675: "PlayerStatusUpdateMessage",
8673: "BasicWhoIsMessage",
4629: "BasicWhoIsNoMatchMessage",
2693: "NumericWhoIsMessage",
4877: "BasicPongMessage",
6273: "BasicLatencyStatsRequestMessage",
594: "SequenceNumberRequestMessage",
9599: "CurrentServerStatusUpdateMessage",
991: "CinematicMessage",
2370: "DumpedEntityStatsMessage",
9357: "DebugHighlightCellsMessage",
3737: "DebugClearHighlightCellsMessage",
6256: "DebugInClientMessage",
3498: "ClientYouAreDrunkMessage",
4632: "DisplayNumericalValuePaddockMessage",
7991: "CurrentMapMessage",
5476: "CurrentMapInstanceMessage",
6669: "TeleportOnSameMapMessage",
2838: "MapFightCountMessage",
8225: "MapRunningFightListMessage",
2005: "MapRunningFightDetailsMessage",
8895: "MapRunningFightDetailsExtendedMessage",
75: "MapObstacleUpdateMessage",
9792: "MapComplementaryInformationsDataMessage",
1071: "MapComplementaryInformationsDataInHouseMessage",
5198: "MapComplementaryInformationsWithCoordsMessage",
1678: "SubareaRewardRateMessage",
9138: "BreachEnterMessage",
1178: "BreachTeleportResponseMessage",
8241: "BreachRoomLockedMessage",
7028: "BreachRoomUnlockResultMessage",
6746: "BreachExitResponseMessage",
4428: "MapComplementaryInformationsBreachMessage",
9314: "BreachGameFightEndMessage",
9316: "AnomalyStateMessage",
1124: "AnomalyOpenedMessage",
7688: "MapComplementaryInformationsAnomalyMessage",
9437: "MapFightStartPositionsUpdateMessage",
1818: "GameRolePlayShowActorMessage",
323: "GameRolePlayShowMultipleActorsMessage",
5: "GameRolePlayShowActorWithEventMessage",
4395: "CharacterStatsListMessage",
4354: "FighterStatsListMessage",
1373: "ApplySpellModifierMessage",
194: "RemoveSpellModifierMessage",
5797: "CharacterLevelUpMessage",
9701: "CharacterExperienceGainMessage",
3031: "CharacterLevelUpInformationMessage",
1395: "UpdateLifePointsMessage",
9965: "LifePointsRegenBeginMessage",
6833: "LifePointsRegenEndMessage",
8693: "GameRolePlayPlayerLifeStatusMessage",
3824: "GameRolePlayGameOverMessage",
5826: "GameRolePlayFightRequestCanceledMessage",
6235: "GameRolePlayAggressionMessage",
4626: "GameRolePlayPlayerFightFriendlyRequestedMessage",
1668: "GameRolePlayPlayerFightFriendlyAnsweredMessage",
4586: "GameRolePlayArenaRegistrationStatusMessage",
5667: "GameRolePlayArenaFightPropositionMessage",
2033: "ArenaFightAnswerAcknowledgementMessage",
3114: "GameRolePlayArenaFighterStatusMessage",
1665: "GameRolePlayArenaUpdatePlayerInfosMessage",
4751: "GameRolePlayArenaSwitchToFightServerMessage",
6763: "GameRolePlayArenaSwitchToGameServerMessage",
953: "GameRolePlayArenaInvitationCandidatesAnswerMessage",
7599: "GameRolePlayArenaLeagueRewardsMessage",
1302: "GameRolePlayArenaPlayerBehavioursMessage",
8542: "GameRolePlayArenaRegistrationWarningMessage",
9879: "GameRolePlayMonsterAngryAtPlayerMessage",
5585: "GameRolePlayMonsterNotAngryAtPlayerMessage",
7254: "GameRolePlayShowChallengeMessage",
3370: "GameRolePlayRemoveChallengeMessage",
1173: "GameRolePlaySpellAnimMessage",
4358: "GameRolePlayDelayedActionMessage",
3110: "GameRolePlayDelayedObjectUseMessage",
7896: "GameRolePlayDelayedActionFinishedMessage",
9194: "ShowCellMessage",
4927: "ShowCellSpectatorMessage",
6131: "GameFightStartingMessage",
8166: "GameFightJoinMessage",
3924: "GameFightSpectatorJoinMessage",
282: "GameFightPlacementPossiblePositionsMessage",
6325: "GameFightPlacementSwapPositionsErrorMessage",
5124: "GameFightPlacementSwapPositionsOfferMessage",
1579: "GameFightPlacementSwapPositionsCancelledMessage",
5606: "GameFightPlacementSwapPositionsMessage",
3172: "GameFightOptionStateUpdateMessage",
3874: "GameFightUpdateTeamMessage",
7301: "GameFightRemoveTeamMemberMessage",
109: "GameFightHumanReadyStateMessage",
6974: "GameFightLeaveMessage",
9783: "GameFightStartMessage",
6318: "GameFightSpectateMessage",
2675: "GameFightResumeMessage",
5652: "GameFightResumeWithSlavesMessage",
2386: "GameFightEndMessage",
8261: "GameFightNewRoundMessage",
1243: "GameFightTurnListMessage",
217: "GameFightTurnStartMessage",
4448: "GameFightNewWaveMessage",
3867: "GameFightTurnStartPlayingMessage",
7389: "GameFightTurnResumeMessage",
1045: "GameFightPauseMessage",
974: "SlaveSwitchContextMessage",
1268: "SlaveNoLongerControledMessage",
2710: "RefreshCharacterStatsMessage",
379: "GameFightTurnReadyRequestMessage",
8985: "GameFightSynchronizeMessage",
7900: "GameFightTurnEndMessage",
5747: "GameFightShowFighterMessage",
3786: "GameFightRefreshFighterMessage",
7583: "GameFightShowFighterRandomStaticPoseMessage",
3724: "ArenaFighterLeaveMessage",
1701: "ArenaFighterIdleMessage",
7231: "SequenceStartMessage",
1586: "SequenceEndMessage",
9631: "AbstractGameActionMessage",
116: "GameActionNoopMessage",
9805: "GameActionSpamMessage",
1587: "AbstractGameActionWithAckMessage",
393: "GameActionFightNoSpellCastMessage",
5172: "AbstractGameActionFightTargetedAbilityMessage",
2679: "GameActionFightSpellCastMessage",
2405: "GameActionFightCloseCombatMessage",
6014: "GameActionUpdateEffectTriggerCountMessage",
7285: "GameActionFightInvisibleDetectedMessage",
8927: "GameActionFightPointsVariationMessage",
3805: "GameActionFightTackledMessage",
9724: "GameActionFightDeathMessage",
6293: "GameActionFightKillMessage",
5071: "GameActionFightVanishMessage",
766: "GameActionFightSpellCooldownVariationMessage",
276: "GameActionFightSpellImmunityMessage",
6590: "GameActionFightLifePointsGainMessage",
6444: "GameActionFightLifePointsLostMessage",
5703: "GameActionFightLifeAndShieldPointsLostMessage",
3071: "GameActionFightDispellableEffectMessage",
2356: "GameActionFightReflectSpellMessage",
1547: "GameActionFightReduceDamagesMessage",
7259: "GameActionFightReflectDamagesMessage",
7515: "GameActionFightDodgePointLossMessage",
7006: "GameActionFightSlideMessage",
9922: "GameActionFightTeleportOnSameMapMessage",
8976: "GameActionFightExchangePositionsMessage",
9152: "GameActionFightDispellMessage",
8550: "GameActionFightDispellEffectMessage",
4714: "GameActionFightDispellSpellMessage",
9731: "GameActionFightModifyEffectsDurationMessage",
8838: "GameActionFightTriggerEffectMessage",
6352: "GameActionFightStealKamaMessage",
1629: "GameActionFightChangeLookMessage",
2495: "GameActionFightInvisibilityMessage",
7363: "GameActionFightSummonMessage",
8549: "GameActionFightMultipleSummonMessage",
432: "GameActionFightMarkCellsMessage",
9827: "GameActionFightUnmarkCellsMessage",
6199: "GameActionFightTriggerGlyphTrapMessage",
5706: "GameActionFightActivateGlyphTrapMessage",
5771: "GameActionFightCarryCharacterMessage",
8659: "GameActionFightThrowCharacterMessage",
8009: "GameActionFightDropCharacterMessage",
6038: "EmoteListMessage",
2112: "EmoteAddMessage",
4524: "EmoteRemoveMessage",
8135: "EmotePlayAbstractMessage",
3198: "EmotePlayMessage",
1886: "EmotePlayMassiveMessage",
7853: "EmotePlayErrorMessage",
7020: "ChatSmileyMessage",
5839: "ChatCommunityChannelCommunityMessage",
8626: "LocalizedChatSmileyMessage",
1383: "MoodSmileyResultMessage",
2215: "MoodSmileyUpdateMessage",
3973: "ChatSmileyExtraPackListMessage",
1770: "ChatAbstractServerMessage",
6772: "ChatServerMessage",
942: "ChatKolizeumServerMessage",
2080: "ChatAdminServerMessage",
399: "ChatServerWithObjectMessage",
8617: "ChatServerCopyMessage",
8059: "ChatServerCopyWithObjectMessage",
6135: "ChatErrorMessage",
2625: "EnabledChannelsMessage",
7739: "ChannelEnablingChangeMessage",
7427: "SpellListMessage",
6155: "ForgettableSpellListUpdateMessage",
4353: "ForgettableSpellDeleteMessage",
41: "ForgettableSpellEquipmentSlotsMessage",
6689: "LeaveDialogMessage",
3238: "PauseDialogMessage",
2991: "InteractiveUseErrorMessage",
3900: "InteractiveUsedMessage",
2897: "InteractiveUseEndedMessage",
9493: "InteractiveMapUpdateMessage",
2054: "StatedMapUpdateMessage",
8912: "InteractiveElementUpdatedMessage",
7859: "StatedElementUpdatedMessage",
9315: "ZaapRespawnUpdatedMessage",
7615: "TeleportDestinationsMessage",
9132: "ZaapDestinationsMessage",
5253: "KnownZaapListMessage",
9554: "TeleportBuddiesMessage",
2454: "TeleportBuddiesRequestedMessage",
5491: "TeleportToBuddyOfferMessage",
4968: "TeleportToBuddyCloseMessage",
9777: "TeleportPlayerOfferMessage",
4378: "TeleportPlayerCloseMessage",
3076: "GroupTeleportPlayerOfferMessage",
2716: "GroupTeleportPlayerCloseMessage",
7767: "SpellVariantActivationMessage",
3065: "StatsUpgradeResultMessage",
4436: "ChallengeListMessage",
9097: "ChallengeTargetsMessage",
5894: "ChallengeResultMessage",
2779: "ChallengeNumberMessage",
8830: "ChallengeProposalMessage",
8045: "ChallengeSelectedMessage",
8563: "ChallengeAddMessage",
4667: "ChallengeModSelectedMessage",
4926: "ChallengeBonusChoiceSelectedMessage",
6850: "EntityInformationMessage",
266: "EntitiesInformationMessage",
9652: "AchievementListMessage",
2058: "AchievementDetailsMessage",
2020: "AchievementDetailedListMessage",
1205: "AchievementAlmostFinishedDetailedListMessage",
1474: "AchievementFinishedMessage",
1898: "AchievementFinishedInformationMessage",
1060: "AchievementRewardSuccessMessage",
3079: "AchievementRewardErrorMessage",
1328: "FriendGuildWarnOnAchievementCompleteStateMessage",
3443: "AchievementsPioneerRanksMessage",
6819: "DungeonKeyRingMessage",
6518: "DungeonKeyRingUpdateMessage",
1751: "UpdateMapPlayersAgressableStatusMessage",
5808: "UpdateSelfAgressableStatusMessage",
5019: "AlignmentRankUpdateMessage",
5999: "CompassResetMessage",
872: "CompassUpdateMessage",
9981: "CompassUpdatePartyMemberMessage",
5424: "AtlasPointInformationsMessage",
4778: "CompassUpdatePvpSeekMessage",
2039: "AbstractPartyMessage",
5451: "AbstractPartyEventMessage",
2363: "PartyModifiableStatusMessage",
729: "PartyInvitationMessage",
3539: "PartyInvitationDungeonMessage",
8607: "PartyInvitationDetailsMessage",
2367: "PartyInvitationDungeonDetailsMessage",
7618: "PartyInvitationCancelledForGuestMessage",
1327: "PartyCancelInvitationNotificationMessage",
1724: "PartyRefuseInvitationNotificationMessage",
6016: "PartyCannotJoinErrorMessage",
6577: "PartyJoinMessage",
7060: "PartyNewGuestMessage",
5707: "PartyUpdateMessage",
4529: "PartyNewMemberMessage",
4231: "PartyUpdateLightMessage",
2046: "PartyEntityUpdateLightMessage",
7328: "PartyMemberRemoveMessage",
9438: "PartyMemberEjectedMessage",
6439: "PartyLeaderUpdateMessage",
4068: "PartyFollowStatusUpdateMessage",
8066: "PartyLocateMembersMessage",
83: "PartyLeaveMessage",
4958: "PartyKickedByMessage",
2879: "PartyRestrictedMessage",
8038: "PartyDeletedMessage",
5384: "PartyLoyaltyStatusMessage",
6938: "AbstractPartyMemberInFightMessage",
8285: "PartyMemberInStandardFightMessage",
2380: "PartyMemberInBreachFightMessage",
9591: "PartyNameUpdateMessage",
7989: "PartyNameSetErrorMessage",
8056: "DungeonPartyFinderAvailableDungeonsMessage",
6905: "DungeonPartyFinderListenErrorMessage",
9524: "DungeonPartyFinderRoomContentMessage",
5056: "DungeonPartyFinderRoomContentUpdateMessage",
9509: "DungeonPartyFinderRegisterSuccessMessage",
3226: "DungeonPartyFinderRegisterErrorMessage",
2506: "ContactAddFailureMessage",
8361: "SpouseStatusMessage",
4172: "FriendsListMessage",
5647: "AcquaintancesListMessage",
7779: "SpouseInformationsMessage",
6674: "FriendAddFailureMessage",
2270: "AcquaintanceAddedMessage",
3185: "FriendAddedMessage",
7293: "FriendUpdateMessage",
4930: "FriendDeleteResultMessage",
584: "FriendWarnOnConnectionStateMessage",
5243: "WarnOnPermaDeathStateMessage",
2158: "FriendWarnOnLevelGainStateMessage",
8565: "FriendStatusShareStateMessage",
8123: "IgnoredListMessage",
7186: "IgnoredAddFailureMessage",
3797: "IgnoredAddedMessage",
2365: "IgnoredDeleteResultMessage",
1036: "KohUpdateMessage",
506: "KothEndMessage",
9461: "AreaFightModificatorUpdateMessage",
1039: "ClientUIOpenedMessage",
2467: "ClientUIOpenedByObjectMessage",
669: "GuildListMessage",
7376: "GuildLogbookInformationMessage",
753: "GuildChestTabContributionsMessage",
683: "GuildChestTabLastContributionMessage",
8050: "GuildChestTabContributionMessage",
156: "GuildSummaryMessage",
5711: "GuildCreationStartedMessage",
515: "GuildModificationStartedMessage",
4018: "GuildCreationResultMessage",
775: "GuildModificationResultMessage",
4003: "GuildInvitedMessage",
2343: "GuildInvitationStateRecruterMessage",
9851: "GuildInvitationStateRecrutedMessage",
2814: "GuildJoinedMessage",
8750: "GuildMemberOnlineStatusMessage",
4406: "GuildInformationsGeneralMessage",
6362: "GuildInformationsMembersMessage",
6708: "GuildInformationsMemberUpdateMessage",
7168: "GuildInformationsPaddocksMessage",
7246: "GuildMemberLeavingMessage",
3266: "GuildLeftMessage",
2644: "GuildMembershipMessage",
5408: "GuildLevelUpMessage",
5207: "GuildHousesInformationMessage",
1590: "GuildHouseUpdateInformationMessage",
4888: "GuildHouseRemoveMessage",
4625: "GuildPaddockBoughtMessage",
1415: "GuildPaddockRemovedMessage",
4318: "GuildMotdMessage",
6422: "GuildMotdSetErrorMessage",
1996: "GuildBulletinMessage",
8324: "GuildBulletinSetErrorMessage",
7863: "GuildFactsErrorMessage",
5626: "GuildFactsMessage",
3908: "GuildRanksMessage",
6534: "AllianceCreationStartedMessage",
2149: "AllianceModificationStartedMessage",
7302: "AllianceCreationResultMessage",
3693: "AllianceModificationResultMessage",
5529: "AllianceMemberOnlineStatusMessage",
8801: "AllianceApplicationDeletedMessage",
4969: "AlliancePlayerApplicationAbstractMessage",
9706: "AlliancePlayerApplicationInformationMessage",
7142: "AlliancePlayerNoApplicationInformationMessage",
4844: "AllianceApplicationIsAnsweredMessage",
3610: "AllianceListApplicationAnswerMessage",
3470: "AllianceListApplicationModifiedMessage",
1686: "AllianceApplicationReceivedMessage",
8886: "AllianceApplicationPresenceMessage",
977: "AllianceRecruitmentInformationMessage",
523: "AllianceRecruitmentInvalidateMessage",
9032: "AllianceInvitedMessage",
6551: "AllianceInvitationStateRecruterMessage",
7264: "AllianceInvitationStateRecrutedMessage",
5220: "AllianceJoinedMessage",
626: "AllianceMemberLeavingMessage",
6490: "AllianceLeftMessage",
3547: "AllianceMembershipMessage",
2436: "AllianceSummaryMessage",
4210: "AllianceFactsErrorMessage",
9269: "AllianceFactsMessage",
4427: "AllianceRanksMessage",
3877: "AllianceMemberInformationUpdateMessage",
9553: "AllianceListMessage",
4178: "AlliancePartialListMessage",
4562: "AllianceInsiderInfoMessage",
5386: "AllianceFightInfoMessage",
9676: "AllianceFightStartedMessage",
1947: "AllianceFightFinishedMessage",
1193: "AllianceFightPhaseUpdateMessage",
5310: "AllianceFightFighterAddedMessage",
944: "AllianceFightFighterRemovedMessage",
4661: "AllianceMotdMessage",
6006: "AllianceMotdSetErrorMessage",
8751: "AllianceBulletinMessage",
8685: "AllianceBulletinSetErrorMessage",
2186: "TaxCollectorErrorMessage",
3893: "TopTaxCollectorListMessage",
5744: "TaxCollectorStateUpdateMessage",
7370: "TaxCollectorAddedMessage",
2310: "TaxCollectorRemovedMessage",
5361: "TaxCollectorAttackedMessage",
4787: "TaxCollectorAttackedResultMessage",
3704: "TaxCollectorHarvestedMessage",
4833: "TaxCollectorMovementsOfflineMessage",
2451: "TaxCollectorEquipmentUpdateMessage",
1625: "ConfirmationOfListeningTaxCollectorUpdatesMessage",
2428: "TaxCollectorOrderedSpellUpdatedMessage",
9900: "TaxCollectorPresetsMessage",
2628: "TaxCollectorPresetSpellUpdatedMessage",
8248: "RecruitmentInformationMessage",
5184: "GuildRecruitmentInvalidateMessage",
8782: "GuildApplicationDeletedMessage",
4745: "GuildPlayerApplicationAbstractMessage",
656: "GuildPlayerApplicationInformationMessage",
6961: "GuildPlayerNoApplicationInformationMessage",
3637: "GuildApplicationIsAnsweredMessage",
948: "GuildListApplicationAnswerMessage",
7224: "GuildListApplicationModifiedMessage",
8148: "GuildApplicationReceivedMessage",
9885: "GuildApplicationPresenceMessage",
8036: "ListenersOfSynchronizedStorageMessage",
1826: "AddListenerOnSynchronizedStorageMessage",
91: "RemoveListenerOnSynchronizedStorageMessage",
7733: "PrismsListMessage",
1525: "PrismAddOrUpdateMessage",
4672: "PrismRemoveMessage",
2072: "ChallengeFightJoinRefusedMessage",
48: "PrismAttackedMessage",
8541: "PrismAttackResultMessage",
5214: "NuggetsInformationMessage",
3323: "QuestListMessage",
8372: "QuestStartedMessage",
1736: "QuestValidatedMessage",
3508: "QuestObjectiveValidatedMessage",
4373: "QuestStepValidatedMessage",
2945: "QuestStepStartedMessage",
830: "QuestStepInfoMessage",
6589: "FollowedQuestsMessage",
141: "WatchQuestStepInfoMessage",
5644: "WatchQuestListMessage",
7443: "NotificationListMessage",
3884: "NotificationByServerMessage",
8244: "SubscriptionLimitationMessage",
8183: "SubscriptionZoneMessage",
7707: "GuestLimitationMessage",
5810: "GuestModeMessage",
5023: "ListMapNpcsQuestStatusUpdateMessage",
5877: "NpcGenericActionFailureMessage",
6302: "PortalDialogCreationMessage",
3289: "NpcDialogCreationMessage",
5481: "NpcDialogQuestionMessage",
3500: "TaxCollectorDialogQuestionBasicMessage",
8713: "TaxCollectorDialogQuestionExtendedMessage",
3125: "AlliancePrismDialogQuestionMessage",
1171: "EntityTalkMessage",
9539: "JobDescriptionMessage",
386: "JobLevelUpMessage",
8763: "JobExperienceMultiUpdateMessage",
6979: "JobExperienceUpdateMessage",
1331: "JobExperienceOtherPlayerUpdateMessage",
1737: "JobAllowMultiCraftRequestMessage",
8902: "JobMultiCraftAvailableSkillsMessage",
8710: "JobCrafterDirectoryListMessage",
9206: "JobCrafterDirectorySettingsMessage",
6723: "JobBookSubscriptionMessage",
3245: "JobCrafterDirectoryRemoveMessage",
9328: "JobCrafterDirectoryAddMessage",
2116: "JobCrafterDirectoryEntryMessage",
654: "KamasUpdateMessage",
3774: "ObjectGroundAddedMessage",
7785: "ObjectGroundListAddedMessage",
5855: "ObjectGroundRemovedMessage",
3407: "ObjectGroundRemovedMultipleMessage",
8042: "InventoryContentMessage",
8887: "WatchInventoryContentMessage",
9158: "ShortcutBarContentMessage",
1627: "ShortcutBarAddErrorMessage",
4981: "ShortcutBarRemoveErrorMessage",
6501: "ShortcutBarSwapErrorMessage",
5972: "ShortcutBarRefreshMessage",
8757: "ShortcutBarRemovedMessage",
125: "ShortcutBarReplacedMessage",
7356: "MultiTabStorageMessage",
6526: "StorageInventoryContentMessage",
8968: "StorageKamasUpdateMessage",
2670: "StorageObjectUpdateMessage",
5323: "StorageObjectsUpdateMessage",
8450: "StorageObjectRemoveMessage",
1673: "StorageObjectsRemoveMessage",
7483: "SetUpdateMessage",
9677: "InventoryWeightMessage",
4510: "ObjectMovementMessage",
6866: "ObjectAddedMessage",
1527: "ObjectsAddedMessage",
1521: "GoldAddedMessage",
2089: "ObjectErrorMessage",
6668: "ObjectDeletedMessage",
5219: "ObjectsDeletedMessage",
204: "ObjectQuantityMessage",
5664: "ObjectsQuantityMessage",
7821: "ObjectModifiedMessage",
5441: "ObjectJobAddedMessage",
9678: "ObtainedItemMessage",
7133: "ObtainedItemWithBonusMessage",
6015: "LivingObjectMessageMessage",
2086: "SymbioticObjectErrorMessage",
7196: "SymbioticObjectAssociatedMessage",
5215: "WrapperObjectErrorMessage",
3871: "WrapperObjectAssociatedMessage",
2255: "MimicryObjectPreviewMessage",
3920: "MimicryObjectErrorMessage",
1127: "MimicryObjectAssociatedMessage",
1001: "InvalidPresetsMessage",
8873: "PresetsMessage",
6815: "ItemForPresetUpdateMessage",
889: "PresetSavedMessage",
7630: "PresetSaveErrorMessage",
6319: "PresetDeleteResultMessage",
799: "PresetUseResultMessage",
5059: "PresetUseResultWithMissingIdsMessage",
6145: "ExchangeMoneyMovementInformationMessage",
7440: "ExchangeCraftCountModifiedMessage",
3411: "ExchangeObjectMessage",
8426: "ExchangeObjectAddedMessage",
9703: "ExchangeObjectsAddedMessage",
8090: "ExchangeObjectRemovedMessage",
8928: "ExchangeObjectsRemovedMessage",
7078: "ExchangeObjectModifiedMessage",
7326: "ExchangeObjectsModifiedMessage",
5697: "ExchangeObjectPutInBagMessage",
5602: "ExchangeObjectRemovedFromBagMessage",
9367: "ExchangeObjectModifiedInBagMessage",
4910: "ExchangeKamaModifiedMessage",
7160: "ExchangePodsModifiedMessage",
4154: "ExchangeMultiCraftCrafterCanUseHisRessourcesMessage",
1313: "ExchangeRequestedMessage",
5103: "ExchangeRequestedTradeMessage",
3043: "ExchangeStartedMessage",
5028: "ExchangeStartedWithPodsMessage",
2977: "ExchangeStartedWithStorageMessage",
4135: "ExchangeStartedWithMultiTabStorageMessage",
2613: "ExchangeBidHouseBuyResultMessage",
1557: "ExchangeBidHouseItemAddOkMessage",
8101: "ExchangeBidHouseItemRemoveOkMessage",
3696: "ExchangeBidHouseGenericItemAddedMessage",
3347: "ExchangeBidHouseGenericItemRemovedMessage",
9001: "ExchangeBidHouseInListAddedMessage",
9240: "ExchangeBidHouseInListUpdatedMessage",
4180: "ExchangeBidHouseInListRemovedMessage",
9295: "ExchangeBidHouseUnsoldItemsMessage",
2524: "ExchangeOfflineSoldItemsMessage",
4377: "ExchangeIsReadyMessage",
3673: "ExchangeStoppedMessage",
9232: "ExchangeErrorMessage",
384: "ExchangeLeaveMessage",
3985: "DecraftResultMessage",
4137: "RecycleResultMessage",
8322: "ExchangeStartOkNpcTradeMessage",
1662: "ExchangeStartOkRunesTradeMessage",
9395: "ExchangeStartOkEvolutiveObjectRecycleTradeMessage",
5637: "EvolutiveObjectRecycleResultMessage",
1067: "ExchangeStartOkRecycleTradeMessage",
6130: "ExchangeStartOkNpcShopMessage",
4122: "ExchangeOkMultiCraftMessage",
7869: "ExchangeCraftResultMessage",
1423: "ExchangeCraftResultWithObjectIdMessage",
4819: "ExchangeCraftResultWithObjectDescMessage",
95: "ExchangeCraftResultMagicWithObjectDescMessage",
6115: "ExchangeStartedMountStockMessage",
9791: "ExchangeStartedTaxCollectorShopMessage",
9278: "ExchangeStartedBidSellerMessage",
4280: "ExchangeStartedBidBuyerMessage",
4274: "ExchangeBidPriceMessage",
7209: "ExchangeBidPriceForSellerMessage",
6572: "ExchangeTypesExchangerDescriptionForUserMessage",
2738: "ExchangeTypesItemsExchangerDescriptionForUserMessage",
1630: "ExchangeWeightMessage",
3970: "ExchangeTaxCollectorGetMessage",
2498: "ItemNoMoreAvailableMessage",
9839: "ExchangeBuyOkMessage",
49: "ExchangeSellOkMessage",
4276: "ExchangeWaitingResultMessage",
1232: "ExchangeStartOkMountWithOutPaddockMessage",
2274: "ExchangeStartOkMountMessage",
5267: "ExchangeMountStableErrorMessage",
9743: "ExchangeMountsStableAddMessage",
8350: "ExchangeMountsPaddockAddMessage",
2861: "ExchangeMountsStableBornAddMessage",
6129: "ExchangeMountsStableRemoveMessage",
9608: "ExchangeMountsPaddockRemoveMessage",
3055: "ExchangeMountsTakenFromPaddockMessage",
4615: "ExchangeMountFreeFromPaddockMessage",
7996: "ExchangeMountSterilizeFromPaddockMessage",
8956: "ExchangeBidSearchOkMessage",
5298: "ExchangeItemAutoCraftStopedMessage",
6203: "ExchangeStartOkCraftMessage",
4096: "ExchangeStartOkCraftWithInformationMessage",
7458: "ExchangeStartOkMulticraftCrafterMessage",
5378: "ExchangeStartOkMulticraftCustomerMessage",
2584: "ExchangeCrafterJobLevelupMessage",
1248: "ExchangeStartOkJobIndexMessage",
2319: "ExchangeCraftPaymentModifiedMessage",
1346: "UpdateMountCharacteristicsMessage",
9293: "ExchangeStartedTaxCollectorEquipmentMessage",
5074: "ObjectAveragePricesErrorMessage",
2729: "ObjectAveragePricesMessage",
100: "PurchasableDialogMessage",
7345: "AccountHouseMessage",
3385: "HousePropertiesMessage",
4284: "HouseBuyResultMessage",
6800: "HouseSellingUpdateMessage",
8317: "HouseToSellListMessage",
7676: "HouseGuildNoneMessage",
8722: "HouseGuildRightsMessage",
5838: "PaddockBuyResultMessage",
4650: "PaddockPropertiesMessage",
4196: "PaddockSellBuyDialogMessage",
8213: "GameDataPlayFarmObjectAnimationMessage",
7795: "PaddockToSellListMessage",
5461: "HavenBagRoomUpdateMessage",
9897: "HavenBagPackListMessage",
9417: "EditHavenBagStartMessage",
2362: "EditHavenBagFinishedMessage",
9352: "HavenBagDailyLoteryMessage",
135: "HavenBagFurnituresMessage",
2021: "MapComplementaryInformationsDataInHavenBagMessage",
7957: "HavenBagPermissionsUpdateMessage",
8001: "InviteInHavenBagClosedMessage",
949: "InviteInHavenBagMessage",
5037: "InviteInHavenBagOfferMessage",
9430: "MountSterilizedMessage",
7843: "MountReleasedMessage",
2688: "MountRenamedMessage",
9050: "MountXpRatioMessage",
137: "MountDataMessage",
2483: "MountDataErrorMessage",
110: "MountSetMessage",
8582: "MountUnSetMessage",
5171: "MountEquipedErrorMessage",
3880: "MountRidingMessage",
9218: "GameDataPaddockObjectRemoveMessage",
652: "GameDataPaddockObjectAddMessage",
9121: "GameDataPaddockObjectListAddMessage",
3490: "MountEmoteIconUsedOkMessage",
9268: "LockableShowCodeDialogMessage",
7522: "LockableCodeResultMessage",
107: "LockableStateUpdateAbstractMessage",
7692: "LockableStateUpdateHouseDoorMessage",
569: "LockableStateUpdateStorageMessage",
9246: "DocumentReadingBeginMessage",
9970: "OpenGuideBookMessage",
3749: "TitlesAndOrnamentsListMessage",
455: "TitleGainedMessage",
4759: "TitleLostMessage",
9883: "OrnamentGainedMessage",
2799: "OrnamentLostMessage",
1653: "TitleSelectedMessage",
3338: "TitleSelectErrorMessage",
7251: "OrnamentSelectedMessage",
6401: "OrnamentSelectErrorMessage",
4925: "ContactLookMessage",
6346: "ContactLookErrorMessage",
4859: "SocialNoticeMessage",
4597: "BulletinMessage",
3100: "SocialNoticeSetErrorMessage",
9621: "AccessoryPreviewErrorMessage",
1503: "AccessoryPreviewMessage",
3: "HaapiBufferListMessage",
5031: "HaapiConfirmationMessage",
7090: "HaapiValidationMessage",
1448: "HaapiBuyValidationMessage",
4765: "HaapiApiKeyMessage",
1934: "HaapiShopApiKeyMessage",
4769: "FinishMoveListMessage",
8368: "TreasureHuntShowLegendaryUIMessage",
7470: "TreasureHuntRequestAnswerMessage",
7235: "TreasureHuntMessage",
1937: "TreasureHuntFinishedMessage",
3567: "TreasureHuntDigRequestAnswerMessage",
2459: "TreasureHuntDigRequestAnswerFailedMessage",
6871: "TreasureHuntFlagRequestAnswerMessage",
1628: "TreasureHuntAvailableRetryCountUpdateMessage",
8989: "BreachStateMessage",
6556: "BreachCharactersMessage",
427: "BreachBonusMessage",
9989: "BreachBudgetMessage",
21: "BreachSavedMessage",
1486: "BreachBranchesMessage",
1741: "BreachRewardsMessage",
560: "BreachRewardBoughtMessage",
5842: "BreachInvitationOfferMessage",
9260: "BreachInvitationResponseMessage",
6049: "BreachInvitationCloseMessage",
5018: "BreachKickResponseMessage",
9235: "AnomalySubareaInformationResponseMessage",
2045: "AlignmentWarEffortProgressionMessage",
2916: "CharacterAlignmentWarEffortProgressionMessage",
7642: "AlignmentWarEffortDonatePreviewMessage",
1517: "AlignmentWarEffortDonationResultMessage",
4627: "HaapiTokenMessage",
349: "HaapiAuthErrorMessage",
4199: "HaapiSessionMessage",
8138: "ReportResponseMessage",
8856: "DebtsUpdateMessage",
7828: "DebtsDeleteMessage",
5717: "ActivitySuggestionsMessage",
7721: "AlterationsMessage",
8844: "AlterationAddedMessage",
9284: "AlterationRemovedMessage",
563: "AlterationsUpdatedMessage",
6944: "SurrenderStateMessage",
99: "SurrenderInfoResponseMessage",
6177: "SurrenderVoteStartMessage",
6154: "SurrenderVoteUpdateMessage",
6083: "SurrenderVoteEndMessage",
6059: "OpponentSurrenderMessage"
}

all_items = {}

# check https://docs.dofusdu.de/#/resources/get-items-resources-single to get all items

all_types = {
    4367: "CharacterBaseInformations",
         9391: "PartyMemberInformations",
         2056: "PartyMemberArenaInformations",
         3577: "PartyInvitationMemberInformations",
         3983: "CharacterHardcoreOrEpicInformations",
         4052: "ChallengeTargetInformation",
         540: "ChallengeTargetWithAttackerInformation",
         2447: "EntityDispositionInformations",
         619: "IdentifiedEntityDispositionInformations",
         3736: "FightEntityDispositionInformations",
         6837: "AbstractSocialGroupInfos",
         2995: "BasicAllianceInformations",
         5416: "BasicNamedAllianceInformations",
         1197: "AllianceInformation",
         6340: "AllianceFactSheetInformation",
         4606: "BasicGuildInformations",
         7929: "GuildInformations",
         643: "GuildFactSheetInformations",
         9836: "GuildInsiderFactSheetInformations",
         643: "GuildFactSheetInformations",
         9836: "GuildInsiderFactSheetInformations",
         6340: "AllianceFactSheetInformation",
         9281: "PrismGeolocalizedInformation",
         65: "PrismInformation",
         4594: "AlliancePrismInformation",
         7229: "AllianceInsiderPrismInformation",
         6701: "CharacterCharacteristic",
         901: "CharacterCharacteristicDetailed",
         1943: "CharacterUsableCharacteristicDetailed",
         3951: "CharacterCharacteristicValue",
         9810: "FightTeamMemberInformations",
         4535: "FightTeamMemberCharacterInformations",
         793: "FightTeamMemberWithAllianceCharacterInformations",
         4832: "FightTeamMemberTaxCollectorInformations",
         7397: "FightTeamMemberMonsterInformations",
         5854: "FightTeamMemberEntityInformation",
         3291: "FightTeamInformations",
         8585: "FightAllianceTeamInformations",
         714: "GameFightCharacteristics",
         3594: "FightResultListEntry",
         613: "FightResultFighterListEntry",
         6507: "FightResultTaxCollectorListEntry",
         6813: "FightResultPlayerListEntry",
         2795: "FightResultMutantListEntry",
         8078: "FightResultAdditionalData",
         7233: "FightResultPvpData",
         5571: "FightResultExperienceData",
         4079: "AbstractFightDispellableEffect",
         2521: "FightTemporaryBoostEffect",
         4574: "FightTemporaryBoostStateEffect",
         7119: "FightTemporarySpellBoostEffect",
         2061: "FightDetailedTemporaryBoostEffect",
         9695: "FightTemporaryBoostWeaponDamagesEffect",
         3450: "FightTemporarySpellImmunityEffect",
         5487: "FightTriggeredEffect",
         7605: "ObjectEffect",
         3930: "ObjectEffectInteger",
         3987: "ObjectEffectCreature",
         5489: "ObjectEffectLadder",
         843: "ObjectEffectMinMax",
         7031: "ObjectEffectDuration",
         3424: "ObjectEffectString",
         670: "ObjectEffectDice",
         3435: "ObjectEffectDate",
         3353: "ObjectEffectMount",
         470: "UpdateMountCharacteristic",
         2137: "UpdateMountBooleanCharacteristic",
         5600: "UpdateMountIntegerCharacteristic",
         5117: "Shortcut",
         8861: "ShortcutObject",
         1697: "ShortcutObjectPreset",
         2079: "ShortcutObjectItem",
         576: "ShortcutSpell",
         4118: "ShortcutSmiley",
         1189: "ShortcutEmote",
         3288: "ShortcutEntitiesPreset",
         6607: "AchievementAchieved",
         9874: "AchievementAchievedRewardable",
         2099: "IgnoredInformations",
         941: "IgnoredOnlineInformations",
         861: "FriendInformations",
         9348: "FriendOnlineInformations",
         1584: "AcquaintanceInformation",
         251: "AcquaintanceOnlineInformation",
         8260: "FriendSpouseInformations",
         8676: "FriendSpouseOnlineInformations",
         2087: "InteractiveElementSkill",
         7880: "InteractiveElementNamedSkill",
         6065: "InteractiveElement",
         2952: "InteractiveElementWithAgeBonus",
         9391: "PartyMemberInformations",
         2056: "PartyMemberArenaInformations",
         3577: "PartyInvitationMemberInformations",
         5790: "PartyEntityBaseInformation",
         118: "PartyEntityMemberInformation",
         3573: "SkillActionDescription",
         1078: "SkillActionDescriptionTimed",
         5684: "SkillActionDescriptionCollect",
         5905: "SkillActionDescriptionCraft",
         2374: "HouseInformations",
         8406: "AccountHouseInformations",
         2801: "HouseInformationsInside",
         409: "HouseInformationsForGuild",
         5255: "HouseOnMapInformations",
         3219: "HouseInstanceInformations",
         4071: "HouseGuildedInformations",
         5612: "PaddockBuyableInformations",
         4294: "PaddockGuildedInformations",
         3056: "GameContextActorPositionInformations",
         9060: "GameContextActorInformations",
         5601: "GameFightFighterInformations",
         8061: "GameFightAIInformations",
         1792: "GameFightMonsterInformations",
         7656: "GameFightMonsterWithAlignmentInformations",
         7175: "GameFightTaxCollectorInformations",
         4176: "GameFightFighterNamedInformations",
         3578: "GameFightCharacterInformations",
         419: "GameFightMutantInformations",
         4556: "GameFightEntityInformation",
         8764: "GameRolePlayActorInformations",
         2808: "GameRolePlayNamedActorInformations",
         9318: "GameRolePlayHumanoidInformations",
         2574: "GameRolePlayMutantInformations",
         9304: "GameRolePlayCharacterInformations",
         9212: "GameRolePlayMountInformations",
         8347: "GameRolePlayNpcInformations",
         7588: "GameRolePlayNpcWithQuestInformations",
         7360: "GameRolePlayGroupMonsterInformations",
         6822: "GameRolePlayGroupMonsterWaveInformations",
         9279: "GameRolePlayTreasureHintInformations",
         4101: "GameRolePlayTaxCollectorInformations",
         7369: "GameRolePlayPrismInformations",
         9999: "GameRolePlayPortalInformations",
         9060: "GameContextActorInformations",
         5601: "GameFightFighterInformations",
         8061: "GameFightAIInformations",
         1792: "GameFightMonsterInformations",
         7656: "GameFightMonsterWithAlignmentInformations",
         7175: "GameFightTaxCollectorInformations",
         4176: "GameFightFighterNamedInformations",
         3578: "GameFightCharacterInformations",
         419: "GameFightMutantInformations",
         4556: "GameFightEntityInformation",
         8764: "GameRolePlayActorInformations",
         2808: "GameRolePlayNamedActorInformations",
         9318: "GameRolePlayHumanoidInformations",
         2574: "GameRolePlayMutantInformations",
         9304: "GameRolePlayCharacterInformations",
         9212: "GameRolePlayMountInformations",
         8347: "GameRolePlayNpcInformations",
         7588: "GameRolePlayNpcWithQuestInformations",
         7360: "GameRolePlayGroupMonsterInformations",
         6822: "GameRolePlayGroupMonsterWaveInformations",
         9279: "GameRolePlayTreasureHintInformations",
         4101: "GameRolePlayTaxCollectorInformations",
         7369: "GameRolePlayPrismInformations",
         9999: "GameRolePlayPortalInformations",
         8764: "GameRolePlayActorInformations",
         2808: "GameRolePlayNamedActorInformations",
         9318: "GameRolePlayHumanoidInformations",
         2574: "GameRolePlayMutantInformations",
         9304: "GameRolePlayCharacterInformations",
         9212: "GameRolePlayMountInformations",
         8347: "GameRolePlayNpcInformations",
         7588: "GameRolePlayNpcWithQuestInformations",
         7360: "GameRolePlayGroupMonsterInformations",
         6822: "GameRolePlayGroupMonsterWaveInformations",
         9279: "GameRolePlayTreasureHintInformations",
         4101: "GameRolePlayTaxCollectorInformations",
         7369: "GameRolePlayPrismInformations",
         9999: "GameRolePlayPortalInformations",
         495: "HumanInformations",
         7701: "HumanOption",
         446: "HumanOptionObjectUse",
         7953: "HumanOptionAlliance",
         1132: "HumanOptionGuild",
         5782: "HumanOptionOrnament",
         7646: "HumanOptionEmote",
         2189: "HumanOptionTitle",
         2036: "HumanOptionSkillUse",
         4364: "HumanOptionSpeedMultiplier",
         8287: "HumanOptionFollowers",
         1672: "TaxCollectorStaticInformations",
         4158: "TaxCollectorInformations",
         1982: "TaxCollectorComplementaryInformations",
         4183: "TaxCollectorLootInformations",
         5931: "TaxCollectorWaitingForHelpInformations",
         5953: "GroupMonsterStaticInformations",
         4829: "GroupMonsterStaticInformationsWithAlternatives",
         7048: "QuestActiveInformations",
         7451: "QuestActiveDetailedInformations",
         7248: "QuestObjectiveInformations",
         8731: "QuestObjectiveInformationsWithCompletion",
         339: "SpawnInformation",
         5062: "BaseSpawnMonsterInformation",
         8568: "SpawnScaledMonsterInformation",
         571: "SpawnMonsterInformation",
         3409: "SpawnCharacterInformation",
         4847: "SpawnCompanionInformation",
         1891: "GameContextBasicSpawnInformation",
         5419: "GameContextSummonsInformation",
         5601: "GameFightFighterInformations",
         8061: "GameFightAIInformations",
         1792: "GameFightMonsterInformations",
         7656: "GameFightMonsterWithAlignmentInformations",
         7175: "GameFightTaxCollectorInformations",
         4176: "GameFightFighterNamedInformations",
         3578: "GameFightCharacterInformations",
         419: "GameFightMutantInformations",
         4556: "GameFightEntityInformation",
         4794: "GameFightFighterLightInformations",
         3925: "GameFightFighterMonsterLightInformations",
         5195: "GameFightFighterNamedLightInformations",
         3310: "GameFightFighterTaxCollectorLightInformations",
         3181: "GameFightFighterEntityLightInformation",
         315: "MapCoordinates",
         7010: "MapCoordinatesAndId",
         1599: "MapCoordinatesExtended",
         3628: "Preset",
         5695: "PresetsContainerPreset",
         2553: "IconNamedPreset",
         7774: "SpellsPreset",
         6253: "ForgettableSpellsPreset",
         1993: "StatsPreset",
         6250: "EntitiesPreset",
         4653: "FullStatsPreset",
         4783: "ItemsPreset",
         8185: "TreasureHuntStep",
         9275: "TreasureHuntStepFollowDirectionToPOI",
         5858: "TreasureHuntStepDig",
         9719: "TreasureHuntStepFight",
         8809: "TreasureHuntStepFollowDirectionToHint",
         9008: "TreasureHuntStepFollowDirection",
         1300: "AbstractPlayerSearchInformation",
         3389: "PlayerSearchTagInformation",
         3022: "PlayerSearchCharacterNameInformation",
         2396: "PortalInformation",
         7507: "BreachBranch",
         8307: "ExtendedBreachBranch",
         4080: "ExtendedLockedBreachBranch",
         8307: "ExtendedBreachBranch",
         4080: "ExtendedLockedBreachBranch",
         2273: "PlayerStatus",
         8257: "PlayerStatusExtended",
         9977: "ServerSessionConstant",
         7359: "ServerSessionConstantString",
         2867: "ServerSessionConstantInteger",
         4175: "ServerSessionConstantLong",
         1815: "StatisticData",
         7834: "StatisticDataInt",
         7901: "StatisticDataBoolean",
         1762: "StatisticDataShort",
         4102: "StatisticDataString",
         4573: "StatisticDataByte",
         8943: "DebtInformation",
         2104: "KamaDebtInformation",
         8590: "GuildLogbookEntryBasicInformation",
         3270: "GuildRankActivity",
         8680: "GuildPlayerRankUpdateActivity",
         9067: "GuildLogbookChestActivity",
         3398: "GuildLevelUpActivity",
         3935: "GuildPaddockActivity",
         2970: "GuildPlayerFlowActivity",
         7681: "GuildUnlockNewTabActivity",
         8655: "SurrenderResponse",
         8906: "SurrenderRefused",
         9548: "SurrenderRefusedBeforeTurn",
         2726: "SurrenderRefusedBeforeVote",
         8859: "SurrenderAccepted",
         3674: "SurrenderVoteResponse",
         1140: "SurrenderVoteRefused",
         5188: "SurrenderVoteRefusedWaitBetweenVotes",
         9709: "SurrenderVoteRefusedBeforeTurn",
         8978: "SurrenderVoteRefusedAlreadyAsked",
         8687: "SurrenderVoteAccepted"
}

class CustomDataWrapper:
    def __init__(self, data = None):
        self.data = data if data else bytearray()

    def writeByte(self, value):
        self.data += value.to_bytes(1, byteorder='big')

    def writeShort(self, value):
        self.data += value.to_bytes(2, byteorder='big')

    def writeInt(self, value):
        self.data += value.to_bytes(4, byteorder='big')

    def writeDouble(self, value):
        self.data += value.to_bytes(8, byteorder='big')

    def writeUTF(self, value):
        self.writeShort(len(value))
        self.data += value.encode('utf-8')

    def readByte(self):
        return int.from_bytes(self.data[:1], byteorder='big')

    def readShort(self):
        return int.from_bytes(self.data[:2], byteorder='big')
    
    def readUnsignedShort(self):
        return int.from_bytes(self.data[:2], byteorder='big')

    def readInt(self):
        return int.from_bytes(self.data[:4], byteorder='big')

    def readDouble(self):
        return int.from_bytes(self.data[:8], byteorder='big')
    
    def readVarUhLong(self):
        value = 0
        i = 0
        while i < 64:
            byte = self.readByte()
            value = value | (byte & 127) << i
            if byte & 128 == 0:
                return value
            i += 7
        raise ValueError("Too much data")
    
    def readVarUhInt(self):
        value = 0
        i = 0
        while i < 32:
            byte = self.readByte()
            value = value | (byte & 127) << i
            if byte & 128 == 0:
                return value
            i += 7
        raise ValueError("Too much data")

    def readUTF(self):
        length = self.readShort()
        value = self.data[2:2+length].decode('utf-8')
        self.data = self.data[2+length:]
        return value

class ChatAbstractServerMessage:
    def __init__(self, channel = 0, content = '', timestamp = 0, fingerprint = ''):
        self.channel = channel
        self.content = content
        self.timestamp = timestamp
        self.fingerprint = fingerprint

    def serialize(self, output: CustomDataWrapper):
        output.writeByte(self.channel)
        output.writeUTF(self.content)
        if self.timestamp < 0:
            raise ValueError("Forbidden value (" + str(self.timestamp) + ") on element timestamp.")
        output.writeInt(self.timestamp)
        output.writeUTF(self.fingerprint)

    def deserialize(self, input: Buffer):
        # self.channel = input.readByte()
        # self.content = input.readUTF()
        # self.timestamp = input.readInt()
        # self.fingerprint = input.readUTF()
        self.channel = input.readByte()
        self.content = input.readUTF()
        self.timestamp = input.readInt()
        self.fingerprint = input.readUTF()

    def getMessageId(self) -> int:
        return 880

class ChatServerMessage(ChatAbstractServerMessage):
    def __init__(self, channel = 0, content = '', timestamp = 0, fingerprint = '', senderId = 0, senderName = '', prefix = '', senderAccountId = 0):
        super().__init__(channel, content, timestamp, fingerprint)
        self.senderId = senderId
        self.senderName = senderName
        self.prefix = prefix
        self.senderAccountId = senderAccountId

    def serialize(self, output: CustomDataWrapper):
        super().serialize(output)
        if self.senderId < -9007199254740990 or self.senderId > 9007199254740990:
            raise ValueError("Forbidden value (" + str(self.senderId) + ") on element senderId.")
        output.writeDouble(self.senderId)
        output.writeUTF(self.senderName)
        output.writeUTF(self.prefix)
        if self.senderAccountId < 0:
            raise ValueError("Forbidden value (" + str(self.senderAccountId) + ") on element senderAccountId.")
        output.writeInt(self.senderAccountId)

    def deserialize(self, input):
        super().deserialize(input)
        self.senderId = input.readDouble()
        self.senderName = input.readUTF()
        self.prefix = input.readUTF()
        self.senderAccountId = input.readInt()

    def getMessageId(self) -> int:
        return 881
    
    def __str__(self) -> str:
        return f"channel: {self.channel}, content: {self.content}, timestamp: {self.timestamp}, fingerprint: {self.fingerprint}, senderId: {self.senderId}, senderName: {self.senderName}, prefix: {self.prefix}, senderAccountId: {self.senderAccountId}"

class BidExchangerObjectInfo:
    def __init__(self) -> None:
        self.objectUID = 0
        self.objectGID = 0
        self.objectType = 0
        self.effects = []
        self.prices = []
      
    def deserialize(self, input: CustomDataWrapper):
        _id4 = 0
        _item4 = None
        _val5 = 0
        self._objectUIDFunc(input)
        self._objectGIDFunc(input)
        self._objectTypeFunc(input)
        _effectsLen = input.readUnsignedShort()

        for _ in range(_effectsLen):
            _id4 = input.readUnsignedShort()
            # _item4 = ProtocolTypeManager.getInstance(ObjectEffect,_id4),
            # _item4.deserialize(input)
            # self.effects.append(_item4)

        _pricesLen = input.readUnsignedShort()
        for _ in range(_pricesLen):
            _val5 = input.readVarUhLong() # or readDouble
            if _val5 < 0 or _val5 > 9007199254740992:
                raise ValueError("Forbidden value (" + str(_val5) + ") on elements of prices.")
            self.prices.append(_val5)

    def _objectUIDFunc(self, input: CustomDataWrapper):
        self.objectUID = input.readVarUhInt()
        if self.objectUID < 0:
            raise ValueError("Forbidden value (" + str(self.objectUID) + ") on element of BidExchangerObjectInfo.objectUID.")
    
    def _objectGIDFunc(self, input: CustomDataWrapper):
        self.objectGID = input.readVarUhInt()
        if self.objectGID < 0:
            raise ValueError("Forbidden value (" + str(self.objectGID) + ") on element of BidExchangerObjectInfo.objectGID.")

    def _objectTypeFunc(self, input: CustomDataWrapper):
        self.objectType = input.readInt()
        if self.objectType < 0:
            raise ValueError("Forbidden value (" + str(self.objectType) + ") on element of BidExchangerObjectInfo.objectType.")
        
    def __str__(self):
        return f"objectUID: {self.objectUID}, objectGID: {self.objectGID}, objectType: {self.objectType}, effects: {self.effects}, prices: {self.prices}"

class ExchangeTypesExchangerDescriptionForUserMessage:
    def __init__(self) -> None:
        self.objectType = 0
        self.typeDescription = []
        self._isInitialized = True

    def deserialize(self, input: CustomDataWrapper):
        self._objectTypeFunc(input)
        _typeDescriptionLen = input.readUnsignedShort()
        for _ in range(_typeDescriptionLen):
            _val2 = input.readVarUhInt()
            if _val2 < 0:
                raise ValueError("Forbidden value (" + str(_val2) + ") on elements of typeDescription.")
            self.typeDescription.append(_val2)
    
    def _objectTypeFunc(self, input: CustomDataWrapper):
        self.objectType = input.readInt()
        if self.objectType < 0:
            raise ValueError("Forbidden value (" + str(self.objectType) + ") on element of ExchangeTypesExchangerDescriptionForUserMessage.objectType.")
        
    def __str__(self) -> str:
        # return f"objectType: {self.objectType}, typeDescription: [" + ', '.join([str(i) for i in self.typeDescription]) + "]"
        return f"objectType: {self.objectType}, typeDescription: [" + ', '.join([all_items[i] if i in all_items else str(i) for i in self.typeDescription]) + "]"

class ExchangeTypesItemsExchangerDescriptionForUserMessage:
    def __init__(self, objectGID = 0, objectType = 0, itemTypeDescriptions = None):
        self.objectGID = objectGID
        self.objectType = objectType
        self.itemTypeDescriptions = []
        self._isInitialized = True

    def getMessageId(self) -> int:
        return 2738

    def deserialize(self, input: CustomDataWrapper):
        self._objectGIDFunc(input)
        self._objectTypeFunc(input)
        _itemTypeDescriptionsLen: int = input.readUnsignedShort()
        for _ in range(_itemTypeDescriptionsLen):
            _item3 = BidExchangerObjectInfo()
            _item3.deserialize(input)
            self.itemTypeDescriptions.append(_item3)

    def _objectGIDFunc(self, input: CustomDataWrapper):
        self.objectGID = input.readVarUhInt()
        if self.objectGID < 0:
            raise ValueError("Forbidden value (" + str(self.objectGID) + ") on element of ExchangeTypesItemsExchangerDescriptionForUserMessage.objectGID.")
      
    def _objectTypeFunc(self, input: CustomDataWrapper):
        self.objectType = input.readInt()
        if self.objectType < 0:
            raise ValueError("Forbidden value (" + str(self.objectType) + ") on element of ExchangeTypesItemsExchangerDescriptionForUserMessage.objectType.")
    
    def __str__(self):
        # return f"objectGID: {self.objectGID}, objectType: {self.objectType}, itemTypeDescriptions: [" + ', '.join([str(i) for i in self.itemTypeDescriptions]) + "]" 
        if self.objectType in all_items:
            return f"Object: {all_items[self.objectType]}, itemTypeDescriptions: [\n" + '\n'.join([str(i) for i in self.itemTypeDescriptions]) + "]"

id_to_class = {
    1770: ChatAbstractServerMessage,
    6772: ChatServerMessage,
    2738: ExchangeTypesItemsExchangerDescriptionForUserMessage,
    6572: ExchangeTypesExchangerDescriptionForUserMessage
}

class Msg():
    def __init__(self, buffer: Buffer, protocol):
        self.b = True
        self.protocol = protocol
        self.error = ''
        # print("Buffer: ", buffer)
        try:
            header = int.from_bytes(buffer.read(2), byteorder="big")
            self.id = header >> 2
            self.lenType = header & 3
            self.dataLen = int.from_bytes(buffer.read(self.lenType), byteorder="big")
            self.checkHeader()
            if (self.id in all_message):
                print('Message: ' + all_message[self.id])
                if (self.id in id_to_class):
                    value: ChatServerMessage = id_to_class[self.id]()
                    # print("Buffer: ", buffer)
                    value.deserialize(buffer)
                    sprint(f"{value}")
            else:
                print("Wut ?", self.id, "from:\n", buffer)
            try:
                self.data = Data(buffer.read(self.dataLen))
            except Exception as e:
                pass
        except IndexError as e:
            buffer.pos = 0
            self.b = False
        except ValueError:
            buffer.pos = 0
            self.b = False
        except Exception as e:
            eprint("Exception:" + e)
        else:
            buffer.end()

    def checkHeader(self):
        if not self.lenType in [0, 1, 2, 3]:
            self.error = 'Wrong lenType "' + str(self.lenType) + '"'
            raise ValueError

    def __bool__(self):
        return self.b

class Sniffer:
    def __init__(self, concatMode = True):
        self.protocolBuilder = ProtocolBuilder()
        self.protocol = self.protocolBuilder.protocol
        self.buffer = Buffer()
        self.concatMode = concatMode
        self.lastPkt = None

    def run(self, callback, whitelist = None):
        self.callback = callback
        self.whitelist = whitelist
        sniff(
            filter='tcp src port 5555',
            lfilter = lambda pkt: pkt.haslayer(Raw),
            prn = lambda pkt: self.receive(pkt)
        )

    def receive(self, pkt):
        if self.lastPkt and pkt.getlayer(IP).src != self.lastPkt.getlayer(IP).src:
            self.lastPkt = None
        if self.lastPkt and pkt.getlayer(IP).id < self.lastPkt.getlayer(IP).id:
            self.buffer.reorder(bytes(pkt.getlayer(Raw)),
            len(self.lastPkt.getlayer(Raw)))
        else:
            if self.concatMode:
                self.buffer += bytes(pkt.getlayer(Raw))
            else:
                self.buffer = Buffer()
                self.buffer += bytes(pkt.getlayer(Raw))
        self.lastPkt = pkt
        msg = Msg(self.buffer, self.protocol)
        # while msg:
        #     # print('ID: ' + str(msg.id) + ' - dataLen: ' + str(len(msg.data)))
        #     if self.whitelist:
        #         if msg.id in self.whitelist:
        #             self.callback(msg.id, self.protocolBuilder.build(msg.id, msg.data))
        #     else:
        #             self.callback(msg.id, self.protocolBuilder.build(msg.id, msg.data))
        #     msg = Msg(self.buffer, self.protocol)