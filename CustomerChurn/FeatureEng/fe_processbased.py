'''
JMJPFU
22-Jan-2020
This script is for process based feature engineering. In this scripts different processes specific to project will be defined
'''


class FeProcess:
    def __init__(self,dataFrame):
        self.dataFrame = dataFrame

    def process1(self):
        ## Step 1 : New column created by multiplying total recharge data with average recharge amount for the month
        self.dataFrame['total_rech_6'] = self.dataFrame.total_rech_data_6 * self.dataFrame.av_rech_amt_data_6
        self.dataFrame['total_rech_7'] = self.dataFrame.total_rech_data_7 * self.dataFrame.av_rech_amt_data_7

        ## Step 2 : New Column : Recharge amount > Total recharge + Total recharge of data

        self.dataFrame['amt_6'] = self.dataFrame.total_rech_amt_6 + self.dataFrame.total_rech_6
        self.dataFrame['amt_7'] = self.dataFrame.total_rech_amt_7 + self.dataFrame.total_rech_7

        ## Step 3 : New column : Average recharge amount for month 6 and 7

        self.dataFrame['avg_amt_6_7'] = (self.dataFrame['amt_6'] + self.dataFrame['amt_7']) / 2

        ## Printing 70th percentile data for the average amount

        print('Recharge amount at 70th percentile : {0}'.format(self.dataFrame.avg_amt_6_7.quantile(0.7)))

        # Step 4 : Finding those examples who are higher than the 70th percentile data

        # retain only those customers who have recharged their mobiles with more than or equal to 70th percentile amount

        dataFiltered = self.dataFrame.loc[self.dataFrame.avg_amt_6_7 >= self.dataFrame.avg_amt_6_7.quantile(0.7),:]
        dataFiltered = dataFiltered.reset_index(drop=True)

        # Dropping extra features created
        dataFiltered = dataFiltered.drop(['total_rech_6','total_rech_7','amt_6','amt_7','avg_amt_6_7'],axis=1)
        print('Shape of the data set after filtering', dataFiltered.shape)
        return dataFiltered
    def process2(self):
        # Compute the total incoming and outgoing usage
        self.dataFrame['Total_calls_9'] = self.dataFrame.total_ic_mou_9 + self.dataFrame.total_og_mou_9
        # Calculate total 2g and 3g data consumption
        self.dataFrame['Total_data_9'] = self.dataFrame.vol_2g_mb_9 + self.dataFrame.vol_3g_mb_9
        # Customers who have not used either calls or internet in the last month are the churned customers and change category
        self.dataFrame['churn'] = self.dataFrame.apply(lambda rec: 1 if(rec.Total_calls_9==0 and rec.Total_data_9==0) else 0,axis=1)
        self.dataFrame.churn = self.dataFrame.churn.astype('category')
        # Drop the new features created
        self.dataFrame = self.dataFrame.drop(['Total_calls_9','Total_data_9'],axis=1)

        return self.dataFrame
    def process3(self):
        # This process is to compute the difference between 8th month and the average of 6th and 7th months

        self.dataFrame['arpu_diff'] = self.dataFrame.arpu_8 - ((self.dataFrame.arpu_6 + self.dataFrame.arpu_7) / 2)

        self.dataFrame['onnet_mou_diff'] = self.dataFrame.onnet_mou_8 - (
                    (self.dataFrame.onnet_mou_6 + self.dataFrame.onnet_mou_7) / 2)

        self.dataFrame['offnet_mou_diff'] = self.dataFrame.offnet_mou_8 - (
                    (self.dataFrame.offnet_mou_6 + self.dataFrame.offnet_mou_7) / 2)

        self.dataFrame['roam_ic_mou_diff'] = self.dataFrame.roam_ic_mou_8 - (
                    (self.dataFrame.roam_ic_mou_6 + self.dataFrame.roam_ic_mou_7) / 2)

        self.dataFrame['roam_og_mou_diff'] = self.dataFrame.roam_og_mou_8 - (
                    (self.dataFrame.roam_og_mou_6 + self.dataFrame.roam_og_mou_7) / 2)

        self.dataFrame['loc_og_mou_diff'] = self.dataFrame.loc_og_mou_8 - (
                    (self.dataFrame.loc_og_mou_6 + self.dataFrame.loc_og_mou_7) / 2)

        self.dataFrame['std_og_mou_diff'] = self.dataFrame.std_og_mou_8 - (
                    (self.dataFrame.std_og_mou_6 + self.dataFrame.std_og_mou_7) / 2)

        self.dataFrame['isd_og_mou_diff'] = self.dataFrame.isd_og_mou_8 - (
                    (self.dataFrame.isd_og_mou_6 + self.dataFrame.isd_og_mou_7) / 2)

        self.dataFrame['spl_og_mou_diff'] = self.dataFrame.spl_og_mou_8 - (
                    (self.dataFrame.spl_og_mou_6 + self.dataFrame.spl_og_mou_7) / 2)

        self.dataFrame['total_og_mou_diff'] = self.dataFrame.total_og_mou_8 - (
                    (self.dataFrame.total_og_mou_6 + self.dataFrame.total_og_mou_7) / 2)

        self.dataFrame['loc_ic_mou_diff'] = self.dataFrame.loc_ic_mou_8 - (
                    (self.dataFrame.loc_ic_mou_6 + self.dataFrame.loc_ic_mou_7) / 2)

        self.dataFrame['std_ic_mou_diff'] = self.dataFrame.std_ic_mou_8 - (
                    (self.dataFrame.std_ic_mou_6 + self.dataFrame.std_ic_mou_7) / 2)

        self.dataFrame['isd_ic_mou_diff'] = self.dataFrame.isd_ic_mou_8 - (
                    (self.dataFrame.isd_ic_mou_6 + self.dataFrame.isd_ic_mou_7) / 2)

        self.dataFrame['spl_ic_mou_diff'] = self.dataFrame.spl_ic_mou_8 - (
                    (self.dataFrame.spl_ic_mou_6 + self.dataFrame.spl_ic_mou_7) / 2)

        self.dataFrame['total_ic_mou_diff'] = self.dataFrame.total_ic_mou_8 - (
                    (self.dataFrame.total_ic_mou_6 + self.dataFrame.total_ic_mou_7) / 2)

        self.dataFrame['total_rech_num_diff'] = self.dataFrame.total_rech_num_8 - (
                    (self.dataFrame.total_rech_num_6 + self.dataFrame.total_rech_num_7) / 2)

        self.dataFrame['total_rech_amt_diff'] = self.dataFrame.total_rech_amt_8 - (
                    (self.dataFrame.total_rech_amt_6 + self.dataFrame.total_rech_amt_7) / 2)

        self.dataFrame['max_rech_amt_diff'] = self.dataFrame.max_rech_amt_8 - (
                    (self.dataFrame.max_rech_amt_6 + self.dataFrame.max_rech_amt_7) / 2)

        self.dataFrame['total_rech_data_diff'] = self.dataFrame.total_rech_data_8 - (
                    (self.dataFrame.total_rech_data_6 + self.dataFrame.total_rech_data_7) / 2)

        self.dataFrame['max_rech_data_diff'] = self.dataFrame.max_rech_data_8 - (
                    (self.dataFrame.max_rech_data_6 + self.dataFrame.max_rech_data_7) / 2)

        self.dataFrame['av_rech_amt_data_diff'] = self.dataFrame.av_rech_amt_data_8 - (
                    (self.dataFrame.av_rech_amt_data_6 + self.dataFrame.av_rech_amt_data_7) / 2)

        self.dataFrame['vol_2g_mb_diff'] = self.dataFrame.vol_2g_mb_8 - (
                    (self.dataFrame.vol_2g_mb_6 + self.dataFrame.vol_2g_mb_7) / 2)

        self.dataFrame['vol_3g_mb_diff'] = self.dataFrame.vol_3g_mb_8 - (
                    (self.dataFrame.vol_3g_mb_6 + self.dataFrame.vol_3g_mb_7) / 2)

        # Deleting columns related to 9th month

        self.dataFrame = self.dataFrame.filter(regex='[^9]$', axis=1)


        return self.dataFrame





