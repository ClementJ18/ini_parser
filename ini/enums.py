import enum

class DamageTypes(enum.Enum):
    FORCE           = 0
    CRUSH           = 1   
    SLASH           = 2
    PIERCE          = 3
    SIEGE           = 4
    STRUCTURAL      = 5

    FLAME           = 6
    FROST           = 7
    HEALING         = 8
    UNRESISTABLE    = 9 
    WATER           = 10
    PENALTY         = 11
    FALLING         = 12
    TOPPLING        = 13
    REFLECTED       = 14
    PASSENGER       = 15
    MAGIC           = 16
    CHOP            = 17
    HERO            = 18
    SPECIALIST      = 19
    URUK            = 20
    HERO_RANGED     = 21
    FLY_INTO        = 22

    UNDEFINED       = 23
    LOGICAL_FIRE    = 24
    CAVALRY         = 25
    CAVALRY_RANGED  = 26
    POISON          = 27
    
class DamageFXTypes(enum.Enum):
    pass

class CommandTypes(enum.Enum):
    CANCEL_UNIT_BUILD               = 0
    CANCEL_UPGRADE                  = 1
    HORDE_TOGGLE_FORMATION          = 2
    TOGGLE_WEAPONSET                = 3
    ATTACK_MOVE                     = 4
    STOP                            = 5
    GUARD                           = 6
    FIRE_WEAPON                     = 7
    SPECIAL_POWER                   = 8
    WAKE_AUTO_PICKUP                = 9
    BLOODTHIRSTY                    = 10
    MONSTERDOCK                     = 11
    OBJECT_UPGRADE                  = 12
    EXIT_CONTAINER                  = 13
    EVACUATE                        = 14
    CREW_EVACUATE                   = 15
    EVACUATE_CONTESTED              = 17
    FOUNDATION_CONSTRUCT            = 18
    SET_RALLY_POINT                 = 19
    SELL                            = 20
    CASTLE_UNPACK                   = 21
    CASTLE_UNPACK_EXPLICIT_OBJECT   = 22
    UNIT_BUILD                      = 23
    PLAYER_UPGRADE                  = 24
    REVIVE                          = 25
    FOUNDATION_CONSTRUCT_CANCEL     = 26
    SPELL_BOOK                      = 27
    PURCHASE_SCIENCE                = 28
    TOGGLE_NO_AUTO_ACQUIRE          = 29
    PLACE_BEACON                    = 30
    POP_VISIBLE_COMMAND_RANGE       = 31
    TOGGLE_STANCE                   = 32
    SET_STANCE                      = 33
    NONE                            = 34
    TOGGLE_WEAPON                   = 35
    DOZER_CONSTRUCT                 = 36
    PUSH_VISIBLE_COMMAND_RANGE      = 37
    CASTLE_UPGRADE                  = 38
    TOGGLE_GATE                     = 39
    START_SELF_REPAIR               = 40
    START_NEIGHBORHOOD_REPAIR       = 41
    CANCEL_NEIGHBORHOOD             = 42
    SPECIAL_POWER_TOGGLE            = 43
    
class Options(enum.Enum):
    OK_FOR_MULTI_SELECT                             = 0
    OPTION_TWO                                      = 1
    CANCELABLE                                      = 2
    OPTION_ONE                                      = 3
    NEED_TARGET_POS                                 = 4
    CONTEXTMODE_COMMAND                             = 5
    NEED_TARGET_ALLY_OBJECT                         = 6
    TOGGLE_IMAGE_ON_WEAPONSET                       = 7
    NEED_TARGET_ENEMY_OBJECT                        = 8
    OPTION_THREE                                    = 9
    NONPRESSABLE                                    = 10
    NEED_TARGET_NEUTRAL_OBJECT                      = 11
    HIDE_WHILE_DISABLED                             = 12
    NEED_UPGRADE                                    = 13
    NO_PLAY_UNIT_SPECIFIC_SOUND_FOR_AUTO_ABILITY    = 14

class UpgradeTypes(enum.Enum):
    OBJECT  = 0
    PLAYER  = 1
    
class ButtonBorderTypes(enum.Enum):
    pass
    
class ModelConditions(enum.Enum):
    pass
    
class Flags(enum.Enum):
    pass
    
class WeaponSlots(enum.Enum):
    pass
    
class KindsOf(enum.Enum):
    OBSTACLE                        = 0
    SELECTABLE                      = 1
    IMMOBILE                        = 2
    CAN_ATTACK                      = 3
    STICK_TO_TERRAIN_SLOPE          = 4
    CAN_CAST_REFLECTIONS            = 5
    SHRUBBERY                       = 6
    STRUCTURE                       = 7
    INFANTRY                        = 8
    CAVALRY                         = 9
    MONSTER                         = 10
    MACHINE                         = 11
    AIRCRAFT                        = 12
    HUGE_VEHICLE                    = 13
    DOZER                           = 14
    SWARM_DOZER                     = 15
    HARVESTER                       = 16
    COMMANDCENTER                   = 17
    CASTLE_CENTER                   = 18
    SALVAGER                        = 19
    WEAPON_SALVAGER                 = 20
    TRANSPORT                       = 21
    BRIDGE                          = 22
    LANDMARK_BRIDGE                 = 23
    BRIDGE_TOWER                    = 24
    PROJECTILE                      = 25
    PRELOAD                         = 26
    NO_GARRISON                     = 27
    CASTLE_KEEP                     = 28
    WAVE_EFFECT                     = 29
    NO_COLLIDE                      = 30
    REPAIR_PAD                      = 31
    HEAL_PAD                        = 32
    STEALTH_GARRISON                = 33
    SUPPLY_GATHERING_CENTER         = 34
    AIRFIELD                        = 35
    DRAWABLE_ONLY                   = 36
    MP_COUNT_FOR_VICTORY            = 37
    REBUILD_HOLE                    = 38
    SCORE                           = 39
    SCORE_CREATE                    = 40
    SCORE_DESTROY                   = 41
    NO_HEAL_ICON                    = 42
    CAN_RAPPEL                      = 43
    PARACHUTABLE                    = 44
    CAN_BE_REPULSED                 = 45
    MOB_NEXUS                       = 46
    IGNORED_IN_GUI                  = 47
    CRATE                           = 48
    CAPTURABLE                      = 49
    LINKED_TO_FLAG                  = 50
    CLEARED_BY_BUILD                = 51
    SMALL_MISSILE                   = 52
    ALWAYS_VISIBLE                  = 53
    UNATTACKABLE                    = 54
    MINE                            = 55
    CLEANUP_HAZARD                  = 56
    PORTABLE_STRUCTURE              = 57
    ALWAYS_SELECTABLE               = 58
    ATTACK_NEEDS_LINE_OF_SIGHT      = 59
    WALK_ON_TOP_OF_WALL             = 60
    DEFENSIVE_WALL                  = 61
    FS_POWER                        = 62
    FS_FACTORY                      = 63
    FS_BASE_DEFENSE                 = 64
    FS_TECHNOLOGY                   = 65
    AIRCRAFT_PATH_AROUND            = 66
    LOW_OVERLAPPABLE                = 67
    FORCEATTACKABLE                 = 68
    AUTO_RALLYPOINT                 = 69
    OATHBREAKER                     = 70
    POWERED                         = 71
    PRODUCED_AT_HELIPAD             = 72
    DRONE                           = 73
    CAN_SEE_THROUGH_STRUCTURE       = 74
    BALLISTIC_MISSILE               = 75
    CLICK_THROUGH                   = 76
    SUPPLY_SOURCE_ON_PREVIEW        = 77
    PARACHUTE                       = 78
    GARRISONABLE_UNTIL_DESTROYED    = 79
    BOAT                            = 80
    IMMUNE_TO_CAPTURE               = 81
    HULK                            = 82
    SHOW_PORTRAIT_WHEN_CONTROLLED   = 83
    SPAWNS_ARE_THE_WEAPONS          = 84
    CANNOT_BUILD_NEAR_SUPPLIES      = 85
    SUPPLY_SOURCE                   = 86
    REVEAL_TO_ALL                   = 87
    DISGUISER                       = 88
    INERT                           = 89
    HERO                            = 90
    IGNORES_SELECT_ALL              = 91
    DONT_AUTO_CRUSH_INFANTRY        = 92
    SIEGE_TOWER                     = 93
    TREE                            = 94
    SHRUB                           = 95
    CLUB                            = 96
    ROCK                            = 97
    THROWN_OBJECT                   = 98
    GRAB_AND_KILL                   = 99
    OPTIMIZED_PROP                  = 100
    ENVIRONMENT                     = 101
    DEFLECT_BY_SPECIAL_POWER        = 102
    WORKING_PASSENGER               = 103
    BASE_FOUNDATION                 = 104
    NEED_BASE_FOUNDATION            = 105
    REACT_WHEN_SELECTED             = 106
    GIMLI                           = 107
    ORC                             = 108
    HORDE                           = 109
    COMBO_HORDE                     = 110
    NONOCCLUDING                    = 111
    NO_FREEWILL_ENTER               = 112
    CAN_USE_SIEGE_TOWER             = 113
    CAN_RIDE_SIEGE_LADDER           = 114
    TACTICAL_MARKER                 = 115
    PATH_THROUGH_EACH_OTHER         = 116
    NOTIFY_OF_PREATTACK             = 117
    GARRISON                        = 118
    MELEE_HORDE                     = 119
    BASE_SITE                       = 120
    INERT_SHROUD_REVEALER           = 121
    OCL_BIT                         = 122
    SPELL_BOOK                      = 123
    DEPRECATED                      = 124
    PATH_THROUGH_INFANTRY           = 125
    NO_FORMATION_MOVEMENT           = 126
    NO_BASE_CAPTURE                 = 127
    ARMY_SUMMARY                    = 128
    HOBBIT                          = 129
    NOT_AUTOACQUIRABLE              = 130
    URUK                            = 131
    CHUNK_VENDOR                    = 132
    ARCHER                          = 133
    MOVE_ONLY                       = 134
    FS_CASH_PRODUCER                = 135
    ROCK_VENDOR                     = 136
    BLOCKING_GATE                   = 137
    CAN_RIDE_BATTERING_RAM          = 138
    SIEGE_LADDER                    = 139
    MINE_TRIGGER                    = 140
    BUFF                            = 141
    GRAB_AND_DROP                   = 142
    PORTER                          = 143
    SCARY                           = 144
    CRITTER_EMITTER                 = 145
    SALT_LICK                       = 146
    CAN_ATTACK_WALLS                = 147
    IGNORE_FOR_VICTORY              = 148
    DO_NOT_CLASSIFY                 = 149
    WALL_UPGRADE                    = 150
    ARMY_OF_DEAD                    = 151
    TAINT                           = 152
    BASE_DEFENSE_FOUNDATION         = 153
    NOT_SELLABLE                    = 154
    WEBBED                          = 155
    WALL_HUB                        = 156
    BUILD_FOR_FREE                  = 157
    IGNORE_FOR_EVA_SPEECH_POSITION  = 158
    MADE_OF_WOOD                    = 159
    MADE_OF_METAL                   = 160
    MADE_OF_STONE                   = 161
    MADE_OF_DIRT                    = 162
    FACE_AWAY_FROM_CASTLE_KEEP      = 163
    BANNER                          = 164
    I_WANT_TO_EAT_YOU               = 165
    INDUSTRY_AFFECTED               = 166
    DWARVENRICHES_AFFECTED          = 167
    GANDALF                         = 168
    ARAGORN                         = 169
    HAS_HEALTH_BAR                  = 170
    BIG_MONSTER                     = 171
    DEPLOYED_MINE                   = 172
    CANNOT_RETALIATE                = 173
    CREEP                           = 174
    TAINTEFFECT                     = 175
    TROLL_BUFF_NUGGET               = 176
    VITAL_FOR_BASE_SURVIVAL         = 177
    DO_NOT_PICK_ME_WHEN_BUILDING    = 178
    SUMMONED                        = 179
    HIDE_IF_FOGGED                  = 180
    ALWAYS_SHOW_HOUSE_COLOR         = 181
    MOVE_FOR_NOONE                  = 182
    WB_DISPLAY_SCRIPT_NAME          = 183
    CAN_CLIMB_WALLS                 = 184
    MUMAKIL_BUFF_NUGGET             = 185
    LARGE_RECTANGLE_PATHFIND        = 186
    SUBMARINE                       = 187
    PORT                            = 188
    WALL_SEGMENT                    = 189
    CREATE_A_HERO                   = 190
    SHIP                            = 191
    OPTIMIZED_SOUND                 = 192
    PASS_EXPERIENCE_TO_CONTAINED    = 193
    DOZER_FACTORY                   = 194
    THREAT_FINDER                   = 195
    ECONOMY_STRUCTURE               = 196
    LIVING_WORLD_BUILDING_MIRROR    = 197
    PIKE                            = 198
    NONCOM                          = 199
    OBSOLETE                        = 200
    SCALEABLE_WALL                  = 201
    SKYBOX                          = 202
    WALL_GATE                       = 203
    CAPTUREFLAG                     = 204
    NEUTRALGOLLUM                   = 205
    PASS_EXPERIENCE_TO_CONTAINER    = 206
    GIANT_BIRD                      = 207
    ORIENTS_TO_CAMERA               = 208
    NEVER_CULL_FOR_MP               = 209
    DONT_USE_CANCEL_BUILD_BUTTON    = 210
    ONE_RING                        = 211
    HEAVY_MELEE_HITTER              = 212
    DONT_HIDE_IF_FOGGED             = 213
    CAN_SHOOT_OVER_WALLS            = 214
    PASS_EXPERIENCE_TO_PRODUCER     = 215
    EXPANSION_PAD                   = 216
    AMPHIBIOUS                      = 217
    SUPPORT                         = 218
    TROLL                           = 219
    SIEGEENGINE                     = 220
    HORDE_MONSTER                   = 221                 
    
class Descriptors(enum.Enum):
    ANY     = 0
    NONE    = 1
    ALL     = 2
    
class Relations(enum.Enum):
    ENEMIES     = 0
    ALLIES      = 1
    SAME_PLAYER = 2
    
class ModifierCategories(enum.Enum):
    LEADERSHIP          = 0
    FORMATION           = 1
    SPELL               = 2
    WEAPON              = 3
    STRUCTURE           = 4
    LEVEL               = 5
    BUFF                = 6
    DEBUFF              = 7
    STUN                = 8
    INNATE_ARMOR        = 9 
    INNATE_DAMAGEMULT   = 10       
    INNATE_VISION       = 11     
    INNATE_AUTOHEAL     = 12     
    INNATE_HEALTH       = 13
    
class Modifier(enum.Enum):
    ARMOR                           = 0
    DAMAGE_ADD                      = 1
    RESIST_FEAR                     = 2
    RESIST_TERROR                   = 3
    RANGE                           = 4
    RESIST_KNOCKBACK                = 5
    HEALTH                          = 6
    VISION                          = 7
    AUTO_HEAL                       = 8
    SHROUD_CLEARING                 = 9
    SEPARATOR                       = 9.5
    DAMAGE_MULT                     = 10
    EXPERIENCE                      = 11
    SPEED                           = 12
    CRUSH_DECELERATE                = 13
    SPELL_DAMAGE                    = 14
    RECHARGE_TIME                   = 15
    PRODUCTION                      = 16
    HEALTH_MULT                     = 17
    RATE_OF_FIRE                    = 18
    MIN_CRUSH_VELOCITY_PERCENTAGE   = 19
    DAMAGE_STRUCTURE_BOUNTY_ADD     = 20
    COMMAND_POINT_BONUS             = 21
    CRUSHABLE_LEVEL                 = 22
    INVULNERABLE                    = 23
    BOUNTY_PERCENTAGE               = 24
    CRUSHED_DECELERATE              = 25
    
    def is_mult(self):
        return self.value > self.__class__.SEPARATOR.value

class EmotionTypes(enum.Enum):
    TAUNT                       = 0
    ALERT                       = 1
    CHEER                       = 2
    HERO_CHEER                  = 3
    CHEER_FOR_ABOUT_TO_CRUSH    = 4
    FEAR                        = 5
    UNCONTROLLABLE_FEAR         = 6
    TERROR                      = 7
    DOOM                        = 8
    BRACE_FOR_BEING_CRUSHED     = 9
    POINT                       = 10
    QUARRELSOME                 = 11
    
class SpecialPowerEnums(enum.Enum):
    SPECIAL_SPELL_BOOK_ELVEN_GIFTS           = 0
    SPECIAL_SPELL_BOOK_DUNEDAIN_ALLIES       = 1
    SPECIAL_WIZARD_BLAST                     = 2
    SPECIAL_WOUND_ARROW                      = 3
    SPECIAL_ATTRIBUTEMOD_CANCELDISGUISE      = 4
    SPECIAL_GENERAL_TARGETLESS_TWO           = 5
    SPECIAL_SPELL_BOOK_MEN_OF_DALE_ALLIES    = 6
    SPECIAL_AT_VISIBLE_OBJECT                = 7
    SPECIAL_TRIGGER_ATTRIBUTE_MODIFIER       = 8
    SPECIAL_GENERAL_TARGETLESS_THREE         = 9
    SPECIAL_SPELL_BOOK_BOMBARD               = 10
    SPECIAL_AT_VISIBLE_GROUNDED_OBJECT       = 11
    SPECIAL_BALROG_WINGS                     = 12
    SPECIAL_GENERAL_TARGETLESS               = 13
    SPECIAL_SHIELD_BUBBLE                    = 14
    
class Dispositions(enum.Enum):
    USE_CLIFF            = 0
    USE_WATER_SURFACE    = 1
    ON_GROUND_ALIGNED    = 2
    LIKE_EXISTING        = 3
    RELATIVE_ANGLE       = 4

class DeathTypes(enum.Enum):
    pass
    
class LogicTypes(enum.Enum):
    pass
    
class WeaponBone(enum.Enum):
    pass
