#
# from numpy import array
# from numpy import argmax
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OneHotEncoder
# # define example
# data = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot', 'warm', 'cold', 'warm', 'hot']
# values = array(data)
# print(values)
# # integer encode
# label_encoder = LabelEncoder()
# integer_encoded = label_encoder.fit_transform(values)
# print(integer_encoded)
# # binary encode
# onehot_encoder = OneHotEncoder(sparse=False)
# integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
# onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
# print(onehot_encoded)
# # invert first example
# inverted = label_encoder.inverse_transform([argmax(onehot_encoded[2, :])])
# print(inverted)


# from sklearn.preprocessing import OneHotEncoder
#
# enc = OneHotEncoder(handle_unknown='ignore')
# X = [['Male', 1], ['Female', 3], ['Female', 2]]
# enc.fit(X)
#
# enc.categories_
#
# enc.transform([['Female', 1], ['Male', 4]]).toarray()
#
#
# enc.inverse_transform([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0]])
#
#
# enc.get_feature_names(['gender', 'group'])
#
#
# drop_enc = OneHotEncoder(drop='first').fit(X)
# drop_enc.categories_
#
# drop_enc.transform([['Female', 1], ['Male', 2]]).toarray()

# enc = OneHotEncoder(handle_unknown='ignore')
# X = [['Male', 1], ['Female', 3], ['Female', 2]]
# enc.fit(X)
#
# enc.categories_
#
# enc.transform([['Female', 1], ['Male', 4]]).toarray()
#
#
# enc.inverse_transform([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0]])
#
#
# enc.get_feature_names(['gender', 'group'])
#
#
# drop_enc = OneHotEncoder(drop='first').fit(X)
# drop_enc.categories_
#
# drop_enc.transform([['Female', 1], ['Male', 2]]).toarray()

import argparse

parser = argparse.ArgumentParser(
        description='''HPE-to-HAR for robots - RNN training utility''')

subpars = parser.add_subparsers(help='Commands to pre-process or train the RNN')

parser_stats = subpars.add_parser('stat', help='Plot statistics about the pre-processed data set.')
parser_stats.add_argument('-conf', dest='conf_path_list', type=str, nargs='*', required=True,
                          help='List of path to configuration files for training.')
# parser_stats.set_defaults(func=plot_statistics)

# Create the parser for the "pre-process" command
parser_preproc = subpars.add_parser('pre-process',
                                    help='Pre-process data: prepare CVAT dumps and then extract poses '
                                         'using OpenPose-based HPE module.')

parser_preproc.add_argument('-files', action='store_true', type=str, nargs='*',
                            help='List of file names (in CVAT dumps '
                                 'path) to pre-process.')

# parser = argparse.ArgumentParser()
#
# parser.add_argument('-o', '--outputt', action='store_true',
#                     help="shows output")
#
# args = parser.parse_args()
#
# if args.outputt:
#     print("This is some output")

# parser = argparse.ArgumentParser(description='Process some integers.')
#
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
#
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

parser = argparse.ArgumentParser()

parser.add_argument('--name', required=True)

args = parser.parse_args()

print(f'Hello {args.name}')