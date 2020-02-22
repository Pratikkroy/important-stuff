class TeamNotifications(models.Model):
    notification_id = models.CharField(primary_key=True, max_length=255)
    created_by = models.CharField(max_length=145, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    source_id = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=36)
    notification_text = models.TextField(blank=True,null=True)

    class Meta:
        managed = False
        db_table = 'fitpass_team_notifications'


