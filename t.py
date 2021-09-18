    import re
    ak = 'LTAI5tLdUMxQAUNeSAGFL8Ho'
    sk = 'pG2g4K19skdia7YDuyg4Hi4lrYyXtE'
    
    for r in regi_list:
        # r = 'cn-guangzhou'
        print('region:',r)
        # print('cn-hangzhou')
        clt = client.AcsClient('LTAI5tLdUMxQAUNeSAGFL8Ho', 'pG2g4K19skdia7YDuyg4Hi4lrYyXtE', r)

        try:
            list_instances()
        except Exception as e:
            # print(e)
            pass

        time.sleep(3)
        print('###################################################################################\n\n')
