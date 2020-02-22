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


