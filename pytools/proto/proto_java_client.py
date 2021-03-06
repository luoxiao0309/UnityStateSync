#!/usr/bin/env python
# coding:utf-8
from proto_java import ProtoJava, protocol_const


def parse(code_path, common_path, protos):
	name_ids	= list()
	for proto in protos:
		name_id	= dict()
		name_id['mess_name']	= proto['mess_name']
		name_id['mess_id'] 		= proto['mess_id']
		name_id['mess_note'] 	= proto['mess_note']
		name_ids.append(name_id)
		ProtoJava(code_path, proto).do_client()

	protocol_const(code_path, name_ids)
