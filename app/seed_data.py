"""
Seed data — curated Indian MSME compliance knowledge base.
~30 snippets covering GST, labor laws, MSME registration, tax exemptions,
and Gujarat-specific textile policies.
"""

SEED_DOCUMENTS = [
    # ─── GST ─────────────────────────────────────────────────────
    {
        "content": (
            "GST Registration Thresholds for MSMEs: "
            "Businesses with aggregate annual turnover below ₹40 lakh (₹20 lakh for services "
            "and for special category states) are exempt from GST registration. "
            "For inter-state supply of goods, registration is mandatory regardless of turnover. "
            "Casual taxable persons and non-resident taxable persons must also register "
            "irrespective of turnover. As per CGST Act Section 22 and 24."
        ),
        "metadata": {
            "source": "CGST Act 2017, Sections 22 & 24",
            "category": "GST",
            "subcategory": "Registration",
        },
    },
    {
        "content": (
            "GST Composition Scheme: MSMEs with aggregate turnover up to ₹1.5 crore "
            "(₹75 lakh for special category states) can opt for the Composition Scheme under "
            "Section 10 of CGST Act. Under this scheme, manufacturers pay GST at 1%, "
            "restaurants pay 5%, and other suppliers pay 1% of turnover. Service providers "
            "with turnover up to ₹50 lakh can opt for 6% composition rate. "
            "Key restrictions: Cannot collect GST from customers, cannot claim Input Tax "
            "Credit (ITC), cannot make inter-state supplies, and must file quarterly returns "
            "(GSTR-4) instead of monthly returns."
        ),
        "metadata": {
            "source": "CGST Act 2017, Section 10",
            "category": "GST",
            "subcategory": "Composition Scheme",
        },
    },
    {
        "content": (
            "Input Tax Credit (ITC) under GST: Registered businesses can claim ITC on goods "
            "and services used for business purposes under Section 16 of CGST Act. "
            "ITC is available on inputs, capital goods, and input services. "
            "Conditions for claiming ITC: Must possess a valid tax invoice, goods/services "
            "must have been received, tax must be actually paid to the government by the "
            "supplier, and the buyer must have filed GSTR-3B return. "
            "ITC is blocked on motor vehicles (with exceptions), food & beverages, "
            "health & fitness services, and personal consumption goods."
        ),
        "metadata": {
            "source": "CGST Act 2017, Sections 16-18",
            "category": "GST",
            "subcategory": "Input Tax Credit",
        },
    },
    {
        "content": (
            "GST Returns Filing for MSMEs: Regular taxpayers must file GSTR-1 (outward "
            "supplies, monthly/quarterly), GSTR-3B (summary return, monthly), and GSTR-9 "
            "(annual return). Small taxpayers with turnover up to ₹5 crore can file "
            "quarterly GSTR-1 under the QRMP scheme while paying tax monthly via PMT-06. "
            "Late filing attracts a late fee of ₹50/day (₹20/day for Nil returns) "
            "plus 18% annual interest on outstanding tax."
        ),
        "metadata": {
            "source": "CGST Act 2017, Sections 37-44",
            "category": "GST",
            "subcategory": "Returns Filing",
        },
    },
    {
        "content": (
            "GST Rates for Textile Industry: As per the GST Council's revised rates effective "
            "from January 2022, all textile products attract 5% GST for items with sale value "
            "up to ₹1,000 per piece and 12% GST for items above ₹1,000 per piece. "
            "Cotton fabrics, man-made fabrics, silk, and wool fabrics all follow the same "
            "rate structure. Job work on textiles attracts 5% GST (12% for man-made fiber "
            "garments). Export of textiles is zero-rated under GST, and exporters can claim "
            "refund of accumulated ITC."
        ),
        "metadata": {
            "source": "GST Council Notification, GST Rate Schedule",
            "category": "GST",
            "subcategory": "Textile Rates",
        },
    },

    # ─── MSME REGISTRATION ───────────────────────────────────────
    {
        "content": (
            "Udyam Registration for MSMEs: The Government of India replaced the earlier "
            "UAM system with Udyam Registration (effective July 1, 2020) under the MSME "
            "Development Act, 2006. Registration is free and fully online at udyamregistration.gov.in. "
            "Classification is based on investment in plant/machinery/equipment AND annual turnover: "
            "Micro Enterprise: Investment up to ₹1 crore AND turnover up to ₹5 crore. "
            "Small Enterprise: Investment up to ₹10 crore AND turnover up to ₹50 crore. "
            "Medium Enterprise: Investment up to ₹50 crore AND turnover up to ₹250 crore. "
            "Both criteria must be satisfied. PAN and Aadhaar are mandatory for registration."
        ),
        "metadata": {
            "source": "MSME Development Act 2006, Udyam Registration Portal",
            "category": "MSME Registration",
            "subcategory": "Udyam Registration",
        },
    },
    {
        "content": (
            "Benefits of Udyam/MSME Registration: "
            "1) Priority sector lending from banks at lower interest rates. "
            "2) Collateral-free loans under the Credit Guarantee Fund Trust for Micro and Small Enterprises (CGTMSE). "
            "3) Protection against delayed payments — buyers must pay within 45 days, else pay compound interest at 3x the bank rate. "
            "4) Eligible for government tenders with 25% procurement reservation for MSMEs. "
            "5) Subsidy on patent and trademark registration. "
            "6) ISO certification reimbursement. "
            "7) Eligible for the CLCSS (Credit Linked Capital Subsidy Scheme) — 15% capital subsidy on technology upgradation."
        ),
        "metadata": {
            "source": "MSME Development Act 2006, Government Schemes",
            "category": "MSME Registration",
            "subcategory": "Benefits",
        },
    },

    # ─── LABOR LAWS ──────────────────────────────────────────────
    {
        "content": (
            "Key Labor Laws for Indian MSMEs — Minimum Wages Act, 1948: "
            "Every employer must pay minimum wages as notified by the Central or State Government. "
            "Rates vary by state, industry sector, and skill level (unskilled, semi-skilled, skilled, "
            "highly skilled). For example, in Gujarat (2024), minimum wages for unskilled workers in "
            "the textile industry are approximately ₹11,518-₹12,768 per month. "
            "Non-compliance can result in fines up to ₹50,000 and imprisonment up to 3 months. "
            "Under the new Code on Wages 2019, a national floor wage will be established."
        ),
        "metadata": {
            "source": "Minimum Wages Act 1948, Code on Wages 2019",
            "category": "Labor Laws",
            "subcategory": "Minimum Wages",
        },
    },
    {
        "content": (
            "Employee Provident Fund (EPF) for MSMEs: Under the EPF & Miscellaneous Provisions "
            "Act 1952, EPF is mandatory for establishments with 20 or more employees. "
            "Both employer and employee contribute 12% of basic wages + DA to the fund. "
            "For establishments with up to 20 employees, EPF is optional but encouraged. "
            "New MSMEs get a government subsidy: Under the Pradhan Mantri Rojgar Protsahan Yojana "
            "(PMRPY), the government contributes the employer's full EPF contribution (12%) "
            "for new employees with salary up to ₹15,000/month for 3 years."
        ),
        "metadata": {
            "source": "EPF & Miscellaneous Provisions Act 1952",
            "category": "Labor Laws",
            "subcategory": "EPF",
        },
    },
    {
        "content": (
            "Employees' State Insurance (ESI) for MSMEs: ESI is mandatory for factories "
            "and establishments with 10 or more employees where wages do not exceed ₹21,000/month "
            "(₹25,000/month for disabled employees). Employer contribution: 3.25% of wages. "
            "Employee contribution: 0.75% of wages. ESI provides medical benefits, sickness "
            "benefit, maternity benefit, disablement benefit, and dependants' benefit. "
            "New MSMEs in notified areas must register within 15 days of becoming applicable."
        ),
        "metadata": {
            "source": "ESI Act 1948",
            "category": "Labor Laws",
            "subcategory": "ESI",
        },
    },
    {
        "content": (
            "Shops and Establishments Act — Gujarat: The Gujarat Shops and Establishments "
            "(Regulation of Employment and Conditions of Service) Act, 2019 applies to all "
            "commercial establishments in Gujarat. Key provisions: Maximum working hours: "
            "9 hours/day and 48 hours/week. Overtime wages: 2x the ordinary rate. "
            "Weekly holiday: Minimum one day off per week. Annual leave: 1 day for every "
            "20 days worked. Registration must be obtained within 60 days of commencement. "
            "The Act also mandates appointment letters, wage slips, and maintenance of registers."
        ),
        "metadata": {
            "source": "Gujarat Shops and Establishments Act 2019",
            "category": "Labor Laws",
            "subcategory": "Shops & Establishments",
            "state": "Gujarat",
        },
    },
    {
        "content": (
            "Factories Act 1948 for Manufacturing MSMEs: Applicable to premises with 10+ "
            "workers (with power) or 20+ workers (without power). Key requirements: "
            "1) Obtain factory license from State Factory Inspectorate before commencing operations. "
            "2) Maintain clean, ventilated, and well-lit premises. "
            "3) Provide drinking water, toilets, first-aid, and canteen (for 250+ workers). "
            "4) Working hours: Max 48 hours/week and 9 hours/day. "
            "5) Overtime: 2x wages. "
            "6) Annual leave with wages: 1 day per 20 working days. "
            "7) No employment of young persons (under 14 years) in any factory."
        ),
        "metadata": {
            "source": "Factories Act 1948",
            "category": "Labor Laws",
            "subcategory": "Factories Act",
        },
    },
    {
        "content": (
            "New Labor Codes 2020 — Impact on MSMEs: India has consolidated 29 labor laws "
            "into 4 new Labor Codes: "
            "1) Code on Wages, 2019 — Universal minimum wage, timely payment. "
            "2) Code on Social Security, 2020 — EPF, ESI, gratuity, maternity in a single framework; "
            "extends social security to gig and platform workers. "
            "3) Occupational Safety, Health and Working Conditions Code, 2020 — Establishes "
            "national standards for working conditions across all industries. "
            "4) Industrial Relations Code, 2020 — Standing orders mandatory for 300+ workers "
            "(up from 100), easier retrenchment for firms with under 300 workers. "
            "These codes simplify compliance for MSMEs significantly."
        ),
        "metadata": {
            "source": "Labor Codes 2020, Ministry of Labour & Employment",
            "category": "Labor Laws",
            "subcategory": "New Labor Codes",
        },
    },

    # ─── TAX EXEMPTIONS ──────────────────────────────────────────
    {
        "content": (
            "Income Tax Exemptions for MSMEs — Section 115BA: Domestic companies engaged "
            "in manufacturing (set up and registered on or after March 1, 2016) can opt for "
            "a reduced corporate tax rate of 25% (plus surcharge and cess), provided they: "
            "Do not claim any profit-linked deductions (under Chapter VI-A, except Section 80JJAA), "
            "do not claim investment-linked deductions (Section 35AD), and do not claim "
            "additional depreciation (Section 32(1)(iia)). "
            "Alternatively, under Section 115BAA, any domestic company can opt for a 22% tax rate "
            "(effective ~25.17%) by forgoing all exemptions and deductions."
        ),
        "metadata": {
            "source": "Income Tax Act, Sections 115BA, 115BAA",
            "category": "Tax Exemptions",
            "subcategory": "Corporate Tax Rates",
        },
    },
    {
        "content": (
            "Section 115BAB — New Manufacturing Companies: Domestic companies incorporated "
            "on or after October 1, 2019 AND commencing manufacturing before March 31, 2024 "
            "can opt for a super-reduced tax rate of 15% (effective ~17.16% including surcharge "
            "and cess). Conditions: Must be engaged solely in manufacturing or production of "
            "any article or thing (not software development). Must not use any building, "
            "machinery, or plant previously used for any purpose. This is highly beneficial "
            "for new textile manufacturing startups setting up fresh operations."
        ),
        "metadata": {
            "source": "Income Tax Act, Section 115BAB",
            "category": "Tax Exemptions",
            "subcategory": "New Manufacturing",
        },
    },
    {
        "content": (
            "Presumptive Taxation for Small MSMEs — Section 44AD: Eligible businesses with "
            "turnover up to ₹2 crore (₹3 crore if 95% of receipts are digital) can declare "
            "income at 6% of digital turnover and 8% of cash turnover, without maintaining "
            "detailed books of accounts. This significantly reduces compliance burden. "
            "Similarly, Section 44ADA allows professionals with gross receipts up to ₹75 lakh "
            "(if 95% digital) to declare income at 50% of receipts. "
            "These schemes are available to individuals, HUFs, and partnership firms (not LLPs)."
        ),
        "metadata": {
            "source": "Income Tax Act, Sections 44AD, 44ADA",
            "category": "Tax Exemptions",
            "subcategory": "Presumptive Taxation",
        },
    },
    {
        "content": (
            "Startup Tax Holiday — Section 80-IAC: Eligible startups recognized by DPIIT "
            "(Department for Promotion of Industry and Internal Trade) can claim 100% tax "
            "deduction on profits for 3 consecutive years out of the first 10 years from "
            "incorporation. Eligibility: Incorporated as a Private Limited Company or LLP, "
            "turnover must not exceed ₹100 crore in any financial year, and must be engaged "
            "in innovation, development, or improvement of products/processes/services. "
            "Application must be made to the Inter-Ministerial Board of Certification."
        ),
        "metadata": {
            "source": "Income Tax Act, Section 80-IAC",
            "category": "Tax Exemptions",
            "subcategory": "Startup Tax Holiday",
        },
    },
    {
        "content": (
            "Capital Gains Exemption — Section 54GB: Individuals and HUFs can claim exemption "
            "from long-term capital gains on sale of a residential property if the net "
            "consideration is invested in subscription of equity shares of an eligible startup "
            "(before the due date of filing ITR) and the startup utilizes the amount to "
            "purchase new plant and machinery (not second-hand). Minimum holding period: "
            "5 years. The startup must qualify under Section 80-IAC."
        ),
        "metadata": {
            "source": "Income Tax Act, Section 54GB",
            "category": "Tax Exemptions",
            "subcategory": "Capital Gains",
        },
    },
    {
        "content": (
            "Section 43B(h) — Timely Payment to MSMEs: Effective from April 1, 2024 (AY 2024-25), "
            "any amount payable to a Micro or Small Enterprise (registered under MSMED Act) "
            "is allowed as a deduction only in the year in which it is actually paid, not on "
            "an accrual basis. Payment must be within the time limit specified: 15 days "
            "(if no written agreement) or 45 days (with written agreement) from the date of "
            "acceptance or deemed acceptance. This provision ensures large companies pay MSMEs "
            "on time, as delayed payments increase the buyer's tax liability."
        ),
        "metadata": {
            "source": "Income Tax Act, Section 43B(h), Finance Act 2023",
            "category": "Tax Exemptions",
            "subcategory": "Timely Payment Protection",
        },
    },

    # ─── GUJARAT TEXTILE POLICY ──────────────────────────────────
    {
        "content": (
            "Gujarat Textile Policy 2024 — Overview: The Government of Gujarat announced the "
            "Gujarat Textile Policy 2024 to position Gujarat as India's leading textile hub. "
            "Key objectives: Attract ₹50,000 crore new investment in textiles, create 5 lakh "
            "new jobs, promote technical textiles and man-made fiber (MMF) production, "
            "encourage women entrepreneurship, and develop integrated textile parks. "
            "The policy is valid for 5 years (2024-2029) and covers ginning, spinning, weaving, "
            "knitting, processing, garmenting, technical textiles, and home textiles."
        ),
        "metadata": {
            "source": "Gujarat Textile Policy 2024, Government of Gujarat",
            "category": "State Policy",
            "subcategory": "Gujarat Textile Policy",
            "state": "Gujarat",
        },
    },
    {
        "content": (
            "Gujarat Textile Policy 2024 — Capital Subsidies: "
            "The policy offers tiered capital subsidies based on location (taluka category): "
            "Category A talukas (most developed): 10% of eligible fixed capital investment (FCI), "
            "maximum ₹50 crore. "
            "Category B talukas: 15% of FCI, maximum ₹75 crore. "
            "Category C talukas (least developed): 20% of FCI, maximum ₹100 crore. "
            "For MSMEs specifically: Additional 5% capital subsidy on top of the base rate. "
            "For SC/ST/Women entrepreneurs: Additional 5% subsidy. "
            "For technical textile projects: Additional 10% subsidy. "
            "Maximum combined capital subsidy is capped at 35% of FCI or ₹100 crore."
        ),
        "metadata": {
            "source": "Gujarat Textile Policy 2024, Section: Capital Subsidy",
            "category": "State Policy",
            "subcategory": "Capital Subsidies",
            "state": "Gujarat",
        },
    },
    {
        "content": (
            "Gujarat Textile Policy 2024 — Payroll and Training Assistance: "
            "Monthly payroll assistance for each new employee: "
            "Female workers: ₹3,000 - ₹5,000/month for 5 years depending on taluka category. "
            "Male workers: ₹2,000 - ₹3,000/month for 5 years depending on taluka category. "
            "Skill development support: 50% reimbursement of training costs (max ₹5,000 per worker). "
            "Preference for units employing 50%+ women workforce: Additional 2% interest subsidy. "
            "Target: Create 5 lakh direct jobs in the textile sector by 2029."
        ),
        "metadata": {
            "source": "Gujarat Textile Policy 2024, Section: Employment Generation",
            "category": "State Policy",
            "subcategory": "Payroll Assistance",
            "state": "Gujarat",
        },
    },
    {
        "content": (
            "Gujarat Textile Policy 2024 — Interest Subsidy and Power Tariff: "
            "Interest subsidy on term loans: 5% for MSMEs (7% for SC/ST/Women entrepreneurs) "
            "for a period of 7 years, maximum ₹25 lakh per annum. "
            "Power tariff concession: ₹1/unit discount for first 5 years for new textile units "
            "in notified textile parks. Additional ₹0.50/unit discount for units using solar energy. "
            "Quality certification support: 75% reimbursement (max ₹2 lakh) for obtaining "
            "quality certifications like ISO, ZED, OEKO-TEX, GOTS (Global Organic Textile Standard)."
        ),
        "metadata": {
            "source": "Gujarat Textile Policy 2024, Section: Interest & Power",
            "category": "State Policy",
            "subcategory": "Interest & Power Subsidy",
            "state": "Gujarat",
        },
    },
    {
        "content": (
            "Gujarat Textile Policy 2024 — Incentives for Startups and MSMEs: "
            "Special provisions for textile startups in Gujarat: "
            "1) Plug-and-play infrastructure in Gujarat Industrial Development Corporation (GIDC) "
            "textile parks at subsidized rates. "
            "2) Net SGST reimbursement: 50-75% of net SGST paid for 7-10 years based on investment. "
            "3) Stamp duty and registration fee: 100% exemption for new textile units. "
            "4) Land allotment: Priority allotment in GIDC at subsidized rates for MSMEs. "
            "5) Technology upgrade fund: Reimbursement of up to 50% of cost of new technology/"
            "machinery (max ₹25 lakh). "
            "6) Patent support: 75% reimbursement of patent registration costs."
        ),
        "metadata": {
            "source": "Gujarat Textile Policy 2024, Section: Startup Incentives",
            "category": "State Policy",
            "subcategory": "Startup Incentives",
            "state": "Gujarat",
        },
    },
    {
        "content": (
            "Aatmanirbhar Gujarat Scheme for MSMEs (2022-2027): "
            "A comprehensive state-level MSME support scheme offering: "
            "1) Capital Investment Subsidy: 25% of FCI for micro, 15% for small, 10% for medium "
            "in Category C/D talukas (lower percentages in developed areas). "
            "2) Interest subsidy: 7% on term loan for 7 years (max ₹25 lakh/year) for micro & small. "
            "3) Net SGST reimbursement: 100% for 10 years in underdeveloped talukas. "
            "4) Assistance for ZED/ISO certification, ICT adoption, technology upgradation, "
            "and patent registration. "
            "5) Cluster development: Support for shared infrastructure, common facility centers."
        ),
        "metadata": {
            "source": "Aatmanirbhar Gujarat MSME Scheme 2022-2027",
            "category": "State Policy",
            "subcategory": "Aatmanirbhar Gujarat",
            "state": "Gujarat",
        },
    },
    {
        "content": (
            "Gujarat Industrial Policy 2020 — MSME Incentives: "
            "Special incentives for MSMEs in Gujarat under the Industrial Policy 2020: "
            "1) Capital subsidy of 12-25% based on taluka category for manufacturing MSMEs. "
            "2) Reduced power tariff: ₹1/unit concession for 3-5 years. "
            "3) Waiver of electricity duty for 5 years. "
            "4) Special incentives for women, SC/ST, and rural entrepreneurs: "
            "additional 5% capital subsidy and 2% additional interest subsidy. "
            "5) Priority allocation of industrial plots. "
            "6) Single-window clearance system through Investor Facilitation Portal."
        ),
        "metadata": {
            "source": "Gujarat Industrial Policy 2020",
            "category": "State Policy",
            "subcategory": "Industrial Policy",
            "state": "Gujarat",
        },
    },

    # ─── COMPLIANCE DEADLINES & PRACTICAL ────────────────────────
    {
        "content": (
            "Key Annual Compliance Calendar for Indian MSMEs: "
            "Monthly: GST return filing (GSTR-3B by 20th, GSTR-1 by 11th), TDS payment (7th). "
            "Quarterly: GST Composition return (GSTR-4 by 18th), advance tax installments "
            "(June 15, Sept 15, Dec 15, March 15). "
            "Annual: Income tax return (October 31 for audit cases, July 31 otherwise), "
            "GST annual return GSTR-9 (December 31), Tax audit report (September 30), "
            "DIR-3 KYC for directors (September 30), Company annual filing (October 30). "
            "MSME: Udyam Registration update whenever investment/turnover classification changes."
        ),
        "metadata": {
            "source": "Income Tax Act, CGST Act, Companies Act",
            "category": "Compliance Calendar",
            "subcategory": "Annual Deadlines",
        },
    },
    {
        "content": (
            "Environmental Compliance for Textile MSMEs in Gujarat: "
            "Textile processing units (dyeing, bleaching, printing) are classified as "
            "Red/Orange category by the Central Pollution Control Board (CPCB). "
            "Requirements: "
            "1) Consent to Establish (CTE) and Consent to Operate (CTO) from Gujarat Pollution "
            "Control Board (GPCB) before commencing operations. "
            "2) Zero Liquid Discharge (ZLD) systems mandatory for new dyeing and processing "
            "units in Gujarat since 2015. "
            "3) Annual environmental statement submission. "
            "4) Hazardous waste management authorization. "
            "Non-polluting textile units (garment manufacturing, weaving without processing) "
            "are classified as White/Green category with simplified compliance."
        ),
        "metadata": {
            "source": "Environment Protection Act 1986, GPCB Guidelines",
            "category": "Environmental Compliance",
            "subcategory": "Textile Industry",
            "state": "Gujarat",
        },
    },
    {
        "content": (
            "Export Incentives for Textile MSMEs: "
            "1) Rebate of State and Central Taxes and Levies (RoSCTL): Textile and apparel "
            "exporters can claim duty credits at rates ranging from 1.5% to 6.05% of FOB value. "
            "2) Remission of Duties and Taxes on Exported Products (RoDTEP): Additional "
            "rebate of 0.5% to 4.3% on exported textiles. "
            "3) Advance Authorization scheme: Duty-free import of raw materials for export production. "
            "4) Export Promotion Capital Goods (EPCG) scheme: Zero-duty import of capital goods "
            "against export obligations (6x CIF value in 6 years). "
            "5) Market Access Initiative (MAI) scheme: Financial assistance for export promotion "
            "activities, trade fairs, and buyer-seller meets."
        ),
        "metadata": {
            "source": "Foreign Trade Policy 2023, DGFT",
            "category": "Export Incentives",
            "subcategory": "Textile Exports",
        },
    },
    {
        "content": (
            "Intellectual Property Protection for Textile MSMEs: "
            "MSMEs can protect their textile designs and innovations through: "
            "1) Design Registration: Register unique textile patterns/prints under the Designs "
            "Act, 2000 for 10 years (extendable by 5 years). Fee for MSMEs: ₹1,000. "
            "2) Trademark Registration: Protect brand names, logos for ₹4,500 under the "
            "Trademarks Act, 1999. Valid for 10 years, renewable. "
            "3) Geographical Indication (GI): Textiles like Patola silk, Kutchi embroidery, "
            "Tangaliya weaving have GI tags in Gujarat. GI registration lasts 10 years. "
            "4) MSME subsidy: 50% reimbursement of patent/trademark costs under MSME schemes."
        ),
        "metadata": {
            "source": "Designs Act 2000, Trademarks Act 1999, GI Act 1999",
            "category": "Intellectual Property",
            "subcategory": "IP Protection for Textiles",
        },
    },
]
