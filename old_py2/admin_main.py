#!/usr/bin/env python
import os
import webapp2

import tba_config

from controllers.admin.admin_api_controller import AdminApiAuthAdd, AdminApiAuthDelete, AdminApiAuthEdit, AdminApiAuthManage
from controllers.admin.admin_apistatus_controller import AdminApiStatus
from controllers.admin.admin_contbuild_controller import AdminContbuildController
from controllers.admin.admin_district_controller import AdminDistrictList, AdminDistrictEdit, \
    AdminDistrictCreate
from controllers.admin.admin_event_controller import AdminEventAddAllianceSelections, AdminEventDeleteTeams, AdminEventAddTeams, AdminEventRemapTeams, AdminEventAddWebcast, AdminEventCreate, AdminEventCreateTest, \
    AdminAddAllianceBackup, AdminEventRemoveWebcast, AdminRefetchEventLocation, AdminPlayoffAdvancementAddController, AdminPlayoffAdvancementPurgeController
from controllers.admin.admin_gameday_controller import AdminGamedayDashboard
from controllers.admin.admin_main_controller import AdminDebugHandler, AdminMain,
from controllers.admin.admin_award_controller import AdminAwardDashboard, AdminAwardEdit, AdminAwardAdd, \
    AdminAwardDelete, AdminAwardAddWithEvent
from controllers.admin.admin_match_controller import AdminVideosAdd, AdminMatchCleanup, AdminMatchDashboard, AdminMatchDelete, AdminMatchDetail, AdminMatchAdd, AdminMatchEdit
from controllers.admin.admin_media_controller import AdminMediaDashboard, AdminMediaDeleteReference, AdminMediaMakePreferred, AdminMediaRemovePreferred, AdminMediaAdd, \
    AdminMediaInstagramImport
from controllers.admin.admin_memcache_controller import AdminMemcacheMain
from controllers.admin.admin_migration_controller import AdminMigration, \
    AdminMigrationCreateEventDetails, AdminMigrationRankings, AdminMigrationAddSurrogates, \
    AdminMigrationBackfillYearDQ, AdminMigrationBackfillEventDQ, \
    AdminMigrationPlayoffAdvancement, AdminMigrationPlayoffAdvancementAll
from controllers.admin.admin_mobile_controller import AdminMobile, AdminBroadcast, AdminMobileWebhooks
from controllers.admin.admin_offseason_scraper_controller import AdminOffseasonScraperController
from controllers.admin.admin_offseason_spreadsheet_controller import AdminOffseasonSpreadsheetController
from controllers.admin.admin_suggestion_controller import AdminCreateTestSuggestions
from controllers.admin.admin_tbans_controller import AdminTBANS
from controllers.admin.admin_team_controller import AdminTeamCreateTest, AdminTeamRobotNameUpdate
from controllers.admin.admin_team_media_mod import AdminTeamMediaModCodeList, AdminTeamMediaModCodeAdd, AdminTeamMediaModCodeEdit
from controllers.admin.admin_user_controller import AdminUserDetail, AdminUserEdit, AdminUserTestSetup, AdminUserList, AdminUserPermissionsList, \
    AdminUserLookup
from google.appengine.ext.webapp import template
template.register_template_library('common.my_filters')

app = webapp2.WSGIApplication([('/admin/', AdminMain),
                               ('/admin/api_auth/add', AdminApiAuthAdd),
                               ('/admin/api_auth/delete/(.*)', AdminApiAuthDelete),
                               ('/admin/api_auth/edit/(.*)', AdminApiAuthEdit),
                               ('/admin/api_auth/manage', AdminApiAuthManage),
                               ('/admin/apistatus', AdminApiStatus),
                               ('/admin/contbuild/(.*)', AdminContbuildController),
                               ('/admin/debug', AdminDebugHandler),
                               ('/admin/event/add_alliance_backup/(.*)', AdminAddAllianceBackup),
                               ('/admin/event/add_alliance_selections/(.*)', AdminEventAddAllianceSelections),
                               ('/admin/event/add_teams/(.*)', AdminEventAddTeams),
                               ('/admin/event/delete_teams/(.*)', AdminEventDeleteTeams),
                               ('/admin/event/add_webcast/(.*)', AdminEventAddWebcast),
                               ('/admin/event/remove_webcast/(.*)', AdminEventRemoveWebcast),
                               ('/admin/event/remap_teams/(.*)', AdminEventRemapTeams),
                               ('/admin/event/update_loaction/(.*)', AdminRefetchEventLocation),
                               ('/admin/event/create', AdminEventCreate),
                               ('/admin/event/create/test', AdminEventCreateTest),
                               ('/admin/award/add', AdminAwardAdd),
                               ('/admin/award/add/(.*)', AdminAwardAddWithEvent),
                               ('/admin/matches', AdminMatchDashboard),
                               ('/admin/match/add', AdminMatchAdd),
                               ('/admin/match/cleanup', AdminMatchCleanup),
                               ('/admin/match/delete/(.*)', AdminMatchDelete),
                               ('/admin/match/edit/(.*)', AdminMatchEdit),
                               ('/admin/match/(.*)', AdminMatchDetail),
                               ('/admin/media', AdminMediaDashboard),
                               ('/admin/media/add_media', AdminMediaAdd),
                               ('/admin/media/modcodes/add', AdminTeamMediaModCodeAdd),
                               ('/admin/media/modcodes/edit/([0-9]+)/([0-9]+)', AdminTeamMediaModCodeEdit),
                               ('/admin/media/modcodes/list', AdminTeamMediaModCodeList),
                               ('/admin/media/modcodes/list/([0-9]+)', AdminTeamMediaModCodeList),
                               ('/admin/media/modcodes/list/([0-9]+)/([0-9]*)', AdminTeamMediaModCodeList),
                               ('/admin/media/import/instagram', AdminMediaInstagramImport),
                               ('/admin/memcache', AdminMemcacheMain),
                               ('/admin/migration', AdminMigration),
                               ('/admin/migration/create_event_details', AdminMigrationCreateEventDetails),
                               ('/admin/migration/migrate_rankings/([0-9]*)', AdminMigrationRankings),
                               ('/admin/migration/add_surrogates/([0-9]*)', AdminMigrationAddSurrogates),
                               ('/admin/migration/backfill_year_dq/([0-9]*)', AdminMigrationBackfillYearDQ),
                               ('/admin/migration/backfill_event_dq/(.*)', AdminMigrationBackfillEventDQ),
                               ('/admin/migration/backfill_playoff_advancement', AdminMigrationPlayoffAdvancementAll),
                               ('/admin/migration/backfill_playoff_advancement/(.*)', AdminMigrationPlayoffAdvancement),
                               ('/admin/offseasons', AdminOffseasonScraperController),
                               ('/admin/offseasons/spreadsheet', AdminOffseasonSpreadsheetController),
                               ('/admin/playoff_advancement/add', AdminPlayoffAdvancementAddController),
                               ('/admin/playoff_advancement/purge/(.*)', AdminPlayoffAdvancementPurgeController),
                               ('/admin/suggestions/create/test', AdminCreateTestSuggestions),
                               ('/admin/team/create/test', AdminTeamCreateTest),
                               ('/admin/user/create/test', AdminUserTestSetup),
                               ('/admin/videos/add', AdminVideosAdd),
                               ('/admin/tbans', AdminTBANS),
                               ('/admin/mobile', AdminMobile),
                               ('/admin/mobile/broadcast', AdminBroadcast),
                               ('/admin/mobile/webhooks', AdminMobileWebhooks),
                               ],
                              debug=tba_config.DEBUG)
