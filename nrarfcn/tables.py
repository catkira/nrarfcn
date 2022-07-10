class Table:
    def __init__(self, id: str, release_3gpp: int, ts: str, name: str, header: list, data: list):
        self.id = id
        self.release_3gpp = release_3gpp
        self.ts = ts
        self.name = name
        self.header = header
        self.data = data

    def get_cell(self, row: list, key: str):
        idx = self.header.index(key)
        return row[idx]


def tables_data(key: str) -> Table:
    table_id = 'freq_nrarfcn'
    table_release_3gpp = 17
    table_ts = "3GPP TS 38.104 V17.6.0"
    table_name = "Table 5.4.2.1-1: NR-ARFCN parameters for the global frequency raster"
    table_header = ['f_min', 'f_max', 'df_global', 'f_ref_offs', 'n_ref_offs', 'n_ref_min', 'n_ref_max']
    table_data = [
        [0, 3_000, 5, 0, 0, 0, 599_999],
        [3_000, 24_250, 15, 3_000, 600_000, 600_000, 2_016_666],
        [24_250, 100_000, 60, 24_250.08, 2_016_667, 2_016_667, 3_279_165]
    ]

    table_freq_nrarfcn = Table(table_id, table_release_3gpp, table_ts, table_name, table_header, table_data)

    table_id = 'bands_fr1'
    table_release_3gpp = 0
    table_ts = ''
    table_name = "Table 5.2-1: NR operating bands in FR1"
    table_header = ['band', 'f_ul_low', 'f_ul_high', 'f_dl_low', 'f_dl_high', 'duplex_mode']
    table_data = [
        ['n1', 1920, 1980, 2110, 2170, 'FDD'],
        ['n2', 1850, 1910, 1930, 1990, 'FDD'],
        ['n3', 1710, 1785, 1805, 1880, 'FDD'],
        ['n5', 824, 849, 869, 894, 'FDD'],
        ['n7', 2500, 2570, 2620, 2690, 'FDD'],
        ['n8', 880, 915, 925, 960, 'FDD'],
        ['n12', 699, 716, 729, 746, 'FDD'],
        ['n14', 788, 798, 758, 768, 'FDD'],
        ['n18', 815, 830, 860, 875, 'FDD'],
        ['n20', 832, 862, 791, 821, 'FDD'],
        ['n25', 1850, 1915, 1930, 1995, 'FDD'],
        ['n26', 814, 849, 859, 894, 'FDD'],
        ['n28', 703, 748, 758, 803, 'FDD'],
        ['n29', 'N/A', 'N/A', 717, 728, 'SDL'],
        ['n30', 2305, 2315, 2350, 2360, 'FDD'],
        ['n34', 2010, 2025, 2010, 2025, 'TDD'],
        ['n38', 2570, 2620, 2570, 2620, 'TDD'],
        ['n39', 1880, 1920, 1880, 1920, 'TDD'],
        ['n40', 2300, 2400, 2300, 2400, 'TDD'],
        ['n41', 2496, 2690, 2496, 2690, 'TDD'],
        ['n48', 3550, 3700, 3550, 3700, 'TDD'],
        ['n50', 1432, 1517, 1432, 1517, 'TDD'],
        ['n51', 1427, 1432, 1427, 1432, 'TDD'],
        ['n53', 2483.5, 2495, 2483.5, 2495, 'TDD'],
        ['n65', 1920, 2010, 2110, 2200, 'FDD'],
        ['n66', 1710, 1780, 2110, 2200, 'FDD'],
        ['n70', 1695, 1710, 1995, 2020, 'FDD'],
        ['n71', 663, 698, 617, 652, 'FDD'],
        ['n74', 1427, 1470, 1475, 1518, 'FDD'],
        ['n75', 'N/A', 'N/A', 1432, 1517, 'SDL'],
        ['n76', 'N/A', 'N/A', 1427, 1432, 'SDL'],
        ['n77', 3300, 4200, 3300, 4200, 'TDD'],
        ['n78', 3300, 3800, 3300, 3800, 'TDD'],
        ['n79', 4400, 5000, 4400, 5000, 'TDD'],
        ['n80', 1710, 1785, 'N/A', 'N/A', 'SUL'],
        ['n81', 880, 915, 'N/A', 'N/A', 'SUL'],
        ['n82', 832, 862, 'N/A', 'N/A', 'SUL'],
        ['n83', 703, 748, 'N/A', 'N/A', 'SUL'],
        ['n84', 1920, 1980, 'N/A', 'N/A', 'SUL'],
        ['n86', 1710, 1780, 'N/A', 'N/A', 'SUL'],
        ['n89', 824, 849, 'N/A', 'N/A', 'SUL'],
        ['n90', 2496, 2690, 2496, 2690, 'TDD'],
        ['n91', 832, 862, 1427, 1432, 'FDD'],
        ['n92', 832, 862, 1432, 1517, 'FDD'],
        ['n93', 880, 915, 1427, 1432, 'FDD'],
        ['n94', 880, 915, 1432, 1517, 'FDD'],
        ['n95', 2010, 2025, 'N/A', 'N/A', 'SUL']
    ]

    table_bands_fr1 = Table(table_id, table_release_3gpp, table_ts, table_name, table_header, table_data)

    table_id = 'bands_fr2'
    table_release_3gpp = 17
    table_ts = "3GPP TS 38.104 V17.6.0"
    table_name = "Table 5.2-2: NR operating bands in FR2"
    table_header = ['band', 'f_ul_low', 'f_ul_high', 'f_dl_low', 'f_dl_high', 'duplex_mode']
    table_data = [
        ['n257', 26500, 29500, 26500, 29500, 'TDD'],
        ['n258', 24250, 27500, 24250, 27500, 'TDD'],
        ['n259', 39500, 43500, 39500, 43500, 'TDD'],
        ['n260', 37000, 40000, 37000, 40000, 'TDD'],
        ['n261', 27500, 28350, 27500, 28350, 'TDD'],
        ['n262', 47200, 48200, 47200, 48200, 'TDD'],
        ['n263', 57000, 71000, 57000, 71000, 'TDD'],
    ]

    table_bands_fr2 = Table(table_id, table_release_3gpp, table_ts, table_name, table_header, table_data)

    table_id = 'applicable_nrarfcn_fr1'
    table_release_3gpp = 17
    table_ts = "3GPP TS 38.104 V17.6.0"
    table_name = "Table 5.4.2.3-1: Applicable NR-ARFCN per operating band in FR1"
    table_header = ['band', 'f_raster', 'ul_first', 'ul_step', 'ul_range', 'dl_first', 'dl_step', 'dl_range']
    table_data = [
        ['n1', 100, 384000, 20, 396000, 422000, 20, 434000],
        ['n2', 100, 370000, 20, 382000, 386000, 20, 398000],
        ['n3', 100, 342000, 20, 357000, 361000, 20, 376000],
        ['n5', 100, 164800, 20, 169800, 173800, 20, 178800],
        ['n7', 100, 500000, 20, 514000, 524000, 20, 538000],
        ['n8', 100, 176000, 20, 183000, 185000, 20, 192000],
        ['n12', 100, 139800, 20, 143200, 145800, 20, 149200],
        ['n13', 100, 155400, 20, 157400, 149200, 20, 151200],
        ['n14', 100, 157600, 20, 159600, 151600, 20, 153600],
        ['n18', 100, 163000, 20, 166000, 172000, 20, 175000],
        ['n20', 100, 166400, 20, 172400, 158200, 20, 164200],
        ['n25', 100, 370000, 20, 383000, 386000, 20, 399000],
        ['n24', 100, 325300, 20, 332100, 305000, 20, 311800],
        ['n26', 100, 162800, 20, 169800, 171800, 20, 178800],
        ['n28', 100, 140600, 20, 149600, 151600, 20, 160600],
        ['n29', 100, 'N/A', 'N/A', 'N/A', 143400, 20, 145600],
        ['n30', 100, 461000, 20, 463000, 470000, 20, 472000],
        ['n34', 100, 402000, 20, 405000, 402000, 20, 405000],
        ['n38', 100, 514000, 20, 524000, 514000, 20, 524000],
        ['n39', 100, 376000, 20, 384000, 376000, 20, 384000],
        ['n40', 100, 460000, 20, 480000, 460000, 20, 480000],
        ['n41', 15, 499200, 3, 537999, 499200, 3, 537999],
        ['n41', 30, 499200, 6, 537996, 499200, 6, 537996],
        ['n46', 15, 743334, 1, 795000, 743334, 1, 795000],
        ['n48', 15, 636667, 1, 646666, 636667, 1, 646666],
        ['n48', 30, 636668, 2, 646666, 636668, 2, 646666],
        ['n50', 100, 286400, 20, 303400, 286400, 20, 303400],
        ['n51', 100, 285400, 20, 286400, 285400, 20, 286400],
        ['n53', 100, 496700, 20, 499000, 496700, 20, 499000],
        ['n65', 100, 384000, 20, 402000, 422000, 20, 440000],
        ['n66', 100, 342000, 20, 356000, 422000, 20, 440000],
        ['n67', 100, 'N/A', 'N/A', 'N/A', 147600, 20, 151600],
        ['n70', 100, 339000, 20, 342000, 399000, 20, 404000],
        ['n71', 100, 132600, 20, 139600, 123400, 20, 130400],
        ['n74', 100, 285400, 20, 294000, 295000, 20, 303600],
        ['n75', 100, 'N/A', 'N/A', 'N/A', 286400, 20, 303400],
        ['n76', 100, 'N/A', 'N/A', 'N/A', 285400, 20, 286400],
        ['n77', 15, 620000, 1, 680000, 620000, 1, 680000],
        ['n77', 30, 620000, 2, 680000, 620000, 2, 680000],
        ['n78', 15, 620000, 1, 653333, 620000, 1, 653333],
        ['n78', 30, 620000, 2, 653332, 620000, 2, 653332],
        ['n79', 15, 693334, 1, 733333, 693334, 1, 733333],
        ['n79', 30, 693334, 2, 733332, 693334, 2, 733332],
        ['n80', 100, 342000, 20, 357000, 'N/A', 'N/A', 'N/A'],
        ['n81', 100, 176000, 20, 183000, 'N/A', 'N/A', 'N/A'],
        ['n82', 100, 166400, 20, 172400, 'N/A', 'N/A', 'N/A'],
        ['n83', 100, 140600, 20, 149600, 'N/A', 'N/A', 'N/A'],
        ['n84', 100, 384000, 20, 396000, 'N/A', 'N/A', 'N/A'],
        ['n85', 100, 139600, 20, 143200, 145600, 20, 149200],
        ['n86', 100, 342000, 20, 356000, 'N/A', 'N/A', 'N/A'],
        ['n89', 100, 164800, 20, 169800, 'N/A', 'N/A', 'N/A'],
        ['n90', 15, 499200, 3, 537999, 499200, 3, 537999],
        ['n90', 30, 499200, 6, 537996, 499200, 6, 537996],
        ['n90', 100, 499200, 20, 538000, 499200, 20, 538000],
        ['n91', 100, 166400, 20, 172400, 285400, 20, 286400],
        ['n92', 100, 166400, 20, 172400, 286400, 20, 303400],
        ['n93', 100, 176000, 20, 183000, 285400, 20, 286400],
        ['n94', 100, 176000, 20, 183000, 286400, 20, 303400],
        ['n95', 100, 402000, 20, 405000, 'N/A', 'N/A', 'N/A'],
        ['n96', 15, 795000, 1, 875000, 795000, 1, 875000],
        ['n97', 100, 460000, 20, 480000, 'N/A', 'N/A', 'N/A'],
        ['n98', 100, 376000, 20, 384000, 'N/A', 'N/A', 'N/A'],
        ['n99', 100, 325300, 20, 332100, 'N/A', 'N/A', 'N/A'],
        ['n100', 100, 174880, 20, 176000, 183880, 20, 185000],
        ['n101', 100, 380000, 20, 382000, 380000, 20, 382000],
        ['n102', 15, 796334, 1, 828333, 796334, 1, 828333],
        ['n104', 15, 828334, 1, 875000, 828334, 1, 875000],
        ['n104', 30, 828334, 2, 875000, 828334, 2, 875000]
    ]

    table_applicable_nrarfcn_fr1 = Table(table_id, table_release_3gpp, table_ts, table_name, table_header, table_data)

    table_id = 'applicable_nrarfcn_fr2'
    table_release_3gpp = 17
    table_ts = "3GPP TS 38.104 V17.6.0"
    table_name = "Table 5.4.2.3-2: Applicable NR-ARFCN per operating band in FR2"
    table_header = ['band', 'f_raster', 'ul_first', 'ul_step', 'ul_range', 'dl_first', 'dl_step', 'dl_range']
    table_data = [
        ['n257', 60, 2054166, 1, 2104165, 2054166, 1, 2104165],
        ['n257', 120, 2054167, 2, 2104165, 2054167, 2, 2104165],
        ['n258', 60, 2016667, 1, 2070832, 2016667, 1, 2070832],
        ['n258', 120, 2016667, 2, 2070831, 2016667, 2, 2070831],
        ['n259', 60, 2270833, 1, 2337499, 2270833, 1, 2337499],
        ['n259', 120, 2270833, 2, 2337499, 2270833, 2, 2337499],
        ['n260', 60, 2229166, 1, 2279165, 2229166, 1, 2279165],
        ['n260', 120, 2229167, 2, 2279165, 2229167, 2, 2279165],
        ['n261', 60, 2070833, 1, 2084999, 2070833, 1, 2084999],
        ['n261', 120, 2070833, 2, 2084999, 2070833, 2, 2084999],
        ['n262', 60, 2399166, 1, 2415832, 2399166, 1, 2415832],
        ['n262', 120, 2399167, 2, 2415831, 2399167, 2, 2415831],
        ['n263', 120, 2564083, 1680, 2794243, 2564083, 1680, 2794243],
        ['n263', 480, 2566603, 6720, 2788363, 2566603, 6720, 2788363],
        ['n263', 960, 2566603, 6720, 2788363, 2566603, 6720, 2788363]
    ]
    #  refer to 3GPP TS38.104 v17.6.0 tables 5.3.5-3 5.4.2.3-3 for n263 info

    table_applicable_nrarfcn_fr2 = Table(table_id, table_release_3gpp, table_ts, table_name, table_header, table_data)

    tables = {
        'freq_nrarfcn': table_freq_nrarfcn,
        'bands_fr1': table_bands_fr1,
        'bands_fr2': table_bands_fr2,
        'applicable_nrarfcn_fr1': table_applicable_nrarfcn_fr1,
        'applicable_nrarfcn_fr2': table_applicable_nrarfcn_fr2
    }

    return tables.get(key)
