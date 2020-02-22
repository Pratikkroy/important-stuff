class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=45, blank=True, null=True)
    parent_role = models.ForeignKey('Roles', models.DO_NOTHING, blank=True, null=True)
    class Meta:
        managed = False
        db_table =  'fitpass_roles'


