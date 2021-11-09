import math

class CreatePrice:
    def prices(self, adminValues) -> dict:
        
        # Create new headers / field names
        euPrices = []
        euPricesTruncate = []
        euFinalPrices = []
        euFinalPricesTruncate = []
        adminValues['Price (en-GB)'] = []
        adminValues['Final Price (en-GB)'] = []        
        adminValues['Price (de-DE)'] = []
        adminValues['Final Price (de-DE)'] = []
        adminValues['Price (nl-NL)'] = []
        adminValues['Final Price (nl-NL)'] = []
        adminValues['Price (fi-FI)'] = []
        adminValues['Final Price (fi-FI)'] = []        
        #
        adminValues['Price (da-DK)'] = []        
        adminValues['Final Price (da-DK)'] = []
        adminValues['Price (nb-NO)'] = []
        adminValues['Final Price (nb-NO)'] = []
        adminValues['Price (sv-SE)'] = []
        adminValues['Final Price (sv-SE)'] = []

        # SE Prices / Org. Price
        # Start from index 1, because first row is str('Price')        
        for index, orgPrice in enumerate(adminValues['Price']):

            if index != 0:                                
                # Org price. Convert to int.
                adminValues['Price (sv-SE)'].append(int(orgPrice))
                # 20% Discount. Roundup to nearest 10. Minus 1 (nearest 9). Convert to int.
                adminValues['Final Price (sv-SE)'].append(int(math.ceil((int(orgPrice) - int(orgPrice) * 0.20) / (10.0)) * (10) - 1))
                                    
        for index, sePrice in enumerate(adminValues['Price (sv-SE)']):
            # Multiply by 0.7. Roundup to nearest 10. Minus 1. Convert to int
            adminValues['Price (da-DK)'].append(int(math.ceil(int(sePrice * 0.7) / (10.0)) * (10) - 1))
            # Multiply by 0.1. Roundup to nearest 10. Minus 1. Convert to int.
            adminValues['Price (nb-NO)'].append(int(math.ceil(int(sePrice + (sePrice * 0.1)) / (10.0)) * (10) - 1))
            # Multipy by 0.11. Rounddown to nearest 0.05. Append to euPrices[]
            euPrices.append(float(math.floor(float(sePrice * 0.11) / 0.05) * (0.05)))

        # Special Price
        for index, sePrice in enumerate(adminValues['Final Price (sv-SE)']):
            
            # DK                                    
            # Multiply by 0.7. Roundup to nearest 10. Minus 1. Convert to int
            adminValues['Final Price (da-DK)'].append(int(math.ceil(int(sePrice * 0.7) / (10.0)) * (10) - 1))
            # dkPrices.append(int(math.ceil(int(sePrice * 0.7) / (10.0)) * (10) - 1))

            # NO
            # Multiply by 0.1. Roundup to nearest 10. Minus 1. Convert to int.
            adminValues['Final Price (nb-NO)'].append(int(math.ceil(int(sePrice + (sePrice * 0.1)) / (10.0)) * (10) - 1))

            # Create EU prices
            # Multipy by 0.11. Rounddown to nearest 0.05. Append to euPrices[]			
            euFinalPrices.append(float(math.floor(float(sePrice * 0.11) / 0.05) * (0.05)))						

        ## Truncate eu prices (get rid off 7.50000000000001)
        for euPrice in euPrices:
            euPricesTruncate.append((math.floor(euPrice * 100)) / 100.0)

        for euPrice in euPricesTruncate:                    
            adminValues['Price (en-GB)'].append(euPrice)
            adminValues['Price (de-DE)'].append(euPrice)
            adminValues['Price (nl-NL)'].append(euPrice)
            adminValues['Price (fi-FI)'].append(euPrice)

        # Special Prices 
        for euPrice in euFinalPrices:
            euFinalPricesTruncate.append((math.floor(euPrice * 100)) / 100.0)
        
        for euPrice in euFinalPricesTruncate:                    
            adminValues['Final Price (en-GB)'].append(euPrice)
            adminValues['Final Price (de-DE)'].append(euPrice)
            adminValues['Final Price (nl-NL)'].append(euPrice)
            adminValues['Final Price (fi-FI)'].append(euPrice)

        # Ler first value be price, because reasons...
        adminValues['Price (en-GB)'].insert(0, 'Price')
        adminValues['Final Price (en-GB)'].insert(0, 'Price')
        adminValues['Price (de-DE)'].insert(0, 'Price')
        adminValues['Final Price (de-DE)'].insert(0, 'Price')
        adminValues['Price (nl-NL)'].insert(0, 'Price')
        adminValues['Final Price (nl-NL)'].insert(0, 'Price')
        adminValues['Price (fi-FI)'].insert(0, 'Price')
        adminValues['Final Price (fi-FI)'].insert(0, 'Price')
        adminValues['Price (da-DK)'].insert(0, 'Price')
        adminValues['Final Price (da-DK)'].insert(0, 'Price')
        adminValues['Price (nb-NO)'].insert(0, 'Price')
        adminValues['Final Price (nb-NO)'].insert(0, 'Price')
        adminValues['Price (sv-SE)'].insert(0, 'Price')
        adminValues['Final Price (sv-SE)'].insert(0, 'Price')

        # Return dict
        return adminValues