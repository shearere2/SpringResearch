import pandas as pd
def csv_merge(pitt:pd.DataFrame, walkability:pd.DataFrame):
    pitt_walkability = walkability.loc[walkability['stat_area_name'].str.contains('Pittsburgh') == True].copy()
    pittsburgh_tracts = [10300, 20100, 20300, 30500, 40200, 40400, 40500, 40600,
                         40900, 50100, 50600, 50900, 51000, 51100, 60300, 60500,
                         70300, 70500, 70600, 70800, 70900, 80200, 80400, 80600,
                         80700, 80900, 90100, 90200, 90300, 100500, 101100, 101400,
                         101800, 101900, 110200, 110600, 111300, 111400, 111500,
                         120300, 120900, 130200, 130600, 130700, 130800, 140100,
                         140200, 140300, 140400, 140500, 140800, 141100, 141200,
                         141300, 141400, 151600, 151700, 160800, 160900, 161000,
                         170200, 170600, 180300, 180700, 190300, 191100, 191400,
                         191500, 191600, 191700, 191800, 191900, 192000, 202200,
                         202300, 241300, 250900, 260200, 260700, 261300, 261400,
                         261500, 262000, 270100, 270300, 270800, 271600, 281400,
                         281500, 290100, 290200, 290400, 300100, 310200, 320400,
                         320600, 320700, 401100, 401200, 401300, 402000, 403500,
                         404000, 405000, 406000, 407000, 408000, 409000, 410000,
                         411000, 412000, 413100, 413200, 413300, 413400, 413500,
                         414100, 414200, 415000, 416000, 417100, 417200, 418000,
                         419000, 420000, 421100, 421200, 422000, 423000, 424000,
                         425000, 426300, 426400, 426700, 426800, 427000, 427100,
                         427200, 428100, 428200, 429100, 429200, 429300, 429400,
                         429500, 429600, 429700, 430100, 430200, 431100, 431400,
                         431500, 432300, 432400, 434000, 435000, 437000, 439000,
                         445500, 446000, 447000, 448000, 449000, 450700, 450800,
                         451100, 451300, 452000, 453000, 455000, 456000, 457100,
                         457200, 458000, 459100, 459200, 460000, 461000, 462100,
                         462600, 463900, 464300, 464400, 465600, 465800, 468700,
                         468800, 468900, 469000, 470300, 470400, 470500, 470600,
                         471000, 472100, 472200, 472300, 472400, 473100, 473200,
                         473300, 473400, 473500, 473600, 474100, 474200, 475100,
                         475200, 475300, 475400, 476100, 476200, 477100, 477200,
                         477300, 478100, 478200, 479000, 480100, 480200, 480300,
                         480400, 481000, 482500, 483800, 484300, 484500, 484600,
                         485000, 486700, 486800, 486900, 487000, 488100, 488200,
                         488300, 488400, 488500, 488600, 489000, 491100, 491200,
                         492700, 492800, 492900, 494000, 495000, 496100, 496200,
                         497000, 498000, 499300, 499400, 500300, 501000, 503000,
                         504100, 507000, 508000, 509400, 510000, 512000, 513000,
                         513800, 514000, 515100, 515200, 515300, 515400, 516100,
                         516200, 517000, 518000, 519000, 520000, 521100, 521200,
                         521300, 521300, 521400, 521400, 521500, 522000, 523100,
                         523200, 523300, 523400, 523500, 523500, 523600, 523700,
                         523700, 523800, 524000, 525100, 525200, 525300, 526100,
                         526100, 526200, 526200, 526300, 526300, 550900, 551200,
                         551300, 551900, 552000, 552100, 552200, 552300, 552400,
                         560400, 560500, 561400, 561500, 561900, 562000, 562300,
                         562400, 562500, 562600, 562700, 562800, 562900, 563000,
                         563100, 563200, 563300, 563800, 563900, 564000, 564100,
                         564200, 564400, 564500, 564700, 564800, 565100, 565200,
                         565300, 980000, 980100, 980300, 980400, 980500, 980600,
                         980700, 980800, 980900, 981000, 981100, 981200, 981800,
                         982200]
    
    return pitt_walkability.loc[pitt_walkability['tract_fips_code'] in pittsburgh_tracts]


if __name__ == "__main__":
    df1 = pd.read_csv('data/pitt_neighborhoods_merged.csv',low_memory=False)
    df2 = pd.read_csv('data/walkability.csv',low_memory=False)
    csv_merge(df1,df2)