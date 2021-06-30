from flask import Flask

import xlrd

import json


app = Flask(__name__)


def findCell(sh, searchedValue1):
    if searchedValue1 == "PROFIT FOR THE CURRENT YEAR" or searchedValue1 == "LOSS FOR THE CURRENT YEAR" or searchedValue1 == "PROFIT FOR THE PREVIOUS YEAR" or searchedValue1 == "LOSS FOR THE PREVIOUS YEAR":
        for row in range(sh.nrows):
            for col in range(sh.ncols):
                myCell = sh.cell(row, col)
                if myCell.value == searchedValue1:
                    return sh.cell(row, col + 2)
    else:
        for row in range(sh.nrows):
            for col in range(sh.ncols):
                myCell = sh.cell(row, col)
                if myCell.value == searchedValue1:
                    return sh.cell(row, col + 1)

                # return xl_rowcol_to_cell(row, col+1)
    return -1
@app.route('/oss1')

def hello_world():
    headers = {'Access-Control-Allow-Origin': '*'}
    searchedValue = 'SUBSCRIBED AND PAID UP'
    searchedValue1 = 'STATE GOVERNMENT'
    searchedValue2 = 'OTHER PAIDUP'
    searchedValue3 = 'GENERAL RESERVE FUND'
    searchedValue4 = 'BUILDING FUND'
    searchedValue5 = 'PROFIT EQUALIZATION FUND'
    searchedValue6 = 'REVOLUTION FUND'
    searchedValue7 = 'CONTINGENT PROV.AGAINST'
    searchedValue8 = 'GENERAL PROV FUND'

    searchedValue9 = ' GRATUITY FUND'
    searchedValue10 = 'EDUCATION TRAINING'
    searchedValue11 = 'SILVER JUBILEE FUND'
    searchedValue12 = 'DEVELOPMENT FUND'
    searchedValue13 = 'DONATION A/C'
    searchedValue14 = 'INVESTMENT FLUCTUATION'
    searchedValue15 = 'OTHER PAT'

    searchedValue16 = 'PROFIT FOR THE CURRENT YEAR'
    searchedValue17 = 'LOSS FOR THE CURRENT YEAR'
    searchedValue18 = 'PROFIT FOR THE PREVIOUS YEAR'
    searchedValue19 = 'LOSS FOR THE PREVIOUS YEAR'

    searchedValue20 = 'SUBORIDINET DEBT'

    searchedValue21 = 'SAVING BANK'
    searchedValue22 = 'INOPERATIVE SAVING BANK'
    searchedValue23 = 'SAVINGS BANK INOPERATIVE'

    searchedValue24 = 'CURRENT DEPOSIT'
    searchedValue25 = 'CURRENT INOPERATIVE BANK'

    searchedValue26 = 'FIXED DEPOSIT'
    searchedValue27 = 'MONTHLY INCOME DEPOSIT'
    searchedValue28 = 'QUARTERLY INCOME DEPOSIT'
    searchedValue29 = 'REINVESTMENT DEPOSIT'
    searchedValue30 = 'RECURRING DEPOSIT'
    searchedValue31 = 'CREDIT BALANCE IN'
    searchedValue32 = 'CREDIT BALANCE IN OVER'
    searchedValue33 = 'COMPULSORY DEPOSIT ACCOUNT'

    searchedValue34 = 'OVERDUE INTEREST RESERVE'
    searchedValue35 = 'FIXED DEP. INTEREST'
    searchedValue36 = 'Borrowings'

    searchedValue37 = 'CLAIM AGAINST BANK'
    searchedValue38 = 'PARTLY PAID INVESTMENT'
    searchedValue39 = 'BANK GAURANTEE'
    searchedValue40 = 'FINACIAL'
    searchedValue41 = 'GAURENTEES OTHER'
    searchedValue42 = 'SALES AND REPURCHASE AGREENMENT'
    searchedValue43 = 'FORWARD EXCHANGE CONTRACTS'
    searchedValue44 = 'ACCEPTANCES ENDORSEMENTS'
    searchedValue45 = 'DEA FUND'

    searchedValue46 = 'INVESTMENT FLUCTUATON FUND'
    searchedValue47 = 'DEPRECIATION ON FIXED ASSETS'
    searchedValue48 = 'FOR OTHER IMPAIRED ASSETS'
    searchedValue49 = 'FOR CONTINGENT'
    searchedValue50 = 'SUBSTANDARD ASSETS RESERVE'
    searchedValue51 = 'BAD & DOUBTFUL DEBTS'
    searchedValue52 = 'BAD & DOUBTFUL DEBTS 5'

    # ASSETS
    searchedValue00 = 'CASH IN HAND'
    searchedValue01 = 'STATE BANK OF INDIA(CA)'
    searchedValue02 = 'STATE BANK OF INDIA(SA)'
    searchedValue03 = 'STATE BANK OF INDIA(FD)'
    searchedValue04 = 'RBI(CA)'
    searchedValue05 = 'RBI(Others)'
    searchedValue06 = 'CENTRAL COOPERATIVE BANK(CA)'
    searchedValue07 = 'CENTRAL COOPERATIVE BANK(SA)'
    searchedValue08 = 'CENTRAL COOPERATIVE BANK(FD)'
    searchedValue09 = 'CALL AND SHORT NOTICE MONEY TO COOPERATIVE BANKS'
    searchedValue010 = 'CALL AND SHORT NOTICE MONEY TO OTHER BANKS'
    searchedValue011 = 'LOANS AND ADVANCES TO SCHEDULED COOPERATIVE BANKS'
    searchedValue012 = 'LOANS AND ADVANCES TO NON SCHEDULED COOPERATIVE BANKS'
    searchedValue013 = 'LOANS AND ADVANCES TO OTHER BANKS'

    searchedValue014 = 'HDFC BANK LTD. OD A/C'
    searchedValue0014 = 'AXIS BANK LTD CURRENT A/C'
    searchedValue00014 = 'ICICI BANK LTD. CD A/C'

    searchedValue015 = 'HDFC BANK LTD(FD)'
    searchedValue0015 = 'DCB BANK'
    searchedValue00015 = 'THE SHAMRAO VITHAL COOP. BANK LTD F'
    searchedValue000015 = 'EQUITAS SMALL FINANCE BANK LIMITED'
    searchedValue0000015 = 'SURYODAY SMALL FINANCE BANK LIMITED'
    searchedValue00000015 = 'FINCARE SMALL FINANCE BANK LIMITED'
    searchedValue000000015 = 'JANA SMALL FINANCE BANK LTD.'
    searchedValue0000000015 = 'IDFC FIRST BANK LTD'
    searchedValue00000000015 = 'UTKARSH SMALL FINANCE BANK LTD'

    searchedValue016 = 'DUE FROM OTHER INSTITUTIONS(OTHERS)'
    searchedValue017 = 'GOI T. Bills'
    searchedValue018 = 'HDFC BANK SGL A/C'
    searchedValue019 = 'STATE GOVERNMENT SECURITY'
    searchedValue020 = 'OTHER TRUSTEE'
    searchedValue021 = 'NON SLR INVESTMENT (LIQUID FUND)'
    searchedValue022 = 'NON SLR INVESTMENT NHAI BOND TAX FR'
    searchedValue023 = 'INVESTMENT IN SUBSIDIARIES'
    searchedValue024 = 'INDORE PREMIER COOP.BANK LTD.SHARE'
    searchedValue025 = 'SHARE OF ALL INDIA'
    searchedValue026 = 'UNITS OF MUTUAL FUND'
    searchedValue027 = 'OTHER STATE GOVERNMENT SECURITY'
    searchedValue028 = 'Bonds of PSUs All India Financial Institutions'
    searchedValue029 = 'LOAN AGAINST FIXED DEPOSIT'
    searchedValue030 = 'OVERDRAFT GOLD LOAN'
    searchedValue031 = 'GOLD LOAN'
    searchedValue032 = 'UNSECURED SHORT TERMS LOANS'
    searchedValue033 = 'CASH CREDIT'
    searchedValue034 = 'OVER DRAFT'
    searchedValue035 = 'OVER DRAFT MORTGAGE'
    searchedValue036 = 'UNSECURED CASH CREDITS OVERDRAFTS'
    searchedValue037 = 'MEDIUM TERM SECURED LOAN'
    searchedValue038 = 'MEDIUM TERM UNSECURED LOAN'
    searchedValue039 = 'LONG TERM SECURED LOAN'
    searchedValue040 = 'LONG TERM UNSECURED LOAN'
    searchedValue041 = 'BILLS HUNDIES PURCHASED DISCOUNTED DOCUMENTARY'
    searchedValue042 = 'BILLS HUNDIES PURCHASED DISCOUNTED CLEAN'
    searchedValue043 = 'UNREALISED INTREST IN SUSPENSE'
    searchedValue044 = 'CREDIT RECOVERIES IN SUSPENSE'
    searchedValue045 = 'PROVISIONS FOR CREDIT LOSSES'
    searchedValue046 = 'ACCRUED INT. ON OUR INVESTMENTS'
    searchedValue047 = 'ACCRUED INTR ON GOVT SECURITEIS'
    searchedValue048 = 'INTEREST RECEIVABLE ON LOANS'
    searchedValue049 = 'BILLS RECEIVABLE BEING BILLS FOR COLLECTION AS PER CONTRA'
    searchedValue050 = 'PREMISES'
    searchedValue051 = 'FURNITURE & FIXTURE'
    searchedValue052 = 'LOCKERS'
    searchedValue053 = 'STRONG ROOM DOOR & VENTILATOR'
    searchedValue054 = 'ELECTRIC EQUIPMENTS'
    searchedValue055 = 'COMPUTER UPS'
    searchedValue056 = 'COMPUTER SOFTWARE'
    searchedValue057 = 'COMPUTER HARDWARE'
    searchedValue058 = 'BI-CYCLE'
    searchedValue059 = 'FIRE EXTINGUSHAR EQUIPMENTS'
    searchedValue060 = 'FAX MACHINE'
    searchedValue061 = 'INVERTER'
    searchedValue062 = 'EPABX SYSTEM'
    searchedValue063 = 'SECURITY ALARM SYSTEM'
    searchedValue064 = 'AIR CONDITIONER LG 4 SPLIT AC'
    searchedValue065 = 'NOTE COUNTING MACHINE'
    searchedValue066 = 'FAKE NOTE DETECTION MACHINE'
    searchedValue067 = 'BRANCH ADJUSTMENT'
    searchedValue068 = 'NON BANKING ASSETS ACQUIRED'

    # anaxure1
    searchedValue001 = 'GRATUTITY FUND'
    searchedValue002 = 'EDUCATION TRAINING'
    searchedValue003 = 'SILVER JUBILEE FUND'
    searchedValue004 = 'DEVELOPMENT FUND'
    searchedValue005 = 'DONATION A/C'
    searchedValue006 = 'INVESTMENT FLUCTUATION'
    searchedValue007 = 'PAT'

    for sh in xlrd.open_workbook('BalanceSheet_31032021.xlsx').sheets():
        if findCell(sh, searchedValue) == -1:
            indiv = 0;
        else:
            indiv = str(findCell(sh, searchedValue).value).replace(',', '')
            indiv = round(float(indiv) / 1000);

        if findCell(sh, searchedValue1) == -1:
            stategv = 0;
        else:
            stategv = str(findCell(sh, searchedValue1).value).replace(',', '')
            stategv = round(float(stategv) / 1000);

        if findCell(sh, searchedValue2) == -1:
            otherpaid = 0;
        else:
            otherpaid = str(findCell(sh, searchedValue2).value).replace(',', '')
            otherpaid = round(float(otherpaid) / 1000);

        paidup = indiv + stategv + otherpaid
        if findCell(sh, searchedValue3) == -1:
            statereserve = 0;
        else:
            statereserve = str(findCell(sh, searchedValue3).value).replace(',', '')
            statereserve = round(float(statereserve) / 1000);
        if findCell(sh, searchedValue4) == -1:
            buildfund = 0;
        else:
            buildfund = str(findCell(sh, searchedValue4).value).replace(',', '')
            buildfund = round(float(buildfund) / 1000);

        if findCell(sh, searchedValue5) == -1:
            dividand = 0;
        else:
            dividand = str(findCell(sh, searchedValue5).value).replace(',', '')
            dividand = round(float(dividand) / 1000);
        if findCell(sh, searchedValue6) == -1:
            revolution = 0;
        else:
            revolution = str(findCell(sh, searchedValue6).value).replace(',', '')
            revolution = round(float(revolution) / 1000);

        if findCell(sh, searchedValue7) == -1:
            provision = 0;
        else:
            provision = str(findCell(sh, searchedValue7).value).replace(',', '')
            provision = round(float(provision) / 1000);

        if findCell(sh, searchedValue8) == -1:
            general = 0;
        else:
            general = str(findCell(sh, searchedValue8).value).replace(',', '')
            general = round(float(general) / 1000);

        if findCell(sh, searchedValue9) == -1:
            gratity = 0;
        else:
            gratity = str(findCell(sh, searchedValue9).value).replace(',', '')
            gratity = round(float(gratity) / 1000);
        if findCell(sh, searchedValue10) == -1:
            staff = 0;
        else:
            staff = str(findCell(sh, searchedValue10).value).replace(',', '')
            staff = round(float(staff) / 1000);
        if findCell(sh, searchedValue11) == -1:
            silver = 0;
        else:
            silver = str(findCell(sh, searchedValue11).value).replace(',', '')
            silver = round(float(silver) / 1000);
        if findCell(sh, searchedValue12) == -1:
            development = 0;
        else:
            development = str(findCell(sh, searchedValue8).value).replace(',', '')
            development = round(float(development) / 1000);
        if findCell(sh, searchedValue13) == -1:
            charity = 0;
        else:
            charity = str(findCell(sh, searchedValue13).value).replace(',', '')
            charity = round(float(charity) / 1000);
        if findCell(sh, searchedValue14) == -1:
            otherli = 0;
        else:
            otherli = str(findCell(sh, searchedValue14).value).replace(',', '')
            otherli = round(float(otherli) / 1000);
        if findCell(sh, searchedValue15) == -1:
            PAT = 0;
        else:
            PAT = str(findCell(sh, searchedValue15).value).replace(',', '')
            PAT = round(float(PAT) / 1000);
        if findCell(sh, searchedValue16) == -1:
            currentyear_surplus = 0;
        else:
            currentyear_surplus = str(findCell(sh, searchedValue16).value).replace(',', '')
            currentyear_surplus = round(float(currentyear_surplus) / 1000);
        if findCell(sh, searchedValue17) == -1:
            currentyear_deficit = 0;
        else:
            currentyear_deficit = str(findCell(sh, searchedValue17).value).replace(',', '')
            currentyear_deficit = round(float(currentyear_deficit) / 1000);

        if findCell(sh, searchedValue18) == -1:
            preyear_surplus = 0;
        else:
            preyear_surplus = str(findCell(sh, searchedValue18).value).replace(',', '')
            preyear_surplus = round(float(preyear_surplus) / 1000);

        if findCell(sh, searchedValue19) == -1:
            prevyear_deficit = 0;
        else:
            prevyear_deficit = str(findCell(sh, searchedValue19).value).replace(',', '')
            prevyear_deficit = round(float(prevyear_deficit) / 1000);

        if findCell(sh, searchedValue20) == -1:
            suboridinet_debt = 0;
        else:
            suboridinet_debt = str(findCell(sh, searchedValue20).value).replace(',', '')
            suboridinet_debt = round(float(suboridinet_debt) / 1000);

        if findCell(sh, searchedValue21) == -1:
            saving = 0;
        else:
            saving = str(findCell(sh, searchedValue21).value).replace(',', '')
            saving = round(float(saving) / 1000);
        if findCell(sh, searchedValue22) == -1:
            saving_bank = 0;
        else:
            saving_bank = str(findCell(sh, searchedValue22).value).replace(',', '')
            saving_bank = round(float(saving_bank) / 1000);
        if findCell(sh, searchedValue23) == -1:
            saving = 0;
        else:
            saving_inopp = str(findCell(sh, searchedValue23).value).replace(',', '')
            saving_inopp = round(float(saving_inopp) / 1000);

        if findCell(sh, searchedValue24) == -1:
            current_depo = 0;
        else:
            current_depo = str(findCell(sh, searchedValue24).value).replace(',', '')
            current_depo = round(float(current_depo) / 1000);
        if findCell(sh, searchedValue25) == -1:
            current_bank = 0;
        else:
            current_bank = str(findCell(sh, searchedValue25).value).replace(',', '')
            current_bank = round(float(current_bank) / 1000);

        if findCell(sh, searchedValue26) == -1:
            fixed_depo = 0;
        else:
            fixed_depo = str(findCell(sh, searchedValue26).value).replace(',', '')
            fixed_depo = float(fixed_depo) / 1000;
        if findCell(sh, searchedValue27) == -1:
            monthly_depo = 0;
        else:
            monthly_depo = str(findCell(sh, searchedValue27).value).replace(',', '')
            monthly_depo = float(monthly_depo) / 1000;

            if findCell(sh, searchedValue28) == -1:
                quarter_depo = 0;
            else:
                quarter_depo = str(findCell(sh, searchedValue28).value).replace(',', '')
                quarter_depo = float(quarter_depo) / 1000;
            if findCell(sh, searchedValue29) == -1:
                reinvestment = 0;
            else:
                reinvestment = str(findCell(sh, searchedValue29).value).replace(',', '')
                reinvestment = float(reinvestment) / 1000;
            if findCell(sh, searchedValue30) == -1:
                recurring = 0;
            else:
                recurring = str(findCell(sh, searchedValue30).value).replace(',', '')
                recurring = float(recurring) / 1000;
            if findCell(sh, searchedValue31) == -1:
                credit_bal = 0;
            else:
                credit_bal = str(findCell(sh, searchedValue31).value).replace(',', '')
                credit_bal = float(credit_bal) / 1000;
            if findCell(sh, searchedValue32) == -1:
                credit_bal_overd = 0;
            else:
                credit_bal_overd = str(findCell(sh, searchedValue32).value).replace(',', '')
                credit_bal_overd = float(credit_bal_overd) / 1000;
            if findCell(sh, searchedValue33) == -1:
                comp_deposit = 0;
            else:
                comp_deposit = str(findCell(sh, searchedValue33).value).replace(',', '')
                comp_deposit = float(comp_deposit) / 1000;

            if findCell(sh, searchedValue34) == -1:
                overdueinterest = 0;
            else:
                overdueinterest = str(findCell(sh, searchedValue34).value).replace(',', '')
                overdueinterest = round(float(overdueinterest) / 1000);
            if findCell(sh, searchedValue35) == -1:
                deposit_interest = 0;
            else:
                deposit_interest = str(findCell(sh, searchedValue35).value).replace(',', '')
                deposit_interest = round(float(deposit_interest) / 1000);
            if findCell(sh, searchedValue36) == -1:
                borrow_interest = 0;
            else:
                borrow_interest = str(findCell(sh, searchedValue36).value).replace(',', '')
                borrow_interest = round(float(borrow_interest) / 1000);
            if findCell(sh, searchedValue37) == -1:
                claim_bank = 0;
            else:
                claim_bank = str(findCell(sh, searchedValue37).value).replace(',', '')
                claim_bank = round(float(claim_bank) / 1000);
            if findCell(sh, searchedValue38) == -1:
                paid_invest = 0;
            else:
                paid_invest = str(findCell(sh, searchedValue38).value).replace(',', '')
                paid_invest = round(float(paid_invest) / 1000);
            if findCell(sh, searchedValue39) == -1:
                credit_docu = 0;
            else:
                credit_docu = str(findCell(sh, searchedValue39).value).replace(',', '')
                credit_docu = round(float(credit_docu) / 1000);
            if findCell(sh, searchedValue40) == -1:
                financial = 0;
            else:
                financial = str(findCell(sh, searchedValue40).value).replace(',', '')
                financial = round(float(financial) / 1000);
            if findCell(sh, searchedValue41) == -1:
                gu_other = 0;
            else:
                gu_other = str(findCell(sh, searchedValue41).value).replace(',', '')
                gu_other = round(float(gu_other) / 1000);
            if findCell(sh, searchedValue42) == -1:
                sales_agree = 0;
            else:
                sales_agree = str(findCell(sh, searchedValue42).value).replace(',', '')
                sales_agree = round(float(sales_agree) / 1000);
            if findCell(sh, searchedValue43) == -1:
                forward_exchange = 0;
            else:
                forward_exchange = str(findCell(sh, searchedValue43).value).replace(',', '')
                forward_exchange = round(float(forward_exchange) / 1000);
            if findCell(sh, searchedValue44) == -1:
                acceptances = 0;
            else:
                acceptances = str(findCell(sh, searchedValue44).value).replace(',', '')
                acceptances = round(float(acceptances) / 1000);
            if findCell(sh, searchedValue45) == -1:
                other = 0
            else:
                other = str(findCell(sh, searchedValue45).value).replace(',', '')
                other = round(float(other) / 1000);
            if findCell(sh, searchedValue46) == -1:
                investment = 0;
            else:
                investment = str(findCell(sh, searchedValue46).value).replace(',', '')
                investment = round(float(investment) / 1000);
            if findCell(sh, searchedValue47) == -1:
                depreciation = 0;
            else:
                depreciation = str(findCell(sh, searchedValue47).value).replace(',', '')
                depreciation = round(float(depreciation) / 1000);
            if findCell(sh, searchedValue48) == -1:
                impariedasset = 0
            else:
                impariedasset = str(findCell(sh, searchedValue48).value).replace(',', '')
                impariedasset = round(float(impariedasset) / 1000);
            if findCell(sh, searchedValue49) == -1:
                contigent = 0
            else:
                contigent = str(findCell(sh, searchedValue49).value).replace(',', '')
                contigent = round(float(contigent) / 1000);
            if findCell(sh, searchedValue50) == -1:
                assetsreserve = 0
            else:
                assetsreserve = str(findCell(sh, searchedValue50).value).replace(',', '')
                assetsreserve = round(float(assetsreserve) / 1000);
            if findCell(sh, searchedValue51) == -1:
                BDDR = 0
            else:
                BDDR = str(findCell(sh, searchedValue51).value).replace(',', '')
                BDDR = round(float(BDDR) / 1000);
            if findCell(sh, searchedValue52) == -1:
                BDDRspe = 0
            else:
                BDDRspe = str(findCell(sh, searchedValue52).value).replace(',', '')
                BDDRspe = round(float(BDDRspe) / 1000);


            # assets

            if findCell(sh, searchedValue00) == -1:
                cash_ih_hand = 0;
            else:
                cash_ih_hand = str(findCell(sh, searchedValue00).value).replace(',', '')
                cash_ih_hand = round(float(cash_ih_hand) / 1000);

            if findCell(sh, searchedValue01) == -1:
                sbi_current_ac = 0;
            else:
                sbi_current_ac = str(findCell(sh, searchedValue01).value).replace(',', '')
                sbi_current_ac = round(float(sbi_current_ac) / 1000);

            if findCell(sh, searchedValue02) == -1:
                sbi_saving_ac = 0;
            else:
                sbi_saving_ac = str(findCell(sh, searchedValue02).value).replace(',', '')
                sbi_saving_ac = round(float(sbi_saving_ac) / 1000);

            if findCell(sh, searchedValue03) == -1:
                sbi_fd = 0;
            else:
                sbi_fd = str(findCell(sh, searchedValue03).value).replace(',', '')
                sbi_fd = round(float(sbi_fd) / 1000);

            if findCell(sh, searchedValue04) == -1:
                rbi_ca = 0;
            else:
                rbi_ca = str(findCell(sh, searchedValue04).value).replace(',', '')
                rbi_ca = round(float(rbi_ca) / 1000);

            if findCell(sh, searchedValue05) == -1:
                rbi_others = 0;
            else:
                rbi_others = str(findCell(sh, searchedValue05).value).replace(',', '')
                rbi_others = round(float(rbi_others) / 1000);

            if findCell(sh, searchedValue06) == -1:
                centralcoop_current_ac = 0;
            else:
                centralcoop_current_ac = str(findCell(sh, searchedValue06).value).replace(',', '')
                centralcoop_current_ac = round(float(centralcoop_current_ac) / 1000);

            if findCell(sh, searchedValue07) == -1:
                centralcoop_saving_ac = 0;
            else:
                centralcoop_saving_ac = str(findCell(sh, searchedValue07).value).replace(',', '')
                centralcoop_saving_ac = round(float(centralcoop_saving_ac) / 1000);

            if findCell(sh, searchedValue08) == -1:
                centralcoop_fd = 0;
            else:
                centralcoop_fd = str(findCell(sh, searchedValue08).value).replace(',', '')
                centralcoop_fd = round(float(centralcoop_fd) / 1000);

            if findCell(sh, searchedValue09) == -1:
                call_short_notice_money_cooperative = 0;
            else:
                call_short_notice_money_cooperative = str(findCell(sh, searchedValue09).value).replace(',', '')
                call_short_notice_money_cooperative = round(float(call_short_notice_money_cooperative) / 1000);

            if findCell(sh, searchedValue010) == -1:
                call_short_notice_money_others = 0;
            else:
                call_short_notice_money_others = str(findCell(sh, searchedValue010).value).replace(',', '')
                call_short_notice_money_others = round(float(call_short_notice_money_others) / 1000);

            if findCell(sh, searchedValue011) == -1:
                loan_advances_to_scheduled_cooperative = 0;
            else:
                loan_advances_to_scheduled_cooperative = str(findCell(sh, searchedValue011).value).replace(',', '')
                loan_advances_to_scheduled_cooperative = round(float(loan_advances_to_scheduled_cooperative) / 1000);

            if findCell(sh, searchedValue012) == -1:
                loan_advances_to_nonscheduled_cooperative = 0;
            else:
                loan_advances_to_nonscheduled_cooperative = str(findCell(sh, searchedValue012).value).replace(',', '')
                loan_advances_to_nonscheduled_cooperative = round(
                    float(loan_advances_to_nonscheduled_cooperative) / 1000);

            if findCell(sh, searchedValue013) == -1:
                loan_advances_to_other = 0;
            else:
                loan_advances_to_other = str(findCell(sh, searchedValue013).value).replace(',', '')
                loan_advances_to_other = round(float(loan_advances_to_other) / 1000);

            if findCell(sh, searchedValue014) == -1:
                hdfc_current_ac = 0;
            else:
                hdfc_current_ac = str(findCell(sh, searchedValue014).value).replace(',', '')
                hdfc_current_ac = round(float(hdfc_current_ac) / 1000);

            if findCell(sh, searchedValue0014) == -1:
                axis_current_ac = 0;
            else:
                axis_current_ac = str(findCell(sh, searchedValue0014).value).replace(',', '')
                axis_current_ac = round(float(axis_current_ac) / 1000);

            if findCell(sh, searchedValue00014) == -1:
                ICICI_current_ac = 0;
            else:
                ICICI_current_ac = str(findCell(sh, searchedValue00014).value).replace(',', '')
                ICICI_current_ac = round(float(ICICI_current_ac) / 1000);

            if findCell(sh, searchedValue015) == -1:
                hdfc_fd = 0;
            else:
                hdfc_fd = str(findCell(sh, searchedValue015).value).replace(',', '')
                hdfc_fd = round(float(hdfc_fd) / 1000);

            if findCell(sh, searchedValue0015) == -1:
                dcb_bank_fd = 0;
            else:
                dcb_bank_fd = str(findCell(sh, searchedValue0015).value).replace(',', '')
                dcb_bank_fd = round(float(dcb_bank_fd) / 1000);

            if findCell(sh, searchedValue00015) == -1:
                shamrao_vithal_fd = 0;
            else:
                shamrao_vithal_fd = str(findCell(sh, searchedValue00015).value).replace(',', '')
                shamrao_vithal_fd = round(float(shamrao_vithal_fd) / 1000);

            if findCell(sh, searchedValue000015) == -1:
                equitas_fd = 0;
            else:
                equitas_fd = str(findCell(sh, searchedValue000015).value).replace(',', '')
                equitas_fd = round(float(equitas_fd) / 1000);

            if findCell(sh, searchedValue0000015) == -1:
                suryoday_fd = 0;
            else:
                suryoday_fd = str(findCell(sh, searchedValue0000015).value).replace(',', '')
                suryoday_fd = round(float(suryoday_fd) / 1000);

            if findCell(sh, searchedValue00000015) == -1:
                fincare_fd = 0;
            else:
                fincare_fd = str(findCell(sh, searchedValue00000015).value).replace(',', '')
                fincare_fd = round(float(fincare_fd) / 1000);

            if findCell(sh, searchedValue000000015) == -1:
                jana_fd = 0;
            else:
                jana_fd = str(findCell(sh, searchedValue000000015).value).replace(',', '')
                jana_fd = round(float(jana_fd) / 1000);

            if findCell(sh, searchedValue0000000015) == -1:
                idfc_fd = 0;
            else:
                idfc_fd = str(findCell(sh, searchedValue0000000015).value).replace(',', '')
                idfc_fd = round(float(idfc_fd) / 1000);

            if findCell(sh, searchedValue00000000015) == -1:
                utkarsh_fd = 0;
            else:
                utkarsh_fd = str(findCell(sh, searchedValue00000000015).value).replace(',', '')
                utkarsh_fd = round(float(utkarsh_fd) / 1000);

            if findCell(sh, searchedValue016) == -1:
                due_from_other_institutions_others = 0;
            else:
                due_from_other_institutions_others = str(findCell(sh, searchedValue016).value).replace(',', '')
                due_from_other_institutions_others = round(float(due_from_other_institutions_others) / 1000);

            if findCell(sh, searchedValue017) == -1:
                Goi_t_bills = 0;
            else:
                Goi_t_bills = str(findCell(sh, searchedValue017).value).replace(',', '')
                Goi_t_bills = round(float(Goi_t_bills) / 1000);

            if findCell(sh, searchedValue018) == -1:
                GOI_Securities = 0;
            else:
                GOI_Securities = str(findCell(sh, searchedValue018).value).replace(',', '')
                GOI_Securities = round(float(GOI_Securities) / 1000);

            if findCell(sh, searchedValue019) == -1:
                State_Government_Securities = 0;
            else:
                State_Government_Securities = str(findCell(sh, searchedValue019).value).replace(',', '')
                State_Government_Securities = round(float(State_Government_Securities) / 1000);

            if findCell(sh, searchedValue020) == -1:
                other_trustee = 0;
            else:
                other_trustee = str(findCell(sh, searchedValue020).value).replace(',', '')
                other_trustee = round(float(other_trustee) / 1000);

            if findCell(sh, searchedValue021) == -1:
                non_slr_investment_liquid = 0;
            else:
                non_slr_investment_liquid = str(findCell(sh, searchedValue021).value).replace(',', '')
                non_slr_investment_liquid = round(float(non_slr_investment_liquid) / 1000);

            if findCell(sh, searchedValue022) == -1:
                non_slr_investment_bond = 0;
            else:
                non_slr_investment_bond = str(findCell(sh, searchedValue022).value).replace(',', '')
                non_slr_investment_bond = round(float(non_slr_investment_bond) / 1000);

            if findCell(sh, searchedValue023) == -1:
                investment_in_Subsidiaries = 0;
            else:
                investment_in_Subsidiaries = str(findCell(sh, searchedValue023).value).replace(',', '')
                investment_in_Subsidiaries = round(float(investment_in_Subsidiaries) / 1000);

            if findCell(sh, searchedValue024) == -1:
                shares_cooperative_institute = 0;
            else:
                shares_cooperative_institute = str(findCell(sh, searchedValue024).value).replace(',', '')
                shares_cooperative_institute = round(float(shares_cooperative_institute) / 1000);

            if findCell(sh, searchedValue025) == -1:
                shares_of_all_india = 0;
            else:
                shares_of_all_india = str(findCell(sh, searchedValue025).value).replace(',', '')
                shares_of_all_india = round(float(shares_of_all_india) / 1000);

            if findCell(sh, searchedValue026) == -1:
                unit_of_mutual_fund = 0;
            else:
                unit_of_mutual_fund = str(findCell(sh, searchedValue026).value).replace(',', '')
                unit_of_mutual_fund = round(float(unit_of_mutual_fund) / 1000);

            if findCell(sh, searchedValue027) == -1:
                bond_of_psu = 0;
            else:
                bond_of_psu = str(findCell(sh, searchedValue027).value).replace(',', '')
                bond_of_psu = round(float(bond_of_psu) / 1000);

            if findCell(sh, searchedValue028) == -1:
                Other_State_Government_Securities = 0;
            else:
                Other_State_Government_Securities = str(findCell(sh, searchedValue028).value).replace(',', '')
                Other_State_Government_Securities = round(float(Other_State_Government_Securities) / 1000);

            if findCell(sh, searchedValue029) == -1:
                loan_against_fd = 0;
            else:
                loan_against_fd = str(findCell(sh, searchedValue029).value).replace(',', '')
                loan_against_fd = float(loan_against_fd) / 1000;
                print("LOANS AHIA FD",loan_against_fd);

            if findCell(sh, searchedValue030) == -1:
                overdraft_gold_loan = 0;
            else:
                overdraft_gold_loan = str(findCell(sh, searchedValue030).value).replace(',', '')
                overdraft_gold_loan =float(overdraft_gold_loan) / 1000;

            if findCell(sh, searchedValue031) == -1:
                gold_loan = 0;
            else:
                gold_loan = str(findCell(sh, searchedValue031).value).replace(',', '')
                gold_loan = float(gold_loan) / 1000;

            if findCell(sh, searchedValue032) == -1:
                unsecured_short_terms_loan = 0;
            else:
                unsecured_short_terms_loan = str(findCell(sh, searchedValue032).value).replace(',', '')
                unsecured_short_terms_loan = round(float(unsecured_short_terms_loan) / 1000);

            if findCell(sh, searchedValue033) == -1:
                cash_credit = 0;
            else:
                cash_credit = str(findCell(sh, searchedValue033).value).replace(',', '')
                cash_credit = float(cash_credit) / 1000;

            if findCell(sh, searchedValue034) == -1:
                over_draft = 0;
            else:
                over_draft = str(findCell(sh, searchedValue034).value).replace(',', '')
                over_draft = float(over_draft) / 1000;

            if findCell(sh, searchedValue035) == -1:
                over_draft_mortgage = 0;
            else:
                over_draft_mortgage = str(findCell(sh, searchedValue035).value).replace(',', '')
                over_draft_mortgage = float(over_draft_mortgage) / 1000;

            if findCell(sh, searchedValue036) == -1:
                unsecured_cashcredits_overdrafts = 0;
            else:
                unsecured_cashcredits_overdrafts = str(findCell(sh, searchedValue036).value).replace(',', '')
                unsecured_cashcredits_overdrafts = round(float(unsecured_cashcredits_overdrafts) / 1000);

            if findCell(sh, searchedValue037) == -1:
                medium_term_secure_loan = 0;
            else:
                medium_term_secure_loan = str(findCell(sh, searchedValue037).value).replace(',', '')
                medium_term_secure_loan = float(medium_term_secure_loan) / 1000;

            if findCell(sh, searchedValue038) == -1:
                medium_term_unsecure_loan = 0;
            else:
                medium_term_unsecure_loan = str(findCell(sh, searchedValue038).value).replace(',', '')
                medium_term_unsecure_loan = float(medium_term_unsecure_loan) / 1000;

            if findCell(sh, searchedValue039) == -1:
                long_term_secure_loan = 0;
            else:
                long_term_secure_loan = str(findCell(sh, searchedValue039).value).replace(',', '')
                long_term_secure_loan = round(float(long_term_secure_loan) / 1000);

            if findCell(sh, searchedValue040) == -1:
                long_term_unsecure_loan = 0;
            else:
                long_term_unsecure_loan = str(findCell(sh, searchedValue040).value).replace(',', '')
                long_term_unsecure_loan = round(float(long_term_unsecure_loan) / 1000);

            if findCell(sh, searchedValue041) == -1:
                bills_documentary = 0;
            else:
                bills_documentary = str(findCell(sh, searchedValue041).value).replace(',', '')
                bills_documentary = round(float(bills_documentary) / 1000);

            if findCell(sh, searchedValue042) == -1:
                bills_clean = 0;
            else:
                bills_clean = str(findCell(sh, searchedValue042).value).replace(',', '')
                bills_clean = round(float(bills_clean) / 1000);

            if findCell(sh, searchedValue043) == -1:
                unrealised_suspense = 0;
            else:
                unrealised_suspense = str(findCell(sh, searchedValue043).value).replace(',', '')
                unrealised_suspense = round(float(unrealised_suspense) / 1000);

            if findCell(sh, searchedValue044) == -1:
                credit_recoveries = 0;
            else:
                credit_recoveries = str(findCell(sh, searchedValue044).value).replace(',', '')
                credit_recoveries = round(float(credit_recoveries) / 1000);

            if findCell(sh, searchedValue045) == -1:
                provisions_credit_loss = 0;
            else:
                provisions_credit_loss = str(findCell(sh, searchedValue045).value).replace(',', '')
                provisions_credit_loss = round(float(provisions_credit_loss) / 1000);

            if findCell(sh, searchedValue046) == -1:
                accured_investments = 0;
            else:
                accured_investments = str(findCell(sh, searchedValue046).value).replace(',', '')
                accured_investments = float(accured_investments) / 1000;

            if findCell(sh, searchedValue047) == -1:
                accured_securities = 0;
            else:
                accured_securities = str(findCell(sh, searchedValue047).value).replace(',', '')
                accured_securities = float(accured_securities) / 1000;

            if findCell(sh, searchedValue048) == -1:
                loans_and_advances = 0;
            else:
                loans_and_advances = str(findCell(sh, searchedValue048).value).replace(',', '')
                loans_and_advances = float(loans_and_advances) / 1000;

            if findCell(sh, searchedValue049) == -1:
                bills_receivable = 0;
            else:
                bills_receivable = str(findCell(sh, searchedValue049).value).replace(',', '')
                bills_receivable = round(float(bills_receivable) / 1000);

            if findCell(sh, searchedValue050) == -1:
                premises = 0;
            else:
                premises = str(findCell(sh, searchedValue050).value).replace(',', '')
                premises = round(float(premises) / 1000);

            if findCell(sh, searchedValue051) == -1:
                furniture_fixture = 0;
            else:
                furniture_fixture = str(findCell(sh, searchedValue051).value).replace(',', '')
                furniture_fixture = float(furniture_fixture) / 1000;

            if findCell(sh, searchedValue052) == -1:
                LOCKERS = 0;
            else:
                LOCKERS = str(findCell(sh, searchedValue052).value).replace(',', '')
                LOCKERS = float(LOCKERS) / 1000;

            if findCell(sh, searchedValue053) == -1:
                strong_room_door = 0;
            else:
                strong_room_door = str(findCell(sh, searchedValue053).value).replace(',', '')
                strong_room_door = float(strong_room_door) / 1000;

            if findCell(sh, searchedValue054) == -1:
                electric_equipments = 0;
            else:
                electric_equipments = str(findCell(sh, searchedValue054).value).replace(',', '')
                electric_equipments = float(electric_equipments) / 1000;

            if findCell(sh, searchedValue055) == -1:
                computer_ups = 0;
            else:
                computer_ups = str(findCell(sh, searchedValue055).value).replace(',', '')
                computer_ups = float(computer_ups) / 1000;

            if findCell(sh, searchedValue056) == -1:
                computer_software = 0;
            else:
                computer_software = str(findCell(sh, searchedValue056).value).replace(',', '')
                computer_software = float(computer_software) / 1000;

            if findCell(sh, searchedValue057) == -1:
                computer_hardware = 0;
            else:
                computer_hardware = str(findCell(sh, searchedValue057).value).replace(',', '')
                computer_hardware = float(computer_hardware) / 1000;

            if findCell(sh, searchedValue058) == -1:
                by_cycle = 0;
            else:
                by_cycle = str(findCell(sh, searchedValue058).value).replace(',', '')
                by_cycle = float(by_cycle) / 1000;

            if findCell(sh, searchedValue059) == -1:
                fire = 0;
            else:
                fire = str(findCell(sh, searchedValue059).value).replace(',', '')
                fire =float(fire) / 1000;

            if findCell(sh, searchedValue060) == -1:
                fax_machine = 0;
            else:
                fax_machine = str(findCell(sh, searchedValue060).value).replace(',', '')
                fax_machine = float(fax_machine) / 1000;

            if findCell(sh, searchedValue061) == -1:
                INVERTER = 0;
            else:
                INVERTER = str(findCell(sh, searchedValue061).value).replace(',', '')
                INVERTER = float(INVERTER) / 1000;

            if findCell(sh, searchedValue062) == -1:
                EPABX = 0;
            else:
                EPABX = str(findCell(sh, searchedValue062).value).replace(',', '')
                EPABX = float(EPABX) / 1000;

            if findCell(sh, searchedValue063) == -1:
                Security = 0;
            else:
                Security = str(findCell(sh, searchedValue063).value).replace(',', '')
                Security = float(Security) / 1000;

            if findCell(sh, searchedValue064) == -1:
                ac_lg = 0;
            else:
                ac_lg = str(findCell(sh, searchedValue064).value).replace(',', '')
                ac_lg = float(ac_lg) / 1000;

            if findCell(sh, searchedValue065) == -1:
                note_counting_machine = 0;
            else:
                note_counting_machine = str(findCell(sh, searchedValue065).value).replace(',', '')
                note_counting_machine = float(note_counting_machine) / 1000;

            if findCell(sh, searchedValue066) == -1:
                fake_note_detecting_machine = 0;
            else:
                fake_note_detecting_machine = str(findCell(sh, searchedValue066).value).replace(',', '')
                fake_note_detecting_machine = float(fake_note_detecting_machine) / 1000;

            if findCell(sh, searchedValue067) == -1:
                branch_adjusment = 0;
            else:
                branch_adjusment = str(findCell(sh, searchedValue067).value).replace(',', '')
                branch_adjusment = round(float(branch_adjusment) / 1000);
            if findCell(sh, searchedValue068) == -1:
                non_banking = 0;
            else:
                non_banking = str(findCell(sh, searchedValue068).value).replace(',', '')
                non_banking = round(float(non_banking) / 1000);

            # anxure1
            if findCell(sh, searchedValue001) == -1:
                gratutiyfund = 0;
            else:
                gratutiyfund = str(findCell(sh, searchedValue001).value).replace(',', '')
                gratutiyfund = round(float(gratutiyfund) / 1000);

            if findCell(sh, searchedValue002) == -1:
                staffwalfare = 0;
            else:
                staffwalfare = str(findCell(sh, searchedValue002).value).replace(',', '')
                staffwalfare = round(float(staffwalfare) / 1000);
            if findCell(sh, searchedValue003) == -1:
                silverjubilee = 0;
            else:
                silverjubilee = str(findCell(sh, searchedValue003).value).replace(',', '')
                silverjubilee = round(float(silverjubilee) / 1000);
            if findCell(sh, searchedValue004) == -1:
                developmentfund = 0;
            else:
                developmentfund = str(findCell(sh, searchedValue004).value).replace(',', '')
                developmentfund = round(float(developmentfund) / 1000);
            if findCell(sh, searchedValue005) == -1:
                charityfund = 0;
            else:
                charityfund = str(findCell(sh, searchedValue005).value).replace(',', '')
                charityfund = round(float(charityfund) / 1000);
            if findCell(sh, searchedValue006) == -1:
                otherfund_ = 0;
            else:
                otherfund_ = str(findCell(sh, searchedValue006).value).replace(',', '')

                otherfund_ = round(float(otherfund_) / 1000);
            if findCell(sh, searchedValue007) == -1:
                pat = 0;
            else:
                pat = str(findCell(sh, searchedValue007).value).replace(',', '')
                pat = round(float(pat) / 1000);

    otherfund = gratity + staff + silver + development + charity + otherli + PAT
    reservefund = statereserve + buildfund + dividand + revolution + provision + general + otherfund
    totalprofitloss = currentyear_surplus + currentyear_deficit + preyear_surplus + prevyear_deficit
    totalcapitalreserve = paidup + reservefund + totalprofitloss
    savingdepodit = saving + saving_inopp + saving_bank
    currentbankdeposit = current_bank + current_depo
    # print(fixed_depo," ",monthly_depo," ",quarter_depo," ",reinvestment," ",recurring," ",credit_bal," ",credit_bal_overd,"  ",comp_deposit)
    termdeposit = round(
        fixed_depo + monthly_depo + quarter_depo + reinvestment + recurring + credit_bal + credit_bal_overd + comp_deposit)
    residentDeposit = termdeposit + currentbankdeposit + savingdepodit
    interest_payable = deposit_interest + borrow_interest
    contigentlib = claim_bank + paid_invest + credit_docu + financial + gu_other + sales_agree + forward_exchange + acceptances + other;
    print(assetsreserve, " ", BDDR, " ", BDDRspe);
    Bddr_sp = assetsreserve + BDDR + BDDRspe;
    riskpro = Bddr_sp + investment + depreciation + impariedasset + contigent

    # assets

    sbi_and_other_notified_banks = sbi_current_ac + sbi_saving_ac + sbi_fd
    RBI = rbi_ca + rbi_others
    State_Central_Cooperative_Bank_of_the_State_District_concerned = centralcoop_current_ac + centralcoop_saving_ac + centralcoop_fd
    Balances_with_Banks = State_Central_Cooperative_Bank_of_the_State_District_concerned + RBI + sbi_and_other_notified_banks
    Loans_and_Advances_to_Banks_including_bills = call_short_notice_money_cooperative + call_short_notice_money_others + loan_advances_to_scheduled_cooperative + loan_advances_to_nonscheduled_cooperative + loan_advances_to_other
    Due_from_banks = Balances_with_Banks + Loans_and_Advances_to_Banks_including_bills
    due_from_other_institutions_ca = hdfc_current_ac + axis_current_ac + ICICI_current_ac
    due_from_other_institutions_fixed = hdfc_fd+dcb_bank_fd+shamrao_vithal_fd+equitas_fd+ suryoday_fd + fincare_fd + jana_fd + idfc_fd + utkarsh_fd
    Due_from_other_institutions = due_from_other_institutions_ca + due_from_other_institutions_fixed + due_from_other_institutions_others
    SLR_Investments = Goi_t_bills + GOI_Securities + State_Government_Securities + other_trustee
    Other_Investment = non_slr_investment_liquid + non_slr_investment_bond
    Equities_Units_of_Mutual_Funds = shares_cooperative_institute + shares_of_all_india + unit_of_mutual_fund
    Other_Debt_Securitie = Other_State_Government_Securities + bond_of_psu
    Non_SLR_Investments = Other_Debt_Securitie + Equities_Units_of_Mutual_Funds + investment_in_Subsidiaries + Other_Investment
    Slr_Nonslr_investments = SLR_Investments+Non_SLR_Investments
    print("SECURE SHORT ",loan_against_fd,"  === ",overdraft_gold_loan," ==== ",gold_loan)
    Short_term_secure_loans =round(loan_against_fd + overdraft_gold_loan + gold_loan)
    Short_terms_loans = round(Short_term_secure_loans + unsecured_short_terms_loan)
    Secure_cash_credit_overdraft = round(cash_credit + over_draft + over_draft_mortgage)
    Cash_credit_overdrafts = round(Secure_cash_credit_overdraft + unsecured_cashcredits_overdrafts)
    Medium_terms_loans = round(medium_term_secure_loan + medium_term_unsecure_loan)

    Long_terms_loans = long_term_secure_loan + long_term_unsecure_loan
    Bills = bills_documentary + bills_clean
    Gross_Loans_and_Advances = Short_terms_loans + Cash_credit_overdrafts + Medium_terms_loans + Long_terms_loans + Bills
    Netting_items_on_loans_advances = unrealised_suspense + credit_recoveries + provisions_credit_loss

    Investments = round(accured_investments + accured_securities)
    print("FGN+", accured_investments, " ", accured_securities," ",Investments)
    Interest_Receivable_on = round(Investments + loans_and_advances)
    furniture_and_fixture = round(furniture_fixture + LOCKERS + strong_room_door + electric_equipments + computer_ups + computer_software + computer_hardware + by_cycle + fire + fax_machine + INVERTER + EPABX + Security + ac_lg + note_counting_machine + fake_note_detecting_machine)

    # annuxurw
    print("OTHERRFUND=================", otherfund);
    totalofannaxure1 = gratutiyfund + staffwalfare + silverjubilee + developmentfund + charityfund + otherfund_ + pat;

    x = {
        "LIABILITIES+++++++++++++++++++++++++++++++++++++++++++++++++++++": str("++++++++"),
        "Individual": str(indiv),
        "Stategv": str(stategv),
        "Otherpaidup": str(otherpaid),
        "Totalpaid": str(paidup),
        "ReserveFund": str(reservefund),
        "StatutoryReserve": str(statereserve),
        "BuildingFund": str(buildfund),
        "DividandFund": str(dividand),
        "RevolutionFund": str(revolution),
        "ProvisionalFund": str(provision),
        "GeneralProvisionalFund": str(general),
        "OtherFund": str(otherfund),
        "profit/loss": str(totalprofitloss),
        "Surplus_current": str(currentyear_surplus),
        "Deficit_current": str(currentyear_deficit),
        "Surplus_previous": str(preyear_surplus),
        "Deficit_previous": str(prevyear_deficit),
        "totalcapital_reserve": str(totalcapitalreserve),
        "suboridinet_debt": str(suboridinet_debt),
        "Customerdeposit": str(residentDeposit),
        "Residentdeposit": str(residentDeposit),
        "Term_deposit": str(termdeposit),
        "Saving_bank_deposit": str(savingdepodit),
        "Current_bank_deposit": str(currentbankdeposit),
        "Overdure_interest_rate": str(overdueinterest),
        "Interest_payable": str(interest_payable),
        "deposit": str(deposit_interest),
        "borrow": str(borrow_interest),
        "riskprovisions": str(riskpro),
        "forinvestment": str(investment),
        "BDDR": str(Bddr_sp),
        "depreciation": str(depreciation),
        "otherimpaired": str(impariedasset),
        "contingent": str(contigent),
        "contigentliabilities": str(contigentlib),
        "Claimagianstbank": str(claim_bank),
        "paidinvestment": str(paid_invest),
        "creditdocument": str(credit_docu),
        "finacial": str(financial),
        "other_guarantee": str(gu_other),
        "salesandrepurchase": str(sales_agree),
        "forwardexchange": str(forward_exchange),
        "acceptances": str(acceptances),
        "others": str(other),
        "ASSETSSS+++++++++++++++++++++++++++++++++++++++++++++++++++++": str("++++++++"),

        # assets
        # ASSETS
        "cashinhand": str(cash_ih_hand),
        "Sbi(current_ac)": str(sbi_current_ac),
        "Sbi(saving_ac)": str(sbi_saving_ac),
        "Sbi(fd)": str(sbi_fd),
        "SBI_and_other_notified_banks": str(sbi_and_other_notified_banks),
        "RBI_current_ac": str(rbi_ca),
        "RBI_Others": str(rbi_others),
        "RBI": str(RBI),
        "Central(current_ac)": str(centralcoop_current_ac),
        "Central(saving_ac)": str(centralcoop_saving_ac),
        "Central(fd)": str(centralcoop_fd),
        "State_Central_Cooperative_Bank_of_the_State_District_concerned": str(
            State_Central_Cooperative_Bank_of_the_State_District_concerned),
        "Balances_with_Banks": str(Balances_with_Banks),
        "Call_and_Short_Notice_Money_to_Cooperative_Banks": str(call_short_notice_money_cooperative),
        "Call_and_Short_Notice_Money_to_Other_Banks": str(call_short_notice_money_others),
        "Loans_and_Advances_to_Scheduled_Cooperative_Banks": str(loan_advances_to_scheduled_cooperative),
        "Loans_and_Advances_to_NonScheduled_Cooperative_Banks": str(loan_advances_to_nonscheduled_cooperative),
        "Loans_and_Advances_to_Other_Banks": str(loan_advances_to_other),
        "Loans_and_Advances_to_Banks_(including_bills)": str(Loans_and_Advances_to_Banks_including_bills),
        "Due_from_banks": str(Due_from_banks),
        "Due_from_other_institutions_current": str(due_from_other_institutions_ca),
        "Due_from_other_institutions_fixed": str(due_from_other_institutions_fixed),
        "Due_from_other_institutions_others": str(due_from_other_institutions_others),
        "Due_from_other_institutions": str(Due_from_other_institutions),
        "GOI_T_Bills": str(Goi_t_bills),
        "GOI_Securities": str(GOI_Securities),
        "State_Government_Securities": str(State_Government_Securities),
        "Other_trustee_approved_securities": str(other_trustee),
        "SLR_Investments": str(SLR_Investments),
        "Other_Investment": str(Other_Investment),
        "Investment_Subsidiaries": str(investment_in_Subsidiaries),
        "shares_cooperative_institute": str(shares_cooperative_institute),
        "shares_of_all_india": str(shares_of_all_india),
        "unit_of_mutual_fund": str(unit_of_mutual_fund),
        "Equities_Units_of_Mutual_Funds": str(Equities_Units_of_Mutual_Funds),
        "Other Debt Securities ": str(Other_Debt_Securitie),
        "Other State Government Securities": str(Other_State_Government_Securities),
        "Bonds of PSUs / All India Financial Institutions": str(bond_of_psu),
        "NON_SLR_Investments": str(Non_SLR_Investments),
        "Slr_Nonslr_investments": str(Slr_Nonslr_investments),
        "Secured_short_term_loans": str(Short_term_secure_loans),
        "Unsecured_short_term_loan": str(unsecured_short_terms_loan),
        "Short_term_loans": str(Short_terms_loans),
        "Secure_cash_credit_overdraft": str(Secure_cash_credit_overdraft),
        "Unsecured_cashcredits_overdrafts": str(unsecured_cashcredits_overdrafts),
        "Cash_credit_overdrafts": str(Cash_credit_overdrafts),
        "Medium_term_secure_loan": str(round(medium_term_secure_loan)),
        "Medium_term_unsecure_loan": str(int(medium_term_unsecure_loan)),
        "Medium_term_loans": str(Medium_terms_loans),
        "Long_term_secure_loan": str(long_term_secure_loan),
        "Long_term_unsecure_loan": str(long_term_unsecure_loan),
        "Long_term_loan": str(Long_terms_loans),
        "Bills_documentary": str(bills_documentary),
        "Bills_clean": str(bills_clean),
        "Bills": str(Bills),
        "Gross_Loans_and_Advances": str(Gross_Loans_and_Advances),
        "Loans and Advances": str(Gross_Loans_and_Advances),
        "unrealised_suspense": str(unrealised_suspense),
        "credit_recoveries": str(credit_recoveries),
        "provisions_credit_loss": str(provisions_credit_loss),
        "Netting_items_on_loans_advances": str(Netting_items_on_loans_advances),
        "Loans and Advances(Net)": str(Gross_Loans_and_Advances),
        "Investments": str(Investments),
        "Loans_and_Advances": str(round(loans_and_advances)),
        "Interest_Receivable_on": str(Interest_Receivable_on),
        "Bills_receivable": str(bills_receivable),
        "Premises": str(premises),
        "Furniture_fixture": str(furniture_and_fixture),
        "Branch_adjusment": str(branch_adjusment),
        "non_banking_assets": str(non_banking),
    #anaxure1
        "ANAXURE1+++++++++++++++++++++++++++++++++++++++++++++++++++++": str("++++++++"),
        "Gratuityfund": str(gratutiyfund),
        "staffwalfarefund": str(staffwalfare),
        "silverjubilee": str(silverjubilee),
        "development": str(developmentfund),
        "charity": str(charityfund),
        "otherfund": str(otherfund_),
        "pat": str(pat),
        "total": str(totalofannaxure1),
    }

    print(json.dumps(x))
    return json.dumps(x), headers
    input('Press ENTER to exit')


if __name__ == '__main__':
    app.run()
