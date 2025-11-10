SCHEMA_TEXT = """
DATABASE: Employee Self-Service (ESS) System

================================================================================
TABLE: ESS_EMPLOYEE_TIMEENTRIES
================================================================================
DESCRIPTION: Stores employee time entries including check-in/check-out records, 
shift information, and calculated work duration metrics.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- EMP_ID (bigint) - Employee ID (Foreign Key)
- CHECK_IN (datetime) - System recorded check-in time
- CHECK_OUT (datetime) - System recorded check-out time
- USER_CHECK_IN (datetime) - User corrected check-in time
- USER_CHECK_OUT (datetime) - User corrected check-out time
- SHIFT_DATE (smalldatetime) - Date of the shift
- STATUS (tinyint) - Status code (0-5)
- REASON (varchar) - Reason for discrepancies
- REMARKS (varchar) - Additional remarks
- CREATED_BY (bigint) - User who created record
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - User who modified record
- MODIFIED_ON (smalldatetime) - Modification timestamp
- REC_VERSION (tinyint) - Record version
- DAYMARK (varchar) - Day marking/classification
- PAID_FRACTION (float) - Fraction of paid day
- DAY_FRACTION (float) - Fraction of day worked
- IS_MANUAL (bit) - Flag if entry is manually created
- SHIFT_ID (int) - Associated shift ID (Foreign Key)
- NORMAL_MIN (int) - Normal working minutes
- OT_MIN (int) - Overtime minutes
- LATE_IN_MIN (int) - Late check-in minutes
- EARLY_OUT_MIN (int) - Early check-out minutes
- SHORT_MIN (int) - Shortage minutes
- IN_LOC (varchar) - Check-in location
- OUT_LOC (varchar) - Check-out location
- ISLOCKED (bit) - Record locked flag (Default: 0)
- OT_STATUS (tinyint) - Overtime approval status
- APPROVE_OT_MINS (float) - Approved overtime minutes
- PERMISSION_MIN (int) - Permission minutes taken
- IS_VALID (bit) - Validity flag

CONSTRAINTS:
- Primary Key: ID (Clustered)
- Unique Constraint: TEN_ID, EMP_ID, SHIFT_DATE, DAYMARK (Non-clustered)
- Foreign Key: SHIFT_ID → ESS_SHIFT.SHIFT_ID
- Foreign Key: EMP_ID → ESS_EMPLOYEE.ID

================================================================================
TABLE: ESS_LEAVE_REQ_DETAILS
================================================================================
DESCRIPTION: Stores detailed information about leave requests including 
specific leave dates and leave account mappings.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- LEAVE_REQ_ID (bigint) - Associated leave request ID
- LEAVE_DATE (smalldatetime) - Specific date of leave
- LEAVES (float) - Number of leaves taken
- LEV_ACC_ID (bigint) - Leave account ID

CONSTRAINTS:
- Primary Key: ID (Clustered)

================================================================================
TABLE: ESS_CUSTOM_ATTRIBUTE
================================================================================
DESCRIPTION: Stores custom attributes for various entities with temporal 
versioning support for audit tracking.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- DEF_ID (bigint) - Attribute definition ID
- ENTITY_ID (bigint) - Entity reference ID
- ATT_VALUE (varchar) - Attribute value
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- VERSION (tinyint) - Version number
- StartTime (datetime2) - System temporal start time (System-generated, Hidden)
- EndTime (datetime2) - System temporal end time (System-generated, Hidden)

CONSTRAINTS:
- Primary Key: ID (Clustered)
- System Versioning: Enabled with history table ESS_CUSTOM_ATTRIBUTE_History

================================================================================
TABLE: ESS_EMPLOYEE_SHIFT
================================================================================
DESCRIPTION: Manages employee shift assignments with temporal versioning for 
tracking shift history and changes.

COLUMNS:
- TEN_ID (int) - Tenant ID (Primary Key Component)
- EMP_ID (int) - Employee ID (Primary Key Component)
- SHIFT_ID (int) - Shift ID
- START_DT (datetime) - Shift start date (Primary Key Component)
- END_DT (datetime) - Shift end date
- REC_VERSION (tinyint) - Record version
- StartTime (datetime2) - System temporal start time (System-generated, Hidden)
- EndTime (datetime2) - System temporal end time (System-generated, Hidden)

CONSTRAINTS:
- Primary Key: TEN_ID, EMP_ID, START_DT (Clustered)
- System Versioning: Enabled with history table ESS_EMPLOYEE_SHIFT_HISTORY

================================================================================
TABLE: ESS_EMPLOYEE
================================================================================
DESCRIPTION: Core employee master record containing demographic, employment, 
and organizational information with temporal versioning.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- CODE (varchar) - Employee code/number
- BADGE_ID (varchar) - Badge identification
- TITLE (varchar) - Title/prefix
- NAME (varchar) - Employee name
- EMP_IMG (image) - Employee photograph
- ORGANIZATION (bigint) - Organization ID (Foreign Key)
- DEPARTMENT (bigint) - Department ID (Foreign Key)
- DESIGNATION (bigint) - Designation ID (Foreign Key)
- LOCATION (bigint) - Location ID (Foreign Key)
- EMP_CATEGORY (bigint) - Employee category
- EMP_GROUP (bigint) - Employee group
- EMP_SUBGROUP (bigint) - Employee subgroup
- OFFMAIL (varchar) - Official email
- OFFPHONE (varchar) - Official phone
- PHONEEXT (varchar) - Phone extension
- SEAT (varchar) - Seat/desk number
- DOJ (smalldatetime) - Date of joining
- PROBATION_END (smalldatetime) - Probation end date
- DOL (smalldatetime) - Date of leaving
- LAST_REW (smalldatetime) - Last review date
- DOB (smalldatetime) - Date of birth
- FATHERS_NAME (varchar) - Father's name
- MARITAL_STATUS (int) - Marital status code
- SEX (int) - Gender code
- REPORT_TO (bigint) - Reporting manager ID
- ACTIVE (tinyint) - Active status
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- VERSION (tinyint) - Record version
- IS_DELETED (bit) - Soft delete flag (Default: 0)
- StartTime (datetime2) - System temporal start time (System-generated, Hidden)
- EndTime (datetime2) - System temporal end time (System-generated, Hidden)
- EMP_GRADE (bigint) - Employee grade/level
- DOR (smalldatetime) - Date of resignation (Default: '1900-01-01')
- PERSONAL_EMAIL (nvarchar) - Personal email address
- PERSONAL_PHONE (nvarchar) - Personal phone number
- NATIONALITY (bigint) - Nationality ID
- COUNTRY_OF_RESIDENCE (bigint) - Country of residence ID

CONSTRAINTS:
- Primary Key: ID (Clustered)
- System Versioning: Enabled with history table ESS_EMPLOYEE_History
- Foreign Key: ORGANIZATION → ESS_ORGANIZATION.ORG_ID
- Foreign Key: DEPARTMENT → ESS_DEPARTMENT.DEPT_ID
- Foreign Key: DESIGNATION → ESS_DESIGNATION.DESG_ID
- Foreign Key: LOCATION → ESS_LOCATION.LOC_ID

================================================================================
TABLE: ESS_EMPLOYEE_PAYSTRUCTURE
================================================================================
DESCRIPTION: Maintains employee-specific payroll structure and salary 
component assignments with temporal versioning.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- EMP_ID (bigint) - Employee ID (Foreign Key)
- PSI_ID (bigint) - Payslip item ID (Foreign Key)
- AMOUNT (float) - Salary component amount
- REMARKS (varchar) - Remarks
- EXPRESSION (varchar) - Calculation expression
- VERSION (tinyint) - Version number (Default: 1)
- StartTime (datetime2) - System temporal start time (System-generated, Hidden)
- EndTime (datetime2) - System temporal end time (System-generated, Hidden)

CONSTRAINTS:
- Primary Key: ID (Clustered)
- System Versioning: Enabled with history table ESS_EMPLOYEE_PAYSTRUCTURE_History
- Foreign Key: EMP_ID → ESS_EMPLOYEE.ID
- Foreign Key: PSI_ID → ESS_PAYSLIP_ITEM.ID

================================================================================
TABLE: ESS_EMPLOYEE_STATUTORY
================================================================================
DESCRIPTION: Stores statutory and compliance information for employees 
including PF, ESI, tax, and visa details.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- EMP_ID (bigint) - Employee ID (Foreign Key)
- PAN_NO (varchar) - PAN number
- PASSPORT_NO (varchar) - Passport number
- BANK_ACC_NO (varchar) - Bank account number
- BANK_NAME (varchar) - Bank name
- BRANCH (varchar) - Bank branch
- IFSC_CODE (varchar) - IFSC code
- PF_NO (varchar) - PF number
- PF_EPF_SAL_LIMIT (float) - PF salary limit
- PF_EPF_PERCENT (float) - PF percentage
- PF_EPF_HIGH_CONT (float) - PF high contribution
- PF_PAST_SERVICE_DAYS (float) - Past service days for PF
- PF_CONT_WORKER (bit) - Continuous worker flag
- PF_INTLN_WORKER (bit) - International worker flag
- PF_DIFFERENTLY_ABLED (bit) - Differently abled flag
- PF_DOJ_EPF (smalldatetime) - PF DOJ for EPF
- PF_DOL_EPF (smalldatetime) - PF DOL for EPF
- PF_REASON_LEAVING (varchar) - Reason for leaving PF
- PF_EPS_SAL_LIMIT (float) - EPS salary limit
- PF_EPS_PERCENT (float) - EPS percentage
- PF_EPS_HIGH_CONT (float) - EPS high contribution
- PF_DOJ_EPS (smalldatetime) - DOJ for EPS
- PF_DOL_EPS (smalldatetime) - DOL for EPS
- PF_DOJ_EDLI (smalldatetime) - DOJ for EDLI
- PF_DOL_EDLI (smalldatetime) - DOL for EDLI
- ESI_NO (varchar) - ESI number
- ESI_DOJ (smalldatetime) - ESI date of joining
- ESI_DOL (smalldatetime) - ESI date of leaving
- ESI_REASON_LEAVING (varchar) - ESI reason for leaving
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (datetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (datetime) - Modification timestamp
- VERSION (tinyint) - Record version
- PF_UANNO (varchar) - PF UAN number
- PF_DOCTYPE (varchar) - PF document type
- PF_DOCNO (varchar) - PF document number
- PF_DOCEXP (datetime) - PF document expiry
- PF_EDULEVEL (varchar) - Education level
- PF_DIFABLECAT (varchar) - Disability category
- AADHAR_NO (varchar) - Aadhar number
- StartTime (datetime2) - System temporal start time (System-generated, Hidden)
- EndTime (datetime2) - System temporal end time (System-generated, Hidden)
- FAMILY_DETAILS (nvarchar) - Family details JSON
- NATIONAL_ID (nvarchar) - National ID
- NATIONAL_ID_EXPIRY (datetime) - National ID expiry date
- PASSPORT_EXPIRY (datetime) - Passport expiry date
- VISA_TYPE (tinyint) - Visa type code
- VISA_EXPIRY (datetime) - Visa expiry date
- ADDITIONAL_DETAILS (nvarchar) - Additional details JSON
- RESIDENCY_STATUS (tinyint) - Residency status
- ADDRESS_TYPE (tinyint) - Address type code

CONSTRAINTS:
- Primary Key: ID (Clustered)
- System Versioning: Enabled with history table ESS_EMPLOYEE_STATUTORY_History
- Foreign Key: EMP_ID → ESS_EMPLOYEE.ID

================================================================================
TABLE: ESS_TENANT
================================================================================
DESCRIPTION: Represents organizations/companies using the ESS system with 
subscription and configuration information.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- CODE (varchar) - Tenant code
- NAME (varchar) - Tenant/company name
- SUBSCIRPTION_END_DATE (datetime) - Subscription end date
- SUBSCRIPTION_TYPE (int) - Type of subscription
- ACTIVE (bit) - Active status
- DATASOURCE_ID (varchar) - Data source identifier
- CONTACT_NAME (varchar) - Contact person name
- CONTACT_EMAIL (varchar) - Contact email
- COMPANY_REGI_NO (varchar) - Company registration number
- PF_ESTT_CODE (varchar) - PF establishment code
- PF_GROUP_CODE (varchar) - PF group code
- ESI_NO (varchar) - ESI number
- TAN_NO (varchar) - TAN number
- PAN_NO (varchar) - PAN number
- IT_WARD (varchar) - IT ward
- IT_CIRCLE (varchar) - IT circle
- AUTO_CODE_FORMAT (varchar) - Auto-generation code format
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (datetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (datetime) - Modification timestamp
- VERSION (tinyint) - Record version
- LEAD_SOURCE (varchar) - Lead source
- SUBSCRIPTION_INFO (varchar) - Subscription information
- COUNTRY_ID (bigint) - Country ID (Default: 0)

CONSTRAINTS:
- Primary Key: ID (Clustered)

================================================================================
TABLE: ESS_LEAVE
================================================================================
DESCRIPTION: Defines leave types/categories available in the system.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- CODE (varchar) - Leave type code
- NAME (varchar) - Leave type name
- REMARKS (varchar) - Remarks
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (datetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (datetime) - Modification timestamp
- VERSION (tinyint) - Record version

CONSTRAINTS:
- Primary Key: ID (Clustered)

================================================================================
TABLE: ESS_LEAVE_REQUISITION
================================================================================
DESCRIPTION: Stores employee leave requests/applications for approval workflow.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- REQ_TYPE (int) - Request type code
- REQ_DATE (datetime) - Request submission date
- EMP_ID (bigint) - Employee ID (Foreign Key)
- LEAVE_ID (bigint) - Leave type ID (Foreign Key)
- LEV_REQ_FROM (datetime) - Leave start date
- LEV_REQ_TO (datetime) - Leave end date
- REQ_LEAVES (float) - Number of leaves requested
- CON_ADDR (varchar) - Contact address during leave
- STATUS (tinyint) - Request status (Pending/Approved/Rejected)
- REASONS (varchar) - Reason for leave
- SETOFFBALANCE (float) - Set-off balance
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (datetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (datetime) - Modification timestamp
- VERSION (tinyint) - Record version
- IS_SD_HF (bit) - Is start date half-day flag
- IS_ED_HF (bit) - Is end date half-day flag
- RELIEVER (bigint) - Reliever/covering manager ID
- SUPPORTING_DOCUMENT (varchar) - Supporting document reference

CONSTRAINTS:
- Primary Key: ID (Clustered)
- Foreign Key: EMP_ID → ESS_EMPLOYEE.ID
- Foreign Key: LEAVE_ID → ESS_LEAVE.ID

================================================================================
TABLE: ESS_USERS
================================================================================
DESCRIPTION: User accounts for ESS system access with authentication and 
preference information.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- USER_NAME (varchar) - Login username
- PASSWORD (varchar) - Encrypted password
- DISPLAY_NAME (varchar) - Display name
- REMARKS (varchar) - Remarks
- EMP_CODE (varchar) - Associated employee code
- USER_SECRET_QUESTION (varchar) - Security question
- USER_SECRET_ANSWER (varchar) - Security answer
- REG_GUID (varchar) - Registration GUID
- ACTIVE (tinyint) - Active status
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (datetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (datetime) - Modification timestamp
- VERSION (tinyint) - Record version
- PORTLET_ORDER (varchar) - Dashboard portlet arrangement
- LAST_LOGIN (datetime) - Last login timestamp
- FAVOURITES (varchar) - User favorites/bookmarks
- ALIAS (nvarchar) - User alias

CONSTRAINTS:
- Primary Key: ID (Clustered)

================================================================================
TABLE: ESS_REIMBURSEMENT
================================================================================
DESCRIPTION: Tracks employee expense reimbursement requests and approvals.

COLUMNS:
- ID (bigint) (Primary Key Component) - Auto-increment identifier
- TEN_ID (bigint) (Primary Key Component) - Tenant ID
- EMP_ID (bigint) - Employee ID (Foreign Key)
- REIM_TYPE_ID (bigint) - Reimbursement type ID (Foreign Key)
- STATUS (tinyint) - Request status
- AMOUNT (float) - Claimed amount
- REMARKS (varchar) - Remarks
- APPROVED_AMOUNT (float) - Approved amount
- CUSTOM_ATTR_VALUE (varchar) - Custom attribute value
- REIM_ATTACH (varchar) - Attachment reference
- EXPENSE_DATE (datetime) - Expense date
- PAYMENT_TYPE (varchar) - Payment method type
- PAYMENT_ID (varchar) - Payment ID/reference
- PAYMENT_DATE (datetime) - Payment date
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (datetime) - Creation timestamp (Required)
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (datetime) - Modification timestamp
- VERSION (tinyint) - Record version

CONSTRAINTS:
- Primary Key: ID, TEN_ID (Clustered)
- Foreign Key: EMP_ID → ESS_EMPLOYEE.ID
- Foreign Key: REIM_TYPE_ID → ESS_REIMBURSEMENT_TYPE.ID

================================================================================
TABLE: ESS_REIMBURSEMENT_TYPE
================================================================================
DESCRIPTION: Defines reimbursement categories and policies.

COLUMNS:
- ID (bigint) (Primary Key Component) - Auto-increment identifier
- TEN_ID (bigint) (Primary Key Component) - Tenant ID
- CODE (varchar) - Reimbursement type code
- NAME (varchar) - Reimbursement type name
- REMARKS (varchar) - Remarks
- RECEIPT_REQ_AMT (float) - Receipt required above amount
- REIM_BEFORE (varchar) - Reimbursement before period
- CUSTOM_ATTRIBUTE (varchar) - Custom attribute definition
- ALLOW_LIMIT (int) - Allow limit count
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- REC_VERSION (tinyint) - Record version
- PAYSLIP_ITEM_ID (bigint) - Associated payslip item
- YEARLY_LIMIT (float) - Yearly limit
- MONTHLY_LIMIT (float) - Monthly limit

CONSTRAINTS:
- Primary Key: ID, TEN_ID (Clustered)

================================================================================
TABLE: ESS_PAYSLIP
================================================================================
DESCRIPTION: Stores employee payslips with salary calculations and payment details.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- EMP_ID (bigint) - Employee ID (Foreign Key)
- PAY_PERIOD (varchar) - Pay period identifier (e.g., 'Apr-2023', 'Sep-2025')
- STAT_YEAR (int) - Statistical year
- TOT_EARNINGS (float) - Total earnings
- TOT_DEDUCTS (float) - Total deductions
- NET_SALARY (float) - Net salary paid
- BANK_ACC_NO (varchar) - Bank account number
- BANK_NAME (varchar) - Bank name
- ISLOCKED (bit) - Locked status
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- REC_VERSION (tinyint) - Record version
- PAID_DAYS (float) - Number of paid days (Default: 0)
- CTC (float) - Cost to company
- TOT_EMPR_CONT (float) - Total employer contribution
- GROSS_SAL (float) - Gross salary
- F1-F5 (float) - Formula fields
- STATUS (tinyint) - Payslip status (Default: 0)
- TRANSACTION_ID (varchar) - Transaction reference
- TRANSACTION_DATE (varchar) - Transaction date
- TRANSACTION_REMARKS (varchar) - Transaction remarks

CONSTRAINTS:
- Primary Key: ID (Clustered)

================================================================================
TABLE: ESS_NPS
================================================================================
DESCRIPTION: Records Net Promoter Score feedback from employees.

COLUMNS:
- ID (bigint) (Primary Key Component) - Auto-increment identifier
- TEN_ID (bigint) (Primary Key Component) - Tenant ID
- USER_ID (bigint) - User ID (Foreign Key)
- START_DATE (datetime) - Survey start date
- END_DATE (datetime) - Survey end date
- REMARKS (nvarchar) - Remarks/comments
- NEXT_NPS (datetime) - Next NPS survey date
- TYPE (nvarchar) - NPS type
- SCORE (int) - NPS score (0-10)
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (datetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (datetime) - Modification timestamp
- Version (tinyint) - Record version

CONSTRAINTS:
- Primary Key: ID, TEN_ID (Clustered)

================================================================================
TABLE: ESS_ORGANIZATION
================================================================================
DESCRIPTION: Stores organizational structure information.

COLUMNS:
- ORG_ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- ORG_CODE (varchar) - Organization code
- ORG_NAME (varchar) - Organization name
- ORG_REMARKS (varchar) - Remarks
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- REC_VERSION (tinyint) - Record version
- ORG_IMG (image) - Organization image/logo
- ORG_LOGO (varchar) - Logo file path

CONSTRAINTS:
- Primary Key: ORG_ID (Clustered)

================================================================================
TABLE: ESS_DEPARTMENT
================================================================================
DESCRIPTION: Defines organizational departments.

COLUMNS:
- DEPT_ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- DEPT_CODE (varchar) - Department code
- DEPT_NAME (varchar) - Department name
- DEPT_REMARKS (varchar) - Remarks
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- REC_VERSION (tinyint) - Record version

CONSTRAINTS:
- Primary Key: DEPT_ID (Clustered)

================================================================================
TABLE: ESS_DESIGNATION
================================================================================
DESCRIPTION: Stores job titles and designations.

COLUMNS:
- DESG_ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- DESG_CODE (varchar) - Designation code
- DESG_NAME (varchar) - Designation name
- DESG_REMARKS (varchar) - Remarks
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- REC_VERSION (tinyint) - Record version

CONSTRAINTS:
- Primary Key: DESG_ID (Clustered)

================================================================================
TABLE: ESS_LOCATION
================================================================================
DESCRIPTION: Stores office and work location information.

COLUMNS:
- LOC_ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- LOC_CODE (varchar) - Location code
- LOC_NAME (varchar) - Location name
- ADDRESS1 (varchar) - Address line 1
- ADDRESS2 (varchar) - Address line 2
- CITY (varchar) - City
- STATE (varchar) - State/Province
- COUNTRY (varchar) - Country
- PINCODE (varchar) - Postal/ZIP code
- PHONE1 (varchar) - Primary phone
- PHONE2 (varchar) - Secondary phone
- FAX (varchar) - Fax number
- WEBSITE (varchar) - Website URL
- LOC_REMARKS (varchar) - Remarks
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- REC_VERSION (tinyint) - Record version
- TIMEZONE (varchar) - Timezone (Default: '+5.5')

CONSTRAINTS:
- Primary Key: LOC_ID (Clustered)

================================================================================
TABLE: ESS_SHIFT
================================================================================
DESCRIPTION: Defines shift schedules and working hours.

COLUMNS:
- SHIFT_ID (int) (Primary Key) - Auto-increment identifier
- TEN_ID (int) - Tenant ID
- SHIFT_CODE (varchar) - Shift code
- SHIFT_NAME (varchar) - Shift name
- SHIFT_START (datetime) - Shift start time
- SHIFT_END (datetime) - Shift end time
- GRACE_LATEIN (int) - Grace period for late check-in (minutes)
- GRACE_EARLYOUT (int) - Grace period for early check-out (minutes)
- EARLY_START (int) - Early start allowed (minutes)
- LATE_END (int) - Late end allowed (minutes)
- MIN_FOR_OT (int) - Minimum minutes for overtime
- MIN_FULL_PRESENT (int) - Minimum minutes for full day presence
- MIN_HALF_PRESENT (int) - Minimum minutes for half day presence
- HRS_WRK_RND (int) - Hours worked rounding
- LATE_RANGE_ID (int) - Late deduction range ID
- REMARKS (varchar) - Remarks
- CREATED_BY (int) - Creator user ID
- CREATED_ON (datetime) - Creation timestamp
- MODIFIED_BY (int) - Modifier user ID
- MODIFIED_ON (datetime) - Modification timestamp
- ACTIVE (bit) - Active status

CONSTRAINTS:
- Primary Key: SHIFT_ID (Clustered)

================================================================================
TABLE: ESS_PAYSLIP_ITEM
================================================================================
DESCRIPTION: Defines payroll line items (earnings/deductions).

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- CODE (varchar) - Item code
- NAME (varchar) - Item name
- ITEMTYPE (varchar) - Type (Earning/Deduction)
- EXPRESSION (varchar) - Calculation expression
- PSI_CATEGORY (bigint) - Category ID
- IS_SYSTEM_VARIABLE (bit) - System variable flag
- CR_ACCOUNT (varchar) - Credit account code
- DR_ACCOUNT (varchar) - Debit account code
- DISPLAY_INDEX (tinyint) - Display order (Default: 0)
- EXECUTION_ORDER (tinyint) - Calculation order (Default: 0)
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- REC_VERSION (tinyint) - Record version

CONSTRAINTS:
- Primary Key: ID (Clustered)

================================================================================
TABLE: ESS_LEAVE_STRUCTURE
================================================================================
DESCRIPTION: Defines leave policy structures for different employee groups.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- CODE (varchar) - Structure code
- NAME (varchar) - Structure name
- REMARKS (varchar) - Remarks
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (datetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (datetime) - Modification timestamp
- VERSION (tinyint) - Record version

CONSTRAINTS:
- Primary Key: ID (Clustered)

================================================================================
TABLE: ESS_LEAVE_STRUCTURE_ITEM
================================================================================
DESCRIPTION: Defines leave types within a leave structure with accrual rules.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- LEAVE_ID (bigint) - Leave type ID (Foreign Key)
- LEV_STRUCTURE_ID (bigint) - Leave structure ID (Foreign Key)
- LEV_PERIOD_ID (bigint) - Leave period ID
- NOTICE_PERIOD (int) - Notice period days
- LIFE_TIME_ACC_LIMIT (int) - Lifetime accumulation limit
- MIN_LEAVES (int) - Minimum leaves required
- MAX_LEVS_TAKEN_PER_YEAR (int) - Max leaves per year
- YEARLY_ACC_LIMIT (int) - Yearly accumulation limit
- LEV_BAL_TO_CARRY_FRWD (float) - Leave balance carry forward
- CONSIDER_HOLIDAY (bit) - Consider holidays in calculation
- CONSIDER_WEEKOFF (bit) - Consider weekoffs in calculation
- PAID_FRACTION (float) - Paid fraction for partial days
- MAX_LEAVES_PER_REQU (float) - Max leaves per request
- MIN_LEAVES_PER_REQU (float) - Min leaves per request
- PARTIAL_DAY_LEAVE (bit) - Allow partial day leave
- APPLIED_ON_OPT_HOL (bit) - Applicable on optional holidays
- IS_LOP (bit) - Is Loss of Pay leave
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (datetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (datetime) - Modification timestamp
- VERSION (tinyint) - Record version
- LEV_EXPIRES_ON (varchar) - Expiry condition
- LEV_TO_ACCUM (float) - Leaves to accumulate per period
- ACCUM_EVERY (varchar) - Accumulation frequency
- ACCUM_ON (varchar) - Accumulation date rule
- IS_PRORATED (bit) - Prorated flag
- CONSIDER_WEEKOFF_HOLIDDAY (bit) - Consider weekoff/holiday (Default: 0)
- NOTICE_PERIOD_THRESHOLD (int) - Notice period threshold (Default: 0)
- LEAVE_THRESHOLD (float) - Leave threshold (Default: 0)
- CONSIDER_WEEKOFFS_HOLIDDAYS (varchar) - Detailed weekoff/holiday rules
- LEV_TO_ENCASH (float) - Leaves eligible for encashment
- CONSIDER_FOR_ENCASHMENT (bit) - Eligible for encashment (Default: 1)
- ACC_BASED_ON_DAYS_PRESENT (float) - Accumulation based on days present (Default: 0)
- LEAVE_ACC_FROM (tinyint) - Leave accumulation from (Default: 0)
- SERVICE_DURATION_DAYS (float) - Service duration in days (Default: 0)
- ATTACHMENT_REQUIRED (tinyint) - Attachment required (Default: 0)
- CAN_EDIT_VACATION (tinyint) - Can edit vacation flag (Default: 0)
- DOC_REQUIRED_LEAVE_DAYS (float) - Document required for leave days (Default: 0)
- ACC_BEFORE_DAYS (int) - Accumulate before days

CONSTRAINTS:
- Primary Key: ID (Clustered)
- Foreign Key: LEAVE_ID → ESS_LEAVE.ID
- Foreign Key: LEV_STRUCTURE_ID → ESS_LEAVE_STRUCTURE.ID

================================================================================
TABLE: ESS_TAX_DECLARATION
================================================================================
DESCRIPTION: Stores employee tax declarations and exemption details for 
income tax computation.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- EMP_ID (bigint) - Employee ID (Foreign Key)
- FIN_YEAR (int) - Financial year
- RENT_PAYABLE_FOR_YEAR (float) - Rent paid in FY
- RENT_PAYABLE_FOR_YEAR_PROOF (float) - Rent proof amount
- SEC80D_MED_INSURANCE (float) - Section 80D medical insurance
- SEC80D_MED_INSURANCE_PROOF (float) - Proof amount
- SEC80DD_MAIN_INC_MED (float) - Section 80DD maintenance of dependents
- SEC80DD_MAIN_INC_MED_PROOF (float) - Proof amount
- SEC80DDB_DED_MED_TRT (float) - Section 80DDB medical treatment
- SEC80DDB_DED_MED_TRT_PROOF (float) - Proof amount
- SEC80E_INT_EDU_LOAN (float) - Section 80E education loan interest
- SEC80E_INT_EDU_LOAN_PROOF (float) - Proof amount
- LIC_PREM (float) - LIC premium
- LIC_PREM_PROOF (float) - Proof amount
- PUB_PF (float) - Public provident fund
- PUB_PF_PROOF (float) - Proof amount
- UNT_LNKED_INS_PLAN (float) - Unit-linked insurance plan
- UNT_LNKED_INS_PLAN_PROOF (float) - Proof amount
- PF_PREV_EMP (float) - PF from previous employer
- PF_PREV_EMP_PROOF (float) - Proof amount
- NSC (float) - National Savings Certificate
- NSC_PROOF (float) - Proof amount
- NSC_ACCURED_INT (float) - NSC accrued interest
- NSC_ACCURED_INT_PROOF (float) - Proof amount
- EMP_PF (float) - Employee PF contribution
- EMP_PF_PROOF (float) - Proof amount
- VOLU_PF (float) - Voluntary PF
- VOLU_PF_PROOF (float) - Proof amount
- INC_PREV_EMPLOYER (float) - Income from previous employer
- INC_PREV_EMPLOYER_PROOF (float) - Proof amount
- TAX_DED_BY_PREV_EMPLOYER (float) - Tax deducted by previous employer
- TAX_DED_BY_PREV_EMPLOYER_PROOF (float) - Proof amount
- INTREST_ON_HOUSING_LOAN (float) - Interest on housing loan
- INTREST_ON_HOUSING_LOAN_PROOF (float) - Proof amount
- VEH_MAINT (float) - Vehicle maintenance
- VEH_MAINT_PROOF (float) - Proof amount
- LTA_EXEM (float) - LTA exemption
- LTA_EXEM_PROOF (float) - Proof amount
- CHLD_EDU_ALLW (float) - Children education allowance
- CHLD_EDU_ALLW_PROOF (float) - Proof amount
- MED_BILL_EXEM (float) - Medical bill exemption
- MED_BILL_EXEM_PROOF (float) - Proof amount
- OTHR_EXEM (float) - Other exemptions
- OTHR_EXEM_PROOF (float) - Proof amount
- MED_INS_FOR_PARNTS (float) - Medical insurance for parents
- MED_INS_FOR_PARNTS_PROOF (float) - Proof amount
- DON_TO_APPR_FUND (float) - Donation to approved fund
- DON_TO_APPR_FUND_PROOF (float) - Proof amount
- RENT_DEDS (float) - Rent deductions
- RENT_DEDS_PROOF (float) - Proof amount
- PENSION_SCHEME (float) - Pension scheme
- PENSION_SCHEME_PROOF (float) - Proof amount
- CHLD_EDUC (float) - Children education
- CHLD_EDUC_PROOF (float) - Proof amount
- HOUSE_LN_PRI_REPY (float) - Housing loan principal repayment
- HOUSE_LN_PRI_REPY_PROOF (float) - Proof amount
- HRA_EXEM (float) - HRA exemption
- HRA_EXEM_PROOF (float) - Proof amount
- TRANSPORT_EXEM (float) - Transport exemption
- TRANSPORT_EXEM_PROOF (float) - Proof amount
- TOT_EXEM_ALLOW (float) - Total exemptions allowed
- TOT_EXEM_ALLOW_PROOF (float) - Proof amount
- ANY_OTHR_DED (float) - Any other deduction
- ANY_OTHR_DED_PROOF (float) - Proof amount
- TOT_DED_6A (float) - Total deductions section 6A
- TOT_DED_6A_PROOF (float) - Proof amount
- TOT_DED_6_SEC80C (float) - Total section 80C deductions
- TOT_DED_6_SEC80C_PROOF (float) - Proof amount
- HOUSE_PROP_INCOM_LOSS (float) - House property loss
- HOUSE_PROP_INCOM_LOSS_PROOF (float) - Proof amount
- INCOM_CHARGE_NORMAL (float) - Income charged at normal rate
- INCOM_CHARGE_NORMAL_PROOF (float) - Proof amount
- INCOM_CHARGE_HIGHER (float) - Income charged at higher rate
- INCOM_CHARGE_HIGHER_PROOF (float) - Proof amount
- TOT_OTHR_INCOME (float) - Total other income
- TOT_OTHR_INCOME_PROOF (float) - Proof amount
- TOT_OTHR_DET_INCOME (float) - Total other detailed income
- TOT_OTHR_DET_INCOME_PROOF (float) - Proof amount
- HOUSE_SELF_OCCUPIED (bit) - Self-occupied house flag
- LIVING_IN_METRO (bit) - Living in metro city flag
- COMPANY_ACCOM (bit) - Company accommodation flag
- HOUSE_LOAN_AFT_APR11999 (bit) - House loan after April 1, 1999 flag
- COMPANY_ACCOM_GT4LC (bit) - Company accommodation > 4 lakhs flag
- SR_CITZN_INSU (bit) - Senior citizen insurance flag
- SR_CITZN_TREAT (bit) - Senior citizen treatment flag
- USING_COMPANY_CAR (bit) - Using company car flag
- COMPANY_CAR_GT1600CC (bit) - Company car > 1600cc flag
- DRIVER_USED (bit) - Driver used flag
- IN_INDIA (bit) - In India flag
- PHYSICAL_DIS (bit) - Physical disability flag
- USING_OWN_CAR (bit) - Using own car flag
- TOT_TAX_LIABILITY (float) - Total tax liability
- SEC80U_DED_PER_DISABLTY (float) - Section 80U disability deduction
- SEC80U_DED_PER_DISABLTY_PROOF (float) - Proof amount
- NPS_EMPER (float) - NPS employer contribution
- EQU_80CCG (float) - Equities 80CCG
- OTH_80C_DED (float) - Other 80C deductions
- INS_80EE (float) - Insurance 80EE
- INS_80TTA (float) - Insurance 80TTA
- OTH80_DED (float) - Other 80 deductions
- NPF (float) - NPF contribution
- LTIB_80CCF (float) - LTIB 80CCF
- POSB_80C (float) - POSB 80C
- POSB_80C_LIM (float) - POSB 80C limit
- LIC_80CCC (float) - LIC 80CCC
- LIC_80CCC_LIM (float) - LIC 80CCC limit
- PEN_80CCD (float) - Pension 80CCD
- PEN_80CCD_LIM (float) - Pension 80CCD limit
- CLAIM_80DD (bit) - Claim 80DD flag
- CLAIM_80DD_IS_SEV (bit) - 80DD is severe disability flag
- CLAIM_80U (bit) - Claim 80U flag
- CLAIM_80U_IS_SEV (bit) - 80U is severe disability flag
- NO_OF_CHILDREN (int) - Number of children
- STATUS (int) - Declaration status (Default: -1)
- DOC_ATTACHMENTS (varchar) - Document attachments
- REMARKS (varchar) - Remarks
- SEC80D_MED_PARENTS (float) - Medical insurance for parents
- IS_PARENTS_SR_CITZN (bit) - Parents are senior citizens flag
- NPS_ADD_EXEMPT (float) - NPS additional exemption
- CREATED_BY (bigint) (Default: 0) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- VERSION (tinyint) (Default: 1) - Record version
- REIMBURSEMENT (float) - Reimbursement amount
- OPTION (tinyint) (Default: 0) - Option selected
- INC_FROM_PREV_EMPLOYER (float) - Income from previous employer
- OWNER_NAME (varchar) - Property owner name
- OWNER_PAN_NO (varchar) - Owner PAN
- SUKANYA_YOJANA (float) - Sukanya Yojana contribution
- SENIOR_CITIZEN_SAVING_SCHEME (float) - Senior citizen savings scheme
- NATIONAL_SAVING_CERT (float) - National savings certificate
- POST_OFFICE_TIME_DEPOSIT (float) - Post office time deposit
- SCH_BANK_FD (float) - Scheduled bank FD
- STAMP_DUTY_REG_CHARGES (float) - Stamp duty and registration charges
- PRV_HEALTH_CHKUP (float) - Preventive health check-up
- INS_80EEA (float) - Insurance 80EEA
- INS_80EEB (float) - Insurance 80EEB
- INS_80GGC (float) - Insurance 80GGC
- INS_80QQB (float) - Insurance 80QQB
- INS_80RRB (float) - Insurance 80RRB
- INS_80TTB (float) - Insurance 80TTB
- SR_CITZN_SPEC_DIS (bit) - Senior citizen with special disability flag

CONSTRAINTS:
- Primary Key: ID (Clustered)
- Foreign Key: EMP_ID → ESS_EMPLOYEE.ID

================================================================================
TABLE: ESS_FORM16
================================================================================
DESCRIPTION: Stores Form 16 (Tax Certificate) details for employee taxation.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- EMP_ID (bigint) - Employee ID (Foreign Key)
- FIN_YEAR (int) - Financial year
- TAX_DEC_ID (bigint) - Tax declaration ID
- [Multiple salary/deduction/exemption columns for Form 16 fields]
- STANDARD_DEDUCTION (float) (Default: 0) - Standard deduction
- TAXABLE_INCM (float) - Taxable income
- MARGINAL_RELIEF (float) - Marginal relief
- VPF (float) - Voluntary PF
- SUKANYA_YOJANA (float) - Sukanya Yojana
- SENIOR_CITIZEN_SAVING_SCHEME (float) - Senior citizen savings
- NATIONAL_SAVING_CERT (float) - National savings certificate
- POST_OFFICE_TIME_DEPOSIT (float) - Post office deposit
- SCH_BANK_FD (float) - Bank FD
- STAMP_DUTY_REG_CHARGES (float) - Stamp duty charges
- PRV_HEALTH_CHKUP (float) - Preventive health checkup
- INS_80EEA (float) - Insurance 80EEA
- INS_80EEB (float) - Insurance 80EEB
- INS_80GGC (float) - Insurance 80GGC
- INS_80QQB (float) - Insurance 80QQB
- INS_80RRB (float) - Insurance 80RRB
- INS_80TTB (float) - Insurance 80TTB
- ExtraTDS (varchar) - Extra TDS details
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- REC_VERSION (tinyint) - Record version

CONSTRAINTS:
- Primary Key: ID (Clustered)
- Foreign Key: EMP_ID → ESS_EMPLOYEE.ID

================================================================================
TABLE: ESS_ROLES
================================================================================
DESCRIPTION: Defines user roles with privilege mappings for access control.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- CODE (varchar) - Role code
- NAME (varchar) - Role name
- ROLE_LEVEL (int) - Role hierarchy level
- REMARKS (varchar) - Remarks
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (datetime) - Creation timestamp
- MODIFIED_BY (varchar) - Modifier user ID
- MODIFIED_ON (datetime) - Modification timestamp
- VERSION (tinyint) - Record version

CONSTRAINTS:
- Primary Key: ID (Clustered)

================================================================================
TABLE: ESS_PERMISSIONS (via ESS_ROLE_PRIVILEGES)
================================================================================
DESCRIPTION: Defines system permissions and associates them with roles.

TABLE: ESS_PRIVILEGES
COLUMNS:
- ID (smallint) (Primary Key) - Identifier
- PRIV_NAME (varchar) - Permission name
- DISPLAY_NAME (varchar) - Display name

TABLE: ESS_ROLE_PRIVILEGES
COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- ROLE_ID (bigint) - Role ID (Foreign Key)
- PRIVILEGE_ID (smallint) - Privilege ID (Foreign Key)

CONSTRAINTS:
- Foreign Key: ROLE_ID → ESS_ROLES.ID
- Foreign Key: PRIVILEGE_ID → ESS_PRIVILEGES.ID

================================================================================
TABLE: ESS_USER_ROLE
================================================================================
DESCRIPTION: Associates users with roles for permission-based access control.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- USER_ID (bigint) - User ID (Foreign Key)
- ROLE_ID (bigint) - Role ID (Foreign Key)
- START_DATE (smalldatetime) - Role assignment start date
- END_DATE (smalldatetime) - Role assignment end date

CONSTRAINTS:
- Primary Key: ID (Clustered)
- Foreign Key: USER_ID → ESS_USERS.ID
- Foreign Key: ROLE_ID → ESS_ROLES.ID

================================================================================
TABLE: ESS_LOGIN_INFO
================================================================================
DESCRIPTION: Tracks user login activities for security auditing.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID (Foreign Key)
- USER_ID (bigint) - User ID (Foreign Key)
- USER_NAME (varchar) - Username at login
- LOGGED_ON (datetime) - Login timestamp
- IP_ADDR (varchar) - IP address
- STATUS (bit) - Login status

CONSTRAINTS:
- Primary Key: ID (Clustered)
- Foreign Key: TEN_ID → ESS_TENANT.ID
- Foreign Key: USER_ID → ESS_USERS.ID

================================================================================
TABLE: ESS_WORKFLOW_DEF
================================================================================
DESCRIPTION: Defines approval workflows for various document types.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- NAME (varchar) - Workflow name
- DOC_TYPE (varchar) - Document type
- CON_TO_ACTIVATE (varchar) - Conditions to activate
- APP_STATUS_NAME (varchar) - Approval status name
- REJ_STATUS_NAME (varchar) - Rejection status name
- UPD_FINAL_DOC_STATUS (bit) - Update final document status flag
- DOC_STATUS_COL (varchar) - Document status column
- APP_DOC_STATUS (tinyint) - Approved document status
- REJ_DOC_STATUS (tinyint) - Rejected document status
- CAN_DOC_STATUS (tinyint) - Cancelled document status
- CAN_HOLD (bit) - Can hold flag
- PRIORITY (int) - Priority level
- NOTIFY_AT (varchar) - Notification trigger
- EMAIL_IDS (varchar) - Notification email addresses
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- REC_VERSION (tinyint) - Record version

CONSTRAINTS:
- Primary Key: ID (Clustered)

================================================================================
TABLE: ESS_WORKFLOW_STAGE
================================================================================
DESCRIPTION: Defines stages within an approval workflow.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- NAME (varchar) - Stage name
- STAGE_INDEX (int) - Execution order
- DOC_STATUS (varchar) - Document status at this stage
- MIN_APPRORAL (tinyint) - Minimum approvals required
- MIN_REJECTION (tinyint) - Minimum rejections to reject
- WORKFLOW_DEF_ID (bigint) - Parent workflow definition
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- REC_VERSION (tinyint) - Record version
- AUTO_ACTION (bit) - Automatic action flag
- SCRIPT (varchar) - Custom script/logic
- PROPERTY (varchar) - Stage properties
- Type (varchar) - Stage type

CONSTRAINTS:
- Primary Key: ID (Clustered)

================================================================================
TABLE: ESS_WORKFLOW
================================================================================
DESCRIPTION: Tracks workflow instances for documents under approval.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- DOC_ID (bigint) - Document ID
- WORKFLOW_DEF_ID (bigint) - Workflow definition ID (Foreign Key)
- DOC_TYPE (varchar) - Document type
- STATUS (tinyint) - Workflow status
- CURRENT_STAGE_ID (bigint) - Current stage ID
- CURRENT_STAGE (tinyint) - Current stage number
- MAX_STAGE (tinyint) - Maximum stages
- REQUESTER_ID (bigint) - Requester/creator ID
- ON_HOLD (tinyint) - On hold flag
- OUTCOME_DECIDED_ON (smalldatetime) - Outcome decision date
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- REC_VERSION (tinyint) - Record version
- CUSTOM_ATTRIBUTES (varchar) - Custom attributes JSON

CONSTRAINTS:
- Primary Key: ID (Clustered)
- Foreign Key: WORKFLOW_DEF_ID → ESS_WORKFLOW_DEF.ID

================================================================================
TABLE: ESS_WORKFLOW_ACTIONS
================================================================================
DESCRIPTION: Records approver actions (approve/reject/comment) on workflow stages.

COLUMNS:
- ID (bigint) (Primary Key) - Auto-increment identifier
- TEN_ID (bigint) - Tenant ID
- FK_DOC_WORKFLOW_ID (bigint) - Workflow instance ID (Foreign Key)
- STAGE_ID (bigint) - Workflow stage ID
- APPROVER (bigint) - Approver user ID
- ACTION (tinyint) - Action taken (Approve/Reject/etc)
- COMMENTS (varchar) - Approver comments
- CREATED_BY (bigint) - Creator user ID
- CREATED_ON (smalldatetime) - Creation timestamp
- MODIFIED_BY (bigint) - Modifier user ID
- MODIFIED_ON (smalldatetime) - Modification timestamp
- REC_VERSION (tinyint) - Record version

CONSTRAINTS:
- Primary Key: ID (Clustered)
- Foreign Key: FK_DOC_WORKFLOW_ID → ESS_WORKFLOW.ID

================================================================================
NOTE: DATABASE CONTAINS 500+ ADDITIONAL TABLES
================================================================================
The complete ESS database includes comprehensive tables for:
- Employee Training & Development
- Performance Management & Reviews
- Asset Management & Allocation
- Attendance & Leave Management
- Payroll Processing & Taxation
- Document Management & Templates
- Job Recruitment & Applicant Tracking
- Vendor & Supplier Management
- Configuration & System Settings
- Audit Logging & Data History
- And many more specialized modules

For complete table listings and detailed schemas, refer to the full SQL 
script file (tablescript.sql).

================================================================================
DATABASE RELATIONSHIPS AND KEY MAPPINGS
================================================================================

CORE HIERARCHIES:
- ESS_TENANT (Organization) 
  ├─ ESS_EMPLOYEE (Employees)
  ├─ ESS_ORGANIZATION (Business Units)
  │  ├─ ESS_DEPARTMENT
  │  ├─ ESS_DESIGNATION
  │  └─ ESS_LOCATION
  ├─ ESS_LEAVE (Leave Types)
  ├─ ESS_SHIFT (Shift Schedules)
  └─ ESS_ROLES (Access Control)

EMPLOYEE RECORDS:
- ESS_EMPLOYEE (Master Record)
  ├─ ESS_EMPLOYEE_STATUTORY (Tax/Compliance)
  ├─ ESS_EMPLOYEE_PAYSTRUCTURE (Salary Components)
  ├─ ESS_EMPLOYEE_TIMEENTRIES (Attendance)
  ├─ ESS_EMPLOYEE_SHIFT (Shift Assignments)
  ├─ ESS_EMPLOYEE_LEAVE (Leave Policy)
  ├─ ESS_EMPLOYEE_TIMESHEET (Timesheet Summary)
  └─ ESS_EMPLOYEE_TRAINING (Training Records)

LEAVE MANAGEMENT:
- ESS_LEAVE_STRUCTURE (Policy)
  └─ ESS_LEAVE_STRUCTURE_ITEM (Leave Types in Policy)
- ESS_EMPLOYEE_LEAVE (Employee Assignment)
  └─ ESS_LEAVE_REQUISITION (Leave Requests)
    └─ ESS_LEAVE_REQ_DETAILS (Individual Dates)
- ESS_LEAVE_ACCUMULATION (Balance Tracking)

PAYROLL:
- ESS_PAYSLIP_ITEM (Line Items)
  ├─ ESS_PAYSLIP_ITEM_CATEGORY
  ├─ ESS_PAYSLIP_ITEM_GROUP
  └─ ESS_PAYSTRUCT_TEMPLATE
- ESS_PAYSLIP (Monthly Payslip)
  ├─ ESS_PAYSLIP_DETAILS
  └─ ESS_PAYSLIP_LINEITEM
- ESS_TAX_DECLARATION (Tax Info)
- ESS_FORM16 (Tax Certificate)

REIMBURSEMENT:
- ESS_REIMBURSEMENT_TYPE (Expense Categories)
  └─ ESS_REIMBURSEMENT (Expense Claims)

WORKFLOWS:
- ESS_WORKFLOW_DEF (Workflow Definitions)
  └─ ESS_WORKFLOW_STAGE (Approval Stages)
- ESS_WORKFLOW (Active Workflows)
  ├─ ESS_WORKFLOW_ACTIONS (Approver Actions)
  └─ ESS_WORKFLOW_ATTACHMENTS (Supporting Docs)

ACCESS CONTROL:
- ESS_ROLES (Roles)
  ├─ ESS_ROLE_PRIVILEGES (Permission Assignments)
  └─ ESS_USER_ROLE (User-Role Mapping)
- ESS_USERS (User Accounts)
  └─ ESS_LOGIN_INFO (Login Audit)
- ESS_DATA_AUTH (Data-Level Authorization)

SECURITY & AUDIT:
- ESS_AUDITLOG (System Changes)
- [HISTORY tables] for temporal versioning
  ├─ ESS_EMPLOYEE_History
  ├─ ESS_EMPLOYEE_STATUTORY_History
  ├─ ESS_EMPLOYEE_PAYSTRUCTURE_History
  └─ [Many more temporal tables]

================================================================================
END OF DATABASE DOCUMENTATION
================================================================================

"""