# from deeppavlov import configs, build_model
# import requests
#
# ner_model_bert = build_model(configs.ner.ner_rus_bert, download=True)
#
#
# def define_locs(bert):
#     all_loc = []
#     curr_loc = []
#     lenght = len(bert[0])
#     for i in range(lenght):
#         dict_items = dict(zip(bert[0][i], bert[1][i]))
#         for k, v in dict_items.items():
#             if (v == 'B-LOC'):
#                 if (curr_loc):
#                     all_loc.append(' '.join(curr_loc))
#                     curr_loc = []
#                 curr_loc.append(k)
#             elif (v == 'I-LOC'):
#                 if (curr_loc):
#                     curr_loc.append(k)
#             else:
#                 if (curr_loc):
#                     all_loc.append(' '.join(curr_loc))
#                     curr_loc = []
#         if (curr_loc):
#             all_loc.append(' '.join(curr_loc))
#             curr_loc = []
#     return all_loc
#
#
# def try_bert(line):
#     res_bert = ner_model_bert([line])
#     res_loc = define_locs(res_bert)
#     return res_loc
#
#
# separators = [None, ',', '.', ';']
#
#
# def find_locs(line):
#     ind = 0
#     flag = True
#     res_bert = None
#
#     while flag:
#         try:
#             sep = separators[ind]
#             if sep:
#                 new_line = line.split(sep)
#                 res_bert = ner_model_bert(new_line)
#             else:
#                 res_bert = ner_model_bert(line)
#
#             flag = False
#
#         except:
#             ind += 1
#
#     if res_bert:
#         res_loc = define_locs(res_bert)
#         if res_loc:
#             return res_loc
#
#     return None
