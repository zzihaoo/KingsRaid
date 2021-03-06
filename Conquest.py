import nox
import DoAllDailies
import Settings
import KRCommon
import Manager

def gen_conquest():
    chapterList = {
        1 : 'ch2_conquest',
        2 : 'ch3_conquest',
        3 : 'ch4_conquest',
        4 : 'ch5_conquest',
        5 : 'ch6_conquest',
        6 : 'ch7_conquest',
        7 : 'ch8_conquest'
        }
    longestRunTimeList = {
        'ch2_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap2_s],
        'ch3_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap3_s],
        'ch4_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap4_s],
        'ch5_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap5_s],
        'ch6_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap6_s],
        'ch7_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap7_s],
        'ch8_conquest' : Settings.Conquest[Settings.Conquest_sLongestRunTime_Chap8_s]
        }

    nSelectEasyContentHeroesAt = 1  # Select heroes for easy content
    nSelectHardContentHeroesAt = Settings.Conquest[Settings.Conquest_sHardContent_StartsFrom]  # Select heroes for hard content (Chapter 8)
    KRCommon.Gen_Conquest_UpperDungeon_Helper(  'conquests',    # button name.. Portal > Conquest
                                                chapterList,
                                                longestRunTimeList,
                                                Settings.Conquest[Settings.Conquest_sHighestClearedChapter] - 1,    # Conquests chapters starts from 2, therefore index-1
                                                Settings.Conquest[Settings.Conquest_sHardContent_NoOfTimesToRetry],
                                                nSelectEasyContentHeroesAt,
                                                nSelectHardContentHeroesAt - 1,
                                                1)     # Conquests chapters starts from 2, therefore index-1
    