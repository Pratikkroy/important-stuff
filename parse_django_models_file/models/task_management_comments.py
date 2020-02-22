class TaskManagementComments(models.Model):
    task_management_comment_id = models.BigAutoField(primary_key=True)
    task_management_id = models.BigIntegerField(blank=True, null=True)
    commented_by = models.CharField(max_length=145, blank=True, null=True)
    comment_time = models.DateTimeField(blank=True, null=True)
    comment_text = models.TextField(blank=True, null=True)
    task_status = models.IntegerField(blank=True,null=True)

    class Meta:
        managed = False
        db_table = 'fitpass_task_management_comments'


