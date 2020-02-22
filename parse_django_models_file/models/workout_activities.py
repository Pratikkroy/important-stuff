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

