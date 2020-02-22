class TaskManagementLogs(models.Model):
    task_management_log_id = models.BigAutoField(primary_key=True)
    updated_by = models.CharField(max_length=145, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    task_management_id = models.BigIntegerField(blank=True, null=True)
    last_changes = models.TextField(blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'fitpass_task_management_logs'

