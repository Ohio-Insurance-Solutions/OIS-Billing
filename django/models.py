import datetime

from django.db import models
from django.utils import timezone


class Location(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    county = models.CharField(max_length=100)
    year_built = models.PositiveSmallIntegerField()
    square_footage = models.PositiveSmallIntegerField()
    construction_type = models.ForeignKey(
        'Construction_Type', on_delete=models.PROTECT)
    location_type = models.ForeignKey(
        'Location_Type', on_delete=models.PROTECT)
    num_units = models.ForeignKey(
        'Num_Units', on_delete=models.PROTECT)
    occupancy = models.ForeignKey(
        'Occupancy', on_delete=models.PROTECT)
    roof_update = models.PositiveSmallIntegerField()
    wiring_update = models.PositiveSmallIntegerField()
    hvac_update = models.PositiveSmallIntegerField()
    plumbing_update = models.PositiveSmallIntegerField()
    garage = models.BooleanField()
    section_8 = models.BooleanField()
    msb_value = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField()
    def __str__(self):
        return self.street_address


class Construction_Type(models.Model):
    construction_type = models.CharField(max_length=20)
    def __str__(self):
        return self.construction_type


class Occupancy(models.Model):
    occupancy = models.CharField(max_length=20)
    def __str__(self):
        return self.occupancy


class Location_Type(models.Model):
    location_type = models.CharField(max_length=20)
    def __str__(self):
        return self.location_type


class Num_Units(models.Model):
    num_units = models.CharField(max_length=20)
    def __str__(self):
        return self.num_units


class Agent(models.Model):
    name = models.CharField(max_length=50)
    agency = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class MTG(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    notes = models.CharField(max_length=200)
    loan_num = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Additional_Insured(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    notes = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Payor(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    notes = models.CharField(max_length=200)
    frequiency = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.name


class Payments(models.Model):
    policy_data = models.ForeignKey(
        'Policy_Data', on_delete=models.PROTECT)
    pay_date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payor = models.ForeignKey(
        'Payor', on_delete=models.PROTECT)
    source = models.CharField(max_length=100)
    notes = models.CharField(max_length=200)
    def __str__(self):
        return self.pay_date


class Policy_Data(models.Model):
    named_insured = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    entity_type = models.ForeignKey(
        'Entity_Type', on_delete=models.PROTECT)
    agent = models.ForeignKey(
        'Agent', on_delete=models.PROTECT)
    ois_fee = models.DecimalField(max_digits=5, decimal_places=2)
    deductible = models.PositiveSmallIntegerField()
    gl_limit = models.ForeignKey(
        'GL_Limit', on_delete=models.PROTECT)
    sales_tax_override = models.DecimalField(max_digits=3, decimal_places=2)
    annual_fee_override = models.DecimalField(max_digits=8, decimal_places=2)
    reporting_type = models.ForeignKey(
        'Reporting_Type', on_delete=models.PROTECT)
    billing_type = models.ForeignKey(
        'Billing_Type', on_delete=models.PROTECT)
    def __str__(self):
        return self.named_insured


class iSOV_Type(models.Model):
    isov_type = models.CharField(max_length=50)
    def __str__(self):
        return self.isov_type


class Entity_Type(models.Model):
    entity_type = models.CharField(max_length=50)
    def __str__(self):
        return self.entity_type

class GL_Limit(models.Model):
    gl_long = models.CharField(max_length=100)
    gl_short = models.CharField(max_length=50)
    def __str__(self):
        return self.gl_short


class Reporting_Type(models.Model):
    reporting_type = models.CharField(max_length=10)
    def __str__(self):
        return self.reporting_type


class Billing_Type(models.Model):
    billing_type = models.CharField(max_length=10)
    def __str__(self):
        return self.billing_type


class Cause_of_Loss_Form(models.Model):
    cause_of_loss = models.CharField(max_length=100)
    def __str__(self):
        return self.cause_of_loss


class Deductible(models.Model):
    deductible = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.deductible


class WH_Deductible(models.Model):
    wh_deductible = models.CharField(max_length=10)
    def __str__(self):
        return self.wh_deductible


class WH_Stop_Loss(models.Model):
    wh_stop_loss = models.CharField(max_length=10)
    def __str__(self):
        return self.wh_stop_loss


class Settlement_Coinsurance(models.Model):
    settlement_coinsurance = models.CharField(max_length=50)
    settlement = models.CharField(max_length=20)
    coinsurance = models.CharField(max_length=20)
    def __str__(self):
        return self.settlement_coinsurance


class iSOV_Totals(models.Model):
    policy_data = models.ForeignKey(
        'Policy_Data', on_delete=models.PROTECT)
    isov_type = models.ForeignKey(
        'iSOV_Type', on_delete=models.PROTECT)
    named_insured = models.CharField(max_length=200)
    mailing_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    entity_type = models.ForeignKey(
        'Entity_Type', on_delete=models.PROTECT)
    gl_limit = models.ForeignKey(
        'GL_Limit', on_delete=models.PROTECT)
    paper_company = models.CharField(max_length=100)
    reporting_type = models.ForeignKey(
        'Reporting_Type', on_delete=models.PROTECT)
    policy_number = models.CharField(max_length=50)
    effective_date = models.DateField()
    expiration_date = models.DateField()
    average_prop_rate = models.DecimalField(max_digits=11, decimal_places=10)
    average_gl_rate = models.PositiveSmallIntegerField()
    deductible = models.ForeignKey(
        'Deductible', on_delete=models.PROTECT)
    wh_deductible = models.ForeignKey(
        'WH_Deductible', on_delete=models.PROTECT)
    wh_stop_loss = models.ForeignKey(
        'WH_Stop_Loss', on_delete=models.PROTECT)
    property_premium = models.DecimalField(max_digits=8, decimal_places=2)
    liability_premium = models.DecimalField(max_digits=8, decimal_places=2)
    ord_law_premium = models.DecimalField(max_digits=8, decimal_places=2)
    mine_subsidence_premium = models.DecimalField(max_digits=8, decimal_places=2)
    earthquake_premium = models.DecimalField(max_digits=8, decimal_places=2)
    total_premium = models.DecimalField(max_digits=8, decimal_places=2)
    inspection_fee = models.DecimalField(max_digits=8, decimal_places=2)
    surplus_lines_tax = models.DecimalField(max_digits=8, decimal_places=2)
    broker_fee = models.DecimalField(max_digits=8, decimal_places=2)
    total_due = models.DecimalField(max_digits=8, decimal_places=2)
    tiv = models.DecimalField(max_digits=11, decimal_places=2)
    file_location = models.CharField(max_length=200)
    date_extracted = models.DateTimeField()
    calculated_sales_tax = models.DecimalField(max_digits=4, decimal_places=3)
    calculated_broker_fee = models.DecimalField(max_digits=4, decimal_places=3)
    def __str__(self):
        return self.isov_type


class iSOV_Locations(models.Model):
    isov_totals = models.ForeignKey(
        'iSOV_Totals', on_delete=models.PROTECT)
    num = models.PositiveSmallIntegerField()
    street_address = models.CharField(max_length=200)
    settlement_coinsurance = models.ForeignKey(
        'Settlement_Coinsurance', on_delete=models.PROTECT)
    pc = models.PositiveSmallIntegerField()
    inspection = models.BooleanField()
    prop_rate = models.DecimalField(max_digits=6, decimal_places=5)
    gl_rate = models.PositiveSmallIntegerField()
    ai_charge = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.street_address


class Locations_Issued(models.Model):
    policy_data = models.ForeignKey(
        'Policy_Data', on_delete=models.PROTECT)
    location = models.ForeignKey(
        'Location', on_delete=models.PROTECT)
    num = models.PositiveSmallIntegerField()
    bldg = models.PositiveIntegerField()
    os = models.PositiveIntegerField()
    bpp = models.PositiveIntegerField()
    bi = models.PositiveIntegerField()
    add_date = models.DateField()
    remove_date = models.DateField()
    prior_premium = models.DecimalField(max_digits=8, decimal_places=2)
    premium_override = models.DecimalField(max_digits=8, decimal_places=2)
    mtg = models.ForeignKey(
        'MTG', on_delete=models.PROTECT)
    additional_insured = models.ForeignKey(
        'Additional_Insured', on_delete=models.PROTECT)
    payor = models.ForeignKey(
        'Payor', on_delete=models.PROTECT)
    def __str__(self):
        return self.location


class Locations_Quoted(models.Model):
    policy_data = models.ForeignKey(
        'Policy_Data', on_delete=models.PROTECT)
    location = models.ForeignKey(
        'Location', on_delete=models.PROTECT)
    bldg = models.PositiveIntegerField()
    os = models.PositiveIntegerField()
    bpp = models.PositiveIntegerField()
    bi = models.PositiveIntegerField()
    add_date = models.DateField()
    prior_premium = models.DecimalField(max_digits=8, decimal_places=2)
    premium_override = models.DecimalField(max_digits=8, decimal_places=2)
    mtg = models.ForeignKey(
        'MTG', on_delete=models.PROTECT)
    additional_insured = models.ForeignKey(
        'Additional_Insured', on_delete=models.PROTECT)
    payor = models.ForeignKey(
        'Payor', on_delete=models.PROTECT)
    def __str__(self):
        return self.location
