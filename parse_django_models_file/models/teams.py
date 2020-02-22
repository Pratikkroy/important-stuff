class Teams(models.Model):
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    team_member_id = models.AutoField(primary_key=True)
    email_address = models.CharField(max_length=245)
    password = models.TextField()
    first_name = models.CharField(max_length=245)
    date_of_birth = models.DateField(blank=True, null=True)
    organisation_name = models.TextField(blank=True, null=True)
    team_type = models.CharField(max_length=9, blank=True, null=True)
    termsagreed_doc = models.CharField(max_length=245, blank=True, null=True)
    organisation_logo = models.CharField(max_length=245, blank=True, null=True)
    last_name = models.CharField(max_length=245, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    mobile_number = models.BigIntegerField(blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.CharField(max_length=3, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=145, blank=True, null=True)
    update_by = models.CharField(max_length=145, blank=True, null=True)
    auth_key = models.TextField(blank=True, null=True)
    role = models.ForeignKey('Roles', blank=True, null=True, on_delete=models.SET_NULL)
    last_login_time = models.DateTimeField(blank=True, null=True)
    device_id = models.CharField(max_length=245, blank=True, null=True)
    device_type = models.CharField(max_length=245, blank=True, null=True)
    device_token = models.CharField(max_length=245, blank=True, null=True)
    latitude = models.CharField(max_length=245, blank=True, null=True)
    longitude = models.CharField(max_length=245, blank=True, null=True)
    login_area = models.TextField(blank=True, null=True)
    team_zone_name = models.CharField(max_length=245, blank=True, null=True)
    parent_team_member_id = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=245, blank=True, null=True)
    about_team_member = models.TextField(blank=True, null=True)
    franchise_bank_details = models.TextField(blank=True, null=True)
    studio_followup_email = models.CharField(max_length=245, blank=True, null=True)
    customer_followup_email = models.CharField(max_length=245, blank=True, null=True)
    class Meta:
        managed = False
        db_table =  'fitpass_teams'




