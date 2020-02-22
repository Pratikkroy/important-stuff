from django.db import models
from django.contrib.auth.models import User as AuthUser
from core.modals.Studios import *
from core.modals.TaskManagement import *

# Create your models here.
class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=45, blank=True, null=True)
    parent_role = models.ForeignKey('Roles', models.DO_NOTHING, blank=True, null=True)
    class Meta:
        managed = False
        db_table =  'fitpass_roles'


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


class UserReservedSchedules(models.Model):
    user_schedule_id = models.BigAutoField(primary_key=True)
    workout_date = models.DateField(blank=True, null=True)
    security_code = models.CharField(max_length=10, blank=True, null=True)
    workout_status = models.IntegerField(blank=True, null=True)
    studio = models.ForeignKey('Studios', models.DO_NOTHING)
    workout = models.ForeignKey('Workouts', models.DO_NOTHING)
    workout_time = models.ForeignKey('WorkoutSchedules', models.DO_NOTHING)
    reserve_source = models.CharField(max_length=45, blank=True, null=True)
    user_schedule_old_id = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.CharField(max_length=145, blank=True, null=True)
    updated_by = models.CharField(max_length=145, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    feedback_summary = models.TextField(blank=True, null=True)
    studio_payment = models.FloatField(blank=True, null=True)
    workout_time_0 = models.CharField(db_column='workout_time', max_length=45, blank=True,
                                      null=True)  # Field renamed because of name conflict.
    workout_name = models.CharField(max_length=245, blank=True, null=True)
    app_version = models.CharField(max_length=45, blank=True, null=True)
    device_name = models.CharField(max_length=45, blank=True, null=True)
    device_type = models.CharField(max_length=45, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    workout_activity_id = models.IntegerField(blank=True, null=True)
    user_rating = models.TextField(blank=True, null=True)
    workout_cancel_by = models.CharField(max_length=245, blank=True, null=True)
    urc_updated_by = models.CharField(max_length=245, blank=True, null=True)
    workout_cancel_time = models.DateTimeField(blank=True, null=True)
    urc_updated_time = models.DateTimeField(blank=True, null=True)
    team_zone_name = models.CharField(max_length=45, blank=True, null=True)
    workout_reserve_source = models.TextField(blank=True, null=True)
    studio_zone = models.CharField(max_length=245, blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    corporate_id = models.IntegerField(blank=True, null=True)
    workout_cancel_status = models.CharField(max_length=3, blank=True, null=True)
    studio_with_group_id = models.IntegerField(blank=True, null=True)
    conflicting_time = models.CharField(max_length=3, blank=True, null=True)
    conflicting_message = models.TextField(blank=True, null=True)
    conflicting_trying_to_attend = models.DateTimeField(blank=True, null=True)
    studio_qr_code_number = models.CharField(max_length=45, blank=True, null=True)
    user_current_cycle = models.DateField(blank=True, null=True)
    task_management = models.ForeignKey('TaskManagement', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fitpass_user_reserved_schedules'


class WorkoutActivities(models.Model):
    workout_activity_id = models.BigAutoField(primary_key=True)
    activity_name = models.CharField(max_length=255, blank=True, null=True)
    parent_workout_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.CharField(max_length=3, blank=True, null=True)
    icon_name = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=145, blank=True, null=True)
    workout_seo_url = models.TextField(blank=True, null=True)
    reserve_workouts = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table =  'fitpass_workout_activities'

class Workouts(models.Model):
    workout_id = models.BigAutoField(primary_key=True)
    workout_name = models.CharField(max_length=245, blank=True, null=True)
    cost_per_user_per_workout = models.IntegerField(blank=True, null=True)
    no_of_seats_per_workout = models.IntegerField(blank=True, null=True)
    workout_description = models.TextField(blank=True, null=True)
    workout_image = models.TextField(blank=True, null=True)
    workout_seo_url = models.TextField(blank=True, null=True)
    seo_zone_url = models.TextField(blank=True, null=True)
    seo_locality_url = models.TextField(blank=True, null=True)
    workout_meta_keyword = models.TextField(blank=True, null=True)
    workout_meta_description = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=145, blank=True, null=True)
    updated_by = models.CharField(max_length=145, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_active = models.CharField(max_length=3, blank=True, null=True)
    is_batch_created = models.CharField(max_length=3, blank=True, null=True)
    old_workout_id = models.BigIntegerField(blank=True, null=True)
    studio = models.ForeignKey(Studios, models.DO_NOTHING)
    workout_activity = models.ForeignKey(WorkoutActivities, models.DO_NOTHING)
    is_deleted = models.CharField(max_length=3, blank=True, null=True)
    team_zone_name = models.CharField(max_length=245, blank=True, null=True)
    workout_available_days = models.CharField(max_length=245, blank=True, null=True)
    workout_available_time = models.CharField(max_length=245, blank=True, null=True)
    device_id = models.TextField(blank=True, null=True)
    last_activity_role = models.TextField(blank=True, null=True)
    device_type = models.TextField(blank=True, null=True)
    workout_active_from = models.DateField(blank=True, null=True)
    workout_active_to = models.DateField(blank=True, null=True)
    information_need_update = models.TextField(blank=True, null=True)
    ladies_workout = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table =  'fitpass_workouts'

class WorkoutSchedules(models.Model):
    workout_time_id = models.BigAutoField(primary_key=True)
    number_of_seats = models.IntegerField(blank=True, null=True)
    start_time = models.CharField(max_length=6, blank=True, null=True)
    end_time = models.CharField(max_length=6, blank=True, null=True)
    workout_days = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.CharField(max_length=3, blank=True, null=True)
    created_by = models.CharField(max_length=145, blank=True, null=True)
    updated_by = models.CharField(max_length=145, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    workout = models.ForeignKey('Workouts', models.DO_NOTHING)
    studio = models.ForeignKey('Studios', models.DO_NOTHING)
    workout_batch_old_id = models.BigIntegerField(blank=True, null=True)
    is_deleted = models.CharField(max_length=3, blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    schedule_specific_days = models.CharField(max_length=45, blank=True, null=True)
    team_zone_name = models.CharField(max_length=245, blank=True, null=True)
    time_type = models.IntegerField(blank=True, null=True)
    schedule_active_from = models.DateField(blank=True, null=True)
    schedule_active_to = models.DateField(blank=True, null=True)
    last_activity_role = models.TextField(blank=True, null=True)
    device_id = models.TextField(blank=True, null=True)
    device_type = models.TextField(blank=True, null=True)
    information_need_update = models.TextField(blank=True, null=True)
    workout_reserve_type = models.CharField(max_length=5, blank=True, null=True)
    workout_reserve_value = models.IntegerField(blank=True, null=True)
    upcoming_activity_startdate = models.DateField(blank=True, null=True)
    upcoming_start_time = models.CharField(max_length=6, blank=True, null=True)
    upcoming_end_time = models.CharField(max_length=6, blank=True, null=True)
    upcoming_workout_days = models.CharField(max_length=20, blank=True, null=True)
    upcoming_number_of_seats = models.IntegerField(blank=True, null=True)
    upcoming_schedule_specific_days = models.CharField(max_length=45, blank=True, null=True)
    upcoming_activity_complete = models.CharField(max_length=3, blank=True, null=True)
    last_update_history = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fitpass_workout_schedules'


class MembershipPlans(models.Model):
    membership_plan_id = models.BigAutoField(primary_key=True)
    product_type = models.IntegerField(blank=True, null=True)
    plan_type = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    selling_amount = models.FloatField(blank=True, null=True)
    actual_amount = models.FloatField(blank=True, null=True)
    duration = models.CharField(max_length=245, blank=True, null=True)
    no_of_workout = models.CharField(max_length=245, blank=True, null=True)
    plan_free_type = models.IntegerField(blank=True, null=True)
    plan_free_duration = models.CharField(max_length=245, blank=True, null=True)
    is_active = models.CharField(max_length=3, blank=True, null=True)
    studio_category = models.IntegerField(blank=True, null=True)
    team_zone_name = models.CharField(max_length=245, blank=True, null=True)
    created_by = models.CharField(max_length=145, blank=True, null=True)
    updated_by = models.CharField(max_length=145, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    offer_name = models.CharField(max_length=245, blank=True, null=True)
    offer_type = models.CharField(max_length=245, blank=True, null=True)
    is_redeem = models.CharField(max_length=3, blank=True, null=True)
    discount_amount = models.CharField(max_length=245, blank=True, null=True)
    coupon_type = models.CharField(max_length=245, blank=True, null=True)
    coupon_name = models.CharField(max_length=245, blank=True, null=True)
    coupon_id = models.IntegerField(blank=True, null=True)
    upgrade_membership_amount = models.FloatField(blank=True, null=True)
    lat_long = models.CharField(max_length=245, blank=True, null=True)
    plan_deeplink_url = models.TextField(blank=True, null=True)
    subscription_id = models.TextField(blank=True, null=True)
    corporate_id = models.IntegerField(blank=True, null=True)
    tax_applicable = models.IntegerField(blank=True, null=True)
    about_plan = models.TextField(blank=True, null=True)
    tax_applicable_amount = models.TextField(blank=True, null=True)
    membership_price = models.FloatField(blank=True, null=True)
    user_can_redeem = models.IntegerField(blank=True, null=True)
    user_can_apply_coupon = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    total_payment_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fitpass_membership_plans'

class TransactionHistory(models.Model):
    transaction_history_id = models.BigAutoField(primary_key=True)
    total_order_price = models.FloatField()
    received_order_price = models.FloatField()
    product_type = models.IntegerField()
    order_date = models.DateTimeField(blank=True, null=True)
    customer_name = models.CharField(max_length=245, blank=True, null=True)
    user_membership_id = models.CharField(max_length=245, blank=True, null=True)
    user_id = models.BigIntegerField()
    request_header = models.TextField(blank=True, null=True)
    transaction_number = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=145, blank=True, null=True)
    order_details = models.TextField(blank=True, null=True)
    transaction_month = models.CharField(max_length=8, blank=True, null=True)
    tax = models.CharField(max_length=45, blank=True, null=True)
    team_zone_name = models.CharField(max_length=245, blank=True, null=True)
    coupon_code = models.CharField(max_length=245, blank=True, null=True)
    transaction_source = models.CharField(max_length=245, blank=True, null=True)
    is_active = models.CharField(max_length=3, blank=True, null=True)
    last_team_response = models.TextField(blank=True, null=True)
    membership_transfer_from_zone_name = models.CharField(max_length=245, blank=True, null=True)
    membership_transfer_to_zone_name = models.CharField(max_length=245, blank=True, null=True)
    membership_transfer_from_zone = models.CharField(max_length=245, blank=True, null=True)
    membership_transfer_zone = models.CharField(max_length=245, blank=True, null=True)
    membership_transfer_remarks = models.TextField(blank=True, null=True)
    payments_details = models.TextField(blank=True, null=True)
    user_source = models.CharField(max_length=45, blank=True, null=True)
    payments_settlement_details = models.TextField(blank=True, null=True)
    payment_gateway_id = models.TextField(blank=True, null=True)
    payments_active_from = models.CharField(max_length=245, blank=True, null=True)
    membership_transfer_date = models.DateTimeField(blank=True, null=True)
    product_cycle = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    membership_transfer_from_product_type = models.IntegerField(blank=True, null=True)
    app_version = models.CharField(max_length=45, blank=True, null=True)
    device_type = models.TextField(blank=True, null=True)
    device_name = models.TextField(blank=True, null=True)
    transaction_type = models.CharField(max_length=245, blank=True, null=True)
    lead_follower_team_member_id = models.CharField(max_length=45, blank=True, null=True)
    membership_plan_id = models.IntegerField(blank=True, null=True)
    corporate_id = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    total_discount = models.FloatField(blank=True, null=True)
    coupon_discount = models.FloatField(blank=True, null=True)
    redeem_points = models.FloatField(blank=True, null=True)
    fitprime_price = models.FloatField(blank=True, null=True)
    referral_channel = models.TextField(blank=True, null=True)
    user_preferred_city = models.CharField(max_length=45, blank=True, null=True)
    is_subscription = models.IntegerField(blank=True, null=True)
    fitcard_agents_id = models.IntegerField(blank=True, null=True)
    task_management = models.ForeignKey('TaskManagement', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fitpass_transaction_history'


class Coupon(models.Model):
    coupon_id = models.BigAutoField(primary_key=True)
    coupon_title = models.CharField(max_length=245, blank=True, null=True)
    coupon_code = models.CharField(max_length=245, blank=True, null=True)
    discount_price = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    activation_days = models.IntegerField(blank=True, null=True)
    max_coupon_use = models.IntegerField(blank=True, null=True)
    coupon_message = models.TextField(blank=True, null=True)
    is_active = models.CharField(max_length=3, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=145, blank=True, null=True)
    updated_by = models.CharField(max_length=145, blank=True, null=True)
    coupon_category_id = models.CharField(max_length=45, blank=True, null=True)
    is_redeem = models.CharField(max_length=3, blank=True, null=True)
    coupon_channel = models.CharField(max_length=7, blank=True, null=True)
    customer_category = models.TextField(blank=True, null=True)
    customer_subcategory = models.TextField(blank=True, null=True)
    min_workouts = models.IntegerField(blank=True, null=True)
    coupon_type = models.CharField(max_length=245, blank=True, null=True)
    team_zone_name = models.CharField(max_length=245, blank=True, null=True)
    min_order_amount = models.FloatField(blank=True, null=True)
    coupon_description = models.TextField(blank=True, null=True)
    fitpass_discount = models.FloatField(blank=True, null=True)
    franchise_discount = models.FloatField(blank=True, null=True)
    membership_type = models.CharField(max_length=245, blank=True, null=True)
    user_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fitpass_coupon'

class CorporateCoupons(models.Model):
    corporate_coupons_id = models.BigAutoField(primary_key=True)
    coupon_code = models.CharField(max_length=245, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_active = models.CharField(max_length=3, blank=True, null=True)
    corporate_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=145, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=145, blank=True, null=True)
    coupon_id = models.IntegerField(blank=True, null=True)
    max_use = models.IntegerField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    membership_plan_id = models.IntegerField(blank=True, null=True)
    min_order_amount = models.FloatField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    mem_validaty_as_coupon_end_date = models.CharField(max_length=3, blank=True, null=True)
    coupon_shared_city = models.TextField(blank=True, null=True)
    membership_validity = models.IntegerField(blank=True, null=True)
    membership_validity_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fitpass_corporate_coupons'


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


class TaskManagementLogs(models.Model):
    task_management_log_id = models.BigAutoField(primary_key=True)
    updated_by = models.CharField(max_length=145, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    task_management_id = models.BigIntegerField(blank=True, null=True)
    last_changes = models.TextField(blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'fitpass_task_management_logs'

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


class TeamNotificationReceivers(models.Model):
    notification_receiver_id = models.BigAutoField(primary_key=True)
    notification = models.ForeignKey('TeamNotifications', models.DO_NOTHING)
    team_member_id = models.BigIntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fitpass_team_notification_receivers'