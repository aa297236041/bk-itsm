# Generated by Django 3.2.4 on 2022-06-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trigger", "0014_trigger_project_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="action",
            name="signal",
            field=models.CharField(
                choices=[
                    ("CREATE_TICKET", "创建单据"),
                    ("CLOSE_TICKET", "关闭单据"),
                    ("TERMINATE_TICKET", "终止单据"),
                    ("SUSPEND_TICKET", "挂起单据"),
                    ("RECOVERY_TICKET", "恢复单据"),
                    ("DELETE_TICKET", "撤销单据"),
                    ("GLOBAL_ENTER_STATE", "进入节点"),
                    ("GLOBAL_LEAVE_STATE", "离开节点"),
                    ("ENTER_STATE", "进入节点"),
                    ("LEAVE_STATE", "离开节点"),
                    ("DISTRIBUTE_STATE", "分派单据"),
                    ("CLAIM_STATE", "认领单据"),
                    ("DELIVER_STATE", "转单"),
                    ("THROUGH_TRANSITION", "进入分支"),
                    ("CREATE_TASK", "创建任务之后"),
                    ("DELETE_TASK", "删除任务"),
                    ("BEFORE_START_TASK", "执行任务之前"),
                    ("AFTER_FINISH_TASK", "执行任务之后"),
                    ("AFTER_CONFIRM_TASK", "完成任务之后"),
                ],
                max_length=128,
                verbose_name="触发事件信号",
            ),
        ),
    ]