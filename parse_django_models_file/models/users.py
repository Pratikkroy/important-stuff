class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_membership_id = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=245, blank=True, null=True)
    user_mobile = models.BigIntegerField(blank=True, null=True)
    alt_phone_number = models.BigIntegerField(blank=True, null=True)
    user_email = models.CharField(max_length=245, blank=True, null=True)
    user_gender = models.CharField(max_length=6, blank=True, null=True)
    user_age_group = models.CharField(max_length=6, blank=True, null=True)
    user_address_line_1 = models.CharField(max_length=245, blank=True, null=True)
    user_address_line_2 = models.CharField(max_length=245, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    user_pin_code = models.IntegerField(blank=True, null=True)
    user_street = models.TextField(blank=True, null=True)
    state_name = models.CharField(max_length=245, blank=True, null=True)
    city_name = models.CharField(max_length=245, blank=True, null=True)
    user_next_follow = models.DateTimeField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    text_password = models.TextField(blank=True, null=True)
    one_time_password = models.CharField(max_length=6, blank=True, null=True)
    auth_key = models.TextField(blank=True, null=True)
    user_photo = models.CharField(max_length=245, blank=True, null=True)
    device_os = models.CharField(max_length=45, blank=True, null=True)
    device_id = models.CharField(max_length=245, blank=True, null=True)
    device_name = models.CharField(max_length=45, blank=True, null=True)
    device_type = models.CharField(max_length=245, blank=True, null=True)
    device_token = models.CharField(max_length=245, blank=True, null=True)
    login_provider = models.CharField(max_length=245, blank=True, null=True)
    login_provider_id = models.CharField(max_length=245, blank=True, null=True)
    last_login_referral_source = models.TextField(blank=True, null=True)
    user_old_id = models.BigIntegerField(blank=True, null=True)
    app_version = models.CharField(max_length=10, blank=True, null=True)
    app_key = models.TextField(blank=True, null=True)
    referral_code_name = models.CharField(max_length=45, blank=True, null=True)
    register_referral_source = models.TextField(blank=True, null=True)
    registration_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_credit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    remaining_workouts = models.IntegerField(blank=True, null=True)
    membership_plan_id = models.IntegerField(blank=True, null=True)
    gym_membership_plan = models.IntegerField(blank=True, null=True)
    fit_prime_end_of_cycle = models.DateField(blank=True, null=True)
    total_used_credit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fitcoach_end_of_cycle = models.DateField(blank=True, null=True)
    gym_end_of_cycle = models.DateField(blank=True, null=True)
    diet_end_of_cycle = models.DateField(blank=True, null=True)
    user_type = models.CharField(max_length=45, blank=True, null=True)
    source_of_user = models.CharField(max_length=10, blank=True, null=True)
    user_come_from = models.CharField(max_length=245, blank=True, null=True)
    user_status = models.CharField(max_length=13, blank=True, null=True)
    issue_status = models.CharField(max_length=8, blank=True, null=True)
    is_email_verify = models.CharField(max_length=3, blank=True, null=True)
    is_follow_up = models.CharField(max_length=3, blank=True, null=True)
    is_active = models.CharField(max_length=3, blank=True, null=True)
    is_pass_hold = models.CharField(max_length=3, blank=True, null=True)
    hold_from = models.DateField(blank=True, null=True)
    hold_to = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=145, blank=True, null=True)
    update_by = models.CharField(max_length=145, blank=True, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    notification_sent = models.IntegerField(blank=True, null=True)
    height = models.CharField(max_length=245, blank=True, null=True)
    weight = models.CharField(max_length=245, blank=True, null=True)
    waist = models.CharField(max_length=6, blank=True, null=True)
    fitness_goal = models.CharField(max_length=245, blank=True, null=True)
    pushnotification_status = models.CharField(max_length=3, blank=True, null=True)
    sms_notification_status = models.CharField(max_length=3, blank=True, null=True)
    email_notification = models.CharField(max_length=3, blank=True, null=True)
    unsubscribe_message = models.TextField(blank=True, null=True)
    corporate_id = models.IntegerField(blank=True, null=True)
    total_orders = models.IntegerField(blank=True, null=True)
    user_date_of_birth = models.DateField(blank=True, null=True)
    customer_last_message = models.TextField(blank=True, null=True)
    user_last_message = models.TextField(blank=True, null=True)
    register_preferred_zone = models.CharField(max_length=45, blank=True, null=True)
    current_preferred_zone = models.CharField(max_length=45, blank=True, null=True)
    team_zone_name = models.CharField(max_length=245, blank=True, null=True)
    total_used_workouts = models.IntegerField(blank=True, null=True)
    diet_onboard = models.CharField(max_length=3, blank=True, null=True)
    fitcoach_onboard = models.CharField(max_length=3, blank=True, null=True)
    diet_preference = models.CharField(max_length=45, blank=True, null=True)
    referral_used = models.CharField(max_length=3, blank=True, null=True)
    user_week_start = models.TextField(blank=True, null=True)
    freshchat_restore_id = models.TextField(blank=True, null=True)
    workout_video_category_id = models.IntegerField(blank=True, null=True)
    gym_membership_active_type = models.CharField(max_length=45, blank=True, null=True)
    fitdirect_end_of_cycle = models.DateField(blank=True, null=True)
    fitpass_insure_card = models.DateField(blank=True, null=True)
    twitter_user_id = models.CharField(max_length=45, blank=True, null=True)
    facebook_user_id = models.CharField(max_length=45, blank=True, null=True)
    google_user_id = models.CharField(max_length=45, blank=True, null=True)
    login_referral_channel = models.TextField(blank=True, null=True)
    register_referral_channel = models.TextField(blank=True, null=True)
    notify_to_fitpass = models.TextField(blank=True, null=True)
    gym_start_of_cycle = models.DateField(blank=True, null=True)
    contact_connect = models.CharField(max_length=45, blank=True, null=True)
    is_user_agent = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table =  'fitpass_users'


