import nox
import Settings
import Inventory
import DoAllDailies
import KRSelect
import Campaign
import Common
import Manager

sNONE = 'none'

##############
# NOX Helpers
##############
def _KillKingsRaid():
    # Bring up recent apps
    Manager.keypress(nox.keypress_RecentApps, Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Kill King's Raid app
    nox.mouse_drag('main_killkingsraid_bottom',
                   'main_killkingsraid_top', 
                   Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter],
                   0.5)

def Back():
    #Manager.click_button('main_backbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.keypress(nox.keypress_Back, Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

##############
# Public Helpers
##############
def Gen_RelaunchKingsRaid ():
    _KillKingsRaid()
    Gen_LaunchKingsRaidAndGoToMainScreen()

# Go to main screen after Nox restarted
def Gen_LaunchKingsRaidAndGoToMainScreen () :
    NoOfClicksToClearTranslucentPopups = 3
    # Launch game from Nox screen till Tap to Play screen
    Manager.click_button('nox_launchgame', Settings.Main[Settings.Main_sGameLaunch_TapToPlayDuration] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Tap to play till main game screen
    Manager.click_button('nox_launchgame', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.click_button('nox_launchgame', Settings.Main[Settings.Main_sGameLaunch_MainGameScreenDuration] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # This will click away main game screen, loading screen, advertisements
    for i in range(0, Settings.Main[Settings.Main_sNoOfClicksToClearAdvertisement]) :
        Manager.click_button('main_advertisement_close', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Close translucent popup separately .. don't wait so long to click again
    for i in range(0, NoOfClicksToClearTranslucentPopups) :
        Manager.click_button('translucentpopup_close', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Just to be sure - click again to clear advertisement
    for i in range(0, Settings.Main[Settings.Main_sNoOfClicksToClearAdvertisement]) :
        Manager.click_button('main_advertisement_close', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        
def Gen_DoStory(i_sWhichChapter = 8, i_bStartBattle = True) :
    # Navigate to chapter
    # currently only support chapter 6 and 8
    if 8 <= i_sWhichChapter :
        Gen_GoToChapter('conquests', 'ch8_conquest', Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('ch8_conquest_naviTo_story_8_20', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('ch8_conquest_naviTo_story_8_25', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('ch8_conquest_naviTo_story_8_24', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('ch8_conquest_naviTo_story_8_23', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('ch8_conquest_naviTo_story_8_23_2', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    elif 7 == i_sWhichChapter :
        Gen_GoToChapter('conquests', 'ch7_conquest', Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('ch7_conquest_naviTo_story_7_8', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    elif 6 == i_sWhichChapter :
        Gen_GoToChapter('conquests', 'ch6_conquest', Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('ch6_conquest_naviTo_story_6_10', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    if i_bStartBattle :
        Manager.click_button('main_preparebattle', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('get_ready_for_battle', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # For now we use Conquests Hero selection for story as well
        KRSelect.Gen_SelectQuestHero(KRSelect.QuestType_Story, False, Settings.Main_sEasyContent)

        Campaign.gen_natural_stamina_farm()

def Gen_DoDragonRaid (i_bStartBattle = True) :
    whichDragonRaid = Settings.DragonRaidConfig[Settings.DragonRaidConfig_sSelectDragonToAuto]

    Manager.click_button('raid_multi', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.click_button('raid_select', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # room settings
    # select correct dragon
    roomSelect = 'raid_select_black'
    if Settings.Fire_DragonRaid_sFireDragonRaid == whichDragonRaid :
        roomSelect = 'raid_select_fire'
        DragonSettings = Settings.Fire_DragonRaid.copy()
    elif Settings.Frost_DragonRaid_sFrostDragonRaid == whichDragonRaid :
        roomSelect = 'raid_select_frost'
        DragonSettings = Settings.Frost_DragonRaid.copy()
    elif Settings.Poison_DragonRaid_sPoisonDragonRaid== whichDragonRaid :
        roomSelect = 'raid_select_poison'
        DragonSettings = Settings.Poison_DragonRaid.copy()
    elif Settings.Black_DragonRaid_sBlackDragonRaid == whichDragonRaid :
        DragonSettings = Settings.Black_DragonRaid.copy()
        nox.mouse_drag('raid_select_list_bottom', 'raid_select_list_top', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # Click to select the correct dragon room
    Manager.click_button(roomSelect, Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # calculate how many levels to decrement
    differenceFromHighestClearedToAutoLevel = abs(DragonSettings[Settings.DragonRaid_sHighestCleared] - DragonSettings[Settings.DragonRaid_sAutoAtThisLevel])
    for i in range (0, differenceFromHighestClearedToAutoLevel) :
        Manager.click_button('raid_select_decrementlevel', Settings.Main[Settings.Main_sDurationAfterClick_Short])
    # uncheck gather raiders
    Manager.click_button('raid_select_gatherraiders', Settings.Main[Settings.Main_sDurationAfterClick_Short])
    Manager.click_button('raid_select_enter', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    KRSelect.Gen_DragonRaid_HeroSelect()

    if i_bStartBattle :
        Manager.click_button('raid_select_SetAutoRepeat', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('raid_select_StartBattle', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        #TODO refill nrg or not?

def Gen_NavigateToGameHomePage(i_bAlreadyInTown = False):
    Gen_NavigateToMain('portal_orvel_herosinn', i_bAlreadyInTown)
    # Exit to home page
    Back()

def Gen_NavigateToMain(i_portal_orvel_placetogo, i_bAlreadyInTown = False) :
    if False == i_bAlreadyInTown :
        Manager.click_button('main_portal', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('upper_dungeon', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('ch1_upper_dungeon', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        # This has to wait longer because we are transiting to another big game screen    
        Manager.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
    Manager.click_button('main_portal', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.click_button('portal_orvel', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.click_button(i_portal_orvel_placetogo, Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

    # This has to wait longer because we are transiting to another big game screen
    Manager.click_button('minipopup_confirmbutton', Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    
# Clears inventory (Assumes we are at main game screen)
def Gen_ClearInventory() :
    # Click inventory
    Manager.click_button('main_inventory', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Grind all (for now)
    Inventory.manage_inventory(True, False)
    # Back to main game screen
    Back()

# Claim Mailbox
def Gen_ClaimMailbox () :
    # Click mailbox icon
    Manager.click_button('main_mailbox', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.click_button('mailbox_claimall', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Short] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    Manager.click_button('mailbox_close', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

# Doesn't really matter the order at which we claim
def Gen_ClaimDailyMission (i_nNumOfMissionsToClaim = 3, i_bClaimFromHomePage = False) :
    Manager.click_button('main_mission', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    for i in range(0, i_nNumOfMissionsToClaim) :
        Manager.click_button('mission_claim_position1', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        Manager.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
    # Back to main
    Back()
    Gen_NavigateToGameHomePage(i_bClaimFromHomePage)

def Gen_GoToChapter (i_sQuestButtonName,
                     i_nChapterName,
                     i_nTransition_duration_alter) :
    Manager.click_button('portal', 2000 + i_nTransition_duration_alter)
    Manager.click_button(i_sQuestButtonName, 2000 + i_nTransition_duration_alter)
    Manager.click_button(i_nChapterName, 2000 + i_nTransition_duration_alter)
    Manager.click_button('move_to_conquest', 6000 + (i_nTransition_duration_alter * 2))  # map render delay

def _GetQuestTypeFromButtonName(i_sButtonName):
    if 'conquests' == i_sButtonName:
        return KRSelect.QuestType_Conquest
    elif 'upper_dungeon':
        return KRSelect.QuestType_UpperDungeon
    else:
        return KRSelect.QuestType_Story

# Auto Upper Dungeon/ Conquest on one chapter
# Protection is in place if you have used up your keys.  This will then effectively click "open" and "x out" over and over, without clicking reset until the macro completes.
def _Gen_Single_Conquest_or_UpperDungeon_Chapter(i_sQuestButtonName,
                                                i_nChapterName,
                                                i_lChapterList,
                                                i_nLongestRunTime_CurrentChapter,
                                                i_nTransition_duration_alter,
                                                i_nHardContentNoOfTimesToRetry,
                                                i_sEasyOrHardContent=sNONE):
    if False == nox.find_settings_file :
        longest_run_time = nox.prompt_user_for_int(
            "Enter longest run in seconds for {0} or 0 to skip (45-90s suggested for hell): ".format(i_nChapterName))  
    else :
        longest_run_time = i_nLongestRunTime_CurrentChapter
        print ("{0} longest run time = {1}".format(i_nChapterName, longest_run_time))

    if longest_run_time > 0:
        Gen_GoToChapter(i_sQuestButtonName, i_nChapterName, i_nTransition_duration_alter)
        Manager.click_button('prepare_battle', 2000 + i_nTransition_duration_alter)
        Manager.click_button('get_ready_for_battle', 2000 + i_nTransition_duration_alter)

        if sNONE != i_sEasyOrHardContent:
            KRSelect.Gen_SelectQuestHero(_GetQuestTypeFromButtonName(i_sQuestButtonName),
                                         False,
                                         i_sEasyOrHardContent)

        if Settings.Main_sHardContent == i_sEasyOrHardContent :            
            print("Single chap gen (HARD)")
            # Start battle instead of Auto repeat
            Manager.click_button('getreadyforbattle_startbattle', longest_run_time * 1000)
            # loop starts from 1 as we've already started the timer after 'Start battle' is clicked
            for i in range(1, i_nHardContentNoOfTimesToRetry) :
                Manager.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                Manager.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                Manager.click_button('battlecompletion_retry', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                Manager.click_button('repeatpopup_singlerepeat', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                Manager.click_button('repeatpopup_close', Settings.Main[Settings.Main_sDurationAfterClick] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
                Manager.click_button('repeatpopup_close', longest_run_time * 1000)
            
            # After we complete click away the obtained message
            Manager.click_button('main_clicknowhere', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
            Manager.click_button('battlecompletion_exit', Settings.Main[Settings.Main_sDurationAfterClick_Long] + Settings.Main[Settings.Main_sTransitionDuration_Alter])
        else :            
            print("Single chap gen (EASY)")
            Manager.click_button('auto_repeat', 2000 + i_nTransition_duration_alter)
            Manager.click_button('repeat_ok', (longest_run_time * 1000 * 5))  # for now this will be 60s per run or 5 min total.  We can make this smarter later.
            # Manager.click_button('insufficient_keys', 2000 + i_nTransition_duration_alter) # should click x_out instead
            Manager.click_button('x_out', 1000 + i_nTransition_duration_alter)
            Manager.click_button('x_out', 1000 + i_nTransition_duration_alter) # second x_out in case of key reset
            Manager.click_button('exit_conquest', 20000 + (i_nTransition_duration_alter * 3)) # long render

    # Done all conquests/ upper dungeons. 
    # This is to ensure that we exit to main screen (in this case to chapter map)
    nox.wait(Settings.Main[Settings.Main_sAnyGameScreenLoadingTime] + Settings.Main[Settings.Main_sTransitionDuration_Alter])

# Highest cleared level shouldn't exceed amount of chapters available for clearing Conquest/Upper dungeon
def Gen_Conquest_UpperDungeon_Helper (i_sQuestButtonName,           #button name.. 
                                      i_lChapterList,
                                      i_lLongestRunTimeList,
                                      i_nHighestClearedChapter,
                                      i_nHardContentNoOfTimesToRetry,
                                      i_nSelectEasyContentHeroesAt,
                                      i_nSelectHardContentHeroesAt,
                                      i_nStartAtChapter = 1):
    #print('All Upper Dungeons should have set levels.  To do this manually, you can start and then stop a battle on the chosen level per dungeon.  This is also a good way to alter which levels/fragments you want to focus on.')

    if False == nox.find_settings_file :
        transition_duration_alter = nox.prompt_user_for_int(
            "Main transition times are 2000 milliseconds.  Please enter a positive or negative value in milliseconds if you want this changed or (enter) for no change: "
        )
    else :
        transition_duration_alter = Settings.Main[Settings.Main_sTransitionDuration_Alter]

    #nHighestClearedLevel = i_nHighestClearedChapter
    #if len(i_lChapterList) < i_nHighestClearedChapter :
    #    nHighestClearedLevel = len(i_lChapterList)

    bEasyHeroHasBeenSelected = False
    bHardHeroHasBeenSelected = False

    for i in range (i_nStartAtChapter, i_nHighestClearedChapter+1) :
        sContent = sNONE
        if (i_nSelectHardContentHeroesAt <= i) :
            if (False == bHardHeroHasBeenSelected) :
                sContent = Settings.Main_sHardContent
                bHardHeroHasBeenSelected = True
                print ("Hard content from: {0}) {1}".format(i, i_lChapterList[i]))
        elif (i_nSelectEasyContentHeroesAt <= i):
            if (False == bEasyHeroHasBeenSelected):
                sContent = Settings.Main_sEasyContent
                bEasyHeroHasBeenSelected = True
                print ("Easy content from: {0}) {1}".format(i, i_lChapterList[i]))
        _Gen_Single_Conquest_or_UpperDungeon_Chapter(i_sQuestButtonName,
                                                    i_lChapterList[i],
                                                    i_lChapterList,
                                                    i_lLongestRunTimeList[i_lChapterList[i]],
                                                    transition_duration_alter,
                                                    i_nHardContentNoOfTimesToRetry,
                                                    sContent)

    Common.confirm(start_condition='The macro should be started only when the Portal button is visible')
    