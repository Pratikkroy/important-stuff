class Corporate(models.Model):
    corporate_id = models.BigAutoField(primary_key=True)
    domain_name = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=245, blank=True, null=True)
    email_address = models.CharField(max_length=245, blank=True, null=True)
    contact_person = models.CharField(max_length=245, blank=True, null=True)
    mobile_number = models.BigIntegerField(blank=True, null=True)
    designation = models.CharField(max_length=245, blank=True, null=True)
    no_of_employees = models.CharField(max_length=245, blank=True, null=True)
    is_follow_up = models.CharField(max_length=14, blank=True, null=True)
    location = models.CharField(max_length=245, blank=True, null=True)
    query_date = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    deal_with_corporate = models.CharField(max_length=3, blank=True, null=True)
    diet_plan_free = models.CharField(max_length=3, blank=True, null=True)
    corporate_url = models.TextField(blank=True, null=True)
    is_active = models.CharField(max_length=3, blank=True, null=True)
    created_by = models.CharField(max_length=145, blank=True, null=True)
    updated_by = models.CharField(max_length=145, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    photo_name = models.TextField(blank=True, null=True)
    last_follow_up_message = models.TextField(blank=True, null=True)
    next_follow_date = models.DateTimeField(blank=True, null=True)
    studio_restriction = models.CharField(max_length=3, blank=True, null=True)
    workout_restriction = models.CharField(max_length=3, blank=True, null=True)
    reservation_email_trigger_on_team_fitpass = models.TextField(blank=True, null=True)
    bought_email_trigger_on_team_fitpass = models.TextField(blank=True, null=True)
    corporate_landing_page_json_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fitpass_corporate'



