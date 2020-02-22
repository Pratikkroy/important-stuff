class CustomerLeadDataFollowStatus(models.Model):
    customer_lead_data_follow_status_id = models.BigAutoField(primary_key=True)
    customer_lead_data_follow_id = models.BigIntegerField()
    created_by = models.CharField(max_length=145, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    fitpass_id = models.BigIntegerField(blank=True, null=True)
    team_member_id = models.BigIntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    next_followup_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fitpass_customer_lead_data_follow_status'

