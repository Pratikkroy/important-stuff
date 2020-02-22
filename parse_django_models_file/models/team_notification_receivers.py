class TeamNotificationReceivers(models.Model):
    notification_receiver_id = models.BigAutoField(primary_key=True)
    notification = models.ForeignKey('TeamNotifications', models.DO_NOTHING)
    team_member_id = models.BigIntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fitpass_team_notification_receivers'