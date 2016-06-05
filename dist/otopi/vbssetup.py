"""vm backup scheduler setup."""

import os

from otopi import plugin, util

from ovirt_engine_setup import constants as osetupcons
from ovirt_engine_setup.engine import constants as oenginecons


@util.export
class Plugin(plugin.PluginBase):
    """vm backup scheduler setup."""

    @plugin.event(
        stage=plugin.Stages.STAGE_CLOSEUP,
        after=(
            osetupcons.Stages.DIALOG_TITLES_E_SUMMARY,
        ),
    )
    def enable_vm_backup_scheduler_plugin(self):
        os.system("vm-backup-setup --password=%s"
            % self.environment[oenginecons.ConfigEnv.ADMIN_PASSWORD])
        self.dialog.note(text="vm backup scheduler enabled.")