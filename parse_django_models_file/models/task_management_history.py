class TaskManagementHistory(models.Model):
    task_management_history_id = models.BigAutoField(primary_key=True)
    status_id = models.BigIntegerField(blank=True, null=True)
    requirement_type = models.IntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=145, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    task_management_id = models.BigIntegerField(blank=True, null=True)
    last_changes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fitpass_task_management_history'


