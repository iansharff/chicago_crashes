import pandas as pd
import numpy as np

CRASHES_DROP = [
    'RD_NO',
    'CRASH_DATE_EST_I',
    'REPORT_TYPE',
    'NOT_RIGHT_OF_WAY_I',
    'DATE_POLICE_NOTIFIED',
    'SEC_CONTRIBUTORY_CAUSE',
    'STREET_NO',
    'STREET_DIRECTION',
    'STREET_NAME',
    'BEAT_OF_OCCURRENCE',
    'PHOTOS_TAKEN_I',
    'STATEMENTS_TAKEN_I',
    'DOORING_I',
    'WORK_ZONE_TYPE',
    'WORKERS_PRESENT_I',
    'INJURIES_UNKNOWN',
    'INJURIES_INCAPACITATING',
    'INJURIES_NON_INCAPACITATING',
    'INJURIES_REPORTED_NOT_EVIDENT',
    'INJURIES_NO_INDICATION',
    'LOCATION'
]


driving = [
    'FAILING TO YIELD RIGHT-OF-WAY',
    'FOLLOWING TOO CLOSELY',
    'IMPROPER OVERTAKING/PASSING',
    'FAILING TO REDUCE SPEED TO AVOID CRASH',
    'IMPROPER BACKING',
    'IMPROPER LANE USAGE',
    'IMPROPER TURNING/NO SIGNAL',
    'DRIVING SKILLS/KNOWLEDGE/EXPERIENCE',
    'OPERATING VEHICLE IN ERRATIC, RECKLESS, CARELESS, NEGLIGENT OR AGGRESSIVE MANNER',
    'DISTRACTION - FROM INSIDE VEHICLE',
    'PHYSICAL CONDITION OF DRIVER',
    'UNDER THE INFLUENCE OF ALCOHOL/DRUGS (USE WHEN ARREST IS EFFECTED)',
    'DRIVING ON WRONG SIDE/WRONG WAY',
    'EXCEEDING AUTHORIZED SPEED LIMIT',
    'EXCEEDING SAFE SPEED FOR CONDITIONS',
    'CELL PHONE USE OTHER THAN TEXTING',
    'HAD BEEN DRINKING (USE WHEN ARREST IS NOT MADE)',
    'TURNING RIGHT ON RED',
    'DISTRACTION - OTHER ELECTRONIC DEVICE (NAVIGATION DEVICE, DVD PLAYER, ETC.)',
    'TEXTING',
]

disregarding_signs = [
    'DISREGARDING TRAFFIC SIGNALS',
    'DISREGARDING STOP SIGN',
    'DISREGARDING OTHER TRAFFIC SIGNS',
    'DISREGARDING ROAD MARKINGS',
    'DISREGARDING YIELD SIGN',
    'PASSING STOPPED SCHOOL BUS'
    ]


environment = [
    'WEATHER',
    'VISION OBSCURED (SIGNS, TREE LIMBS, BUILDINGS, ETC.)',
    'DISTRACTION - FROM OUTSIDE VEHICLE',
    'ROAD ENGINEERING/SURFACE/MARKING DEFECTS',
    'ROAD CONSTRUCTION/MAINTENENCE',
    'EVASIVE ACTION DUE TO ANIMAL, OBJECT, NONMOTORIST',
    'ANIMAL',
    'OBSTRUCTED CROSSWALKS',
    'EQUIPMENT - VEHICLE CONDITION'
]
def bin_prim_causes(dataframe):
    dataframe['PRIM_CONTRIBUTORY_CAUSE']


if __name__ == '__main__':
    crashes = pd.read_csv('chicago_crashes.csv').drop(columns=CRASHES_DROP)
    print(crashes.columns)