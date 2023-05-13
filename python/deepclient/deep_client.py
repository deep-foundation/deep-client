import asyncio
from typing import Any, Optional, Union, Dict, List
from .deep_client_options import DeepClientOptions
from .gql.serial import generate_serial
from .query import generate_query, generate_query_data

class DeepClient:
    _ids = {
      "@deep-foundation/core": {
        "Type": 1,
        "Package": 2,
        "Contain": 3,
        "Value": 4,
        "String": 5,
        "Number": 6,
        "Object": 7,
        "Any": 8,
        "Promise": 9,
        "Then": 10,
        "Resolved": 11,
        "Rejected": 12,
        "typeValue": 13,
        "packageValue": 14,
        "Selector": 15,
        "SelectorInclude": 16,
        "Rule": 17,
        "RuleSubject": 18,
        "RuleObject": 19,
        "RuleAction": 20,
        "containValue": 21,
        "User": 22,
        "Operation": 23,
        "operationValue": 24,
        "AllowInsert": 25,
        "AllowUpdate": 26,
        "AllowDelete": 27,
        "AllowSelect": 28,
        "File": 29,
        "SyncTextFile": 30,
        "syncTextFileValue": 31,
        "ExecutionProvider": 32,
        "JSExecutionProvider": 33,
        "TreeInclude": 34,
        "Handler": 35,
        "Tree": 36,
        "TreeIncludeDown": 37,
        "TreeIncludeUp": 38,
        "TreeIncludeNode": 39,
        "containTree": 40,
        "containTreeContain": 41,
        "containTreeAny": 42,
        "PackageNamespace": 43,
        "packageNamespaceValue": 44,
        "PackageActive": 45,
        "PackageVersion": 46,
        "packageVersionValue": 47,
        "HandleOperation": 48,
        "HandleInsert": 49,
        "HandleUpdate": 50,
        "HandleDelete": 51,
        "PromiseResult": 52,
        "promiseResultValueRelationTable": 53,
        "PromiseReason": 54,
        "Focus": 55,
        "focusValue": 56,
        "AsyncFile": 57,
        "Query": 58,
        "queryValue": 59,
        "Fixed": 60,
        "fixedValue": 61,
        "Space": 62,
        "spaceValue": 63,
        "AllowLogin": 64,
        "guests": 65,
        "Join": 66,
        "joinTree": 67,
        "joinTreeJoin": 68,
        "joinTreeAny": 69,
        "SelectorTree": 70,
        "AllowAdmin": 71,
        "SelectorExclude": 72,
        "SelectorFilter": 73,
        "HandleSchedule": 74,
        "Schedule": 75,
        "scheduleValue": 76,
        "Router": 77,
        "IsolationProvider": 78,
        "DockerIsolationProvider": 79,
        "dockerIsolationProviderValue": 80,
        "JSDockerIsolationProvider": 81,
        "Supports": 82,
        "dockerSupportsJs": 83,
        "PackageInstall": 84,
        "PackagePublish": 85,
        "packageInstallCode": 86,
        "packageInstallCodeHandler": 87,
        "packageInstallCodeHandleInsert": 88,
        "packagePublishCode": 89,
        "packagePublishCodeHandler": 90,
        "packagePublishCodeHandleInsert": 91,
        "Active": 92,
        "AllowPackageInstall": 93,
        "AllowPackagePublish": 94,
        "PromiseOut": 95,
        "promiseOutValue": 96,
        "PackageQuery": 97,
        "packageQueryValue": 98,
        "Port": 99,
        "portValue": 100,
        "HandlePort": 101,
        "PackageInstalled": 102,
        "PackagePublished": 103,
        "Route": 104,
        "RouterListening": 105,
        "RouterStringUse": 106,
        "routerStringUseValue": 107,
        "HandleRoute": 108,
        "routeTree": 109,
        "routeTreePort": 110,
        "routeTreeRouter": 111,
        "routeTreeRoute": 112,
        "routeTreeHandler": 113,
        "routeTreeRouterListening": 114,
        "routeTreeRouterStringUse": 115,
        "routeTreeHandleRoute": 116,
        "TreeIncludeIn": 117,
        "TreeIncludeOut": 118,
        "TreeIncludeFromCurrent": 119,
        "TreeIncludeToCurrent": 120,
        "TreeIncludeCurrentFrom": 121,
        "TreeIncludeCurrentTo": 122,
        "TreeIncludeFromCurrentTo": 123,
        "TreeIncludeToCurrentFrom": 124,
        "AllowInsertType": 125,
        "AllowUpdateType": 126,
        "AllowDeleteType": 127,
        "AllowSelectType": 128,
        "ruleTree": 129,
        "ruleTreeRule": 130,
        "ruleTreeRuleAction": 131,
        "ruleTreeRuleObject": 132,
        "ruleTreeRuleSubject": 133,
        "ruleTreeRuleSelector": 134,
        "ruleTreeRuleQuery": 135,
        "ruleTreeRuleSelectorInclude": 136,
        "ruleTreeRuleSelectorExclude": 137,
        "ruleTreeRuleSelectorFilter": 138,
        "Plv8IsolationProvider": 139,
        "JSminiExecutionProvider": 140,
        "plv8SupportsJs": 141,
        "Authorization": 142,
        "GeneratedFrom": 143,
        "ClientJSIsolationProvider": 144,
        "clientSupportsJs": 145,
        "Symbol": 146,
        "symbolValue": 147,
        "containTreeSymbol": 148,
        "containTreeThen": 149,
        "containTreeResolved": 150,
        "containTreeRejected": 151,
        "handlersTree": 152,
        "handlersTreeHandler": 153,
        "handlersTreeSupports": 154,
        "handlersTreeHandleOperation": 155,
        "HandleClient": 156,
        "HandlingError": 157,
        "handlingErrorValue": 158,
        "HandlingErrorReason": 159,
        "HandlingErrorLink": 160,
        "GqlEndpoint": 161,
        "MainGqlEndpoint": 162,
        "HandleGql": 163,
        "SupportsCompatable": 164,
        "plv8JSSupportsCompatableHandleInsert": 165,
        "plv8JSSupportsCompatableHandleUpdate": 166,
        "plv8JSSupportsCompatableHandleDelete": 167,
        "dockerJSSupportsCompatableHandleInsert": 168,
        "dockerJSSupportsCompatableHandleUpdate": 169,
        "dockerJSSupportsCompatableHandleDelete": 170,
        "dockerJSSupportsCompatableHandleSchedule": 171,
        "dockerJSSupportsCompatableHandlePort": 172,
        "dockerJSSupportsCompatableHandleRoute": 173,
        "clientJSSupportsCompatableHandleClient": 174,
        "promiseTree": 175,
        "promiseTreeAny": 176,
        "promiseTreeThen": 177,
        "promiseTreePromise": 178,
        "promiseTreeResolved": 179,
        "promiseTreeRejected": 180,
        "promiseTreePromiseResult": 181,
        "MigrationsEnd": 182
      }
    }

    _serialize = {
        "links": {
            "fields": {
                "id": "number",
                "from_id": "number",
                "to_id": "number",
                "type_id": "number",
            },
            "relations": {
                "from": "links",
                "to": "links",
                "type": "links",
                "in": "links",
                "out": "links",
                "typed": "links",
                "selected": "selector",
                "selectors": "selector",
                "value": "value",
                "string": "value",
                "number": "value",
                "object": "value",
                "can_rule": "can",
                "can_action": "can",
                "can_object": "can",
                "can_subject": "can",
                "down": "tree",
                "up": "tree",
                "tree": "tree",
                "root": "tree",
            },
        },
        "selector": {
            "fields": {
                "item_id": "number",
                "selector_id": "number",
                "query_id": "number",
                "selector_include_id": "number",
            },
            "relations": {
                "item": "links",
                "selector": "links",
                "query": "links",
            }
        },
        "can": {
            "fields": {
                "rule_id": "number",
                "action_id": "number",
                "object_id": "number",
                "subject_id": "number",
            },
            "relations": {
                "rule": "links",
                "action": "links",
                "object": "links",
                "subject": "links",
            }
        },
        "tree": {
            "fields": {
                "id": "number",
                "link_id": "number",
                "tree_id": "number",
                "root_id": "number",
                "parent_id": "number",
                "depth": "number",
                "position_id": "string",
            },
            "relations": {
                "link": "links",
                "tree": "links",
                "root": "links",
                "parent": "links",
                "by_link": "tree",
                "by_tree": "tree",
                "by_root": "tree",
                "by_parent": "tree",
                "by_position": "tree",
            }
        },
        "value": {
            "fields": {
                "id": "number",
                "link_id": "number",
                "value": "value",
            },
            "relations": {
                "link": "links",
            },
        },
    }

    _boolExpFields = {
        "_and": True,
        "_not": True,
        "_or": True,
    }

    def path_to_where(self, start, *path):
        pckg = {"type_id": self._ids["@deep-foundation/core"]["Package"], "value": start} if isinstance(start, str) else {"id": start}
        where = pckg
        for item in path:
            if not isinstance(item, bool):
                nextWhere = {"in": {"type_id": self._ids["@deep-foundation/core"]["Contain"], "value": item, "from": where}}
                where = nextWhere
        return where

    def type_to_name(self, value_type):   
        if value_type is int:
            return 'number'
        if value_type is str:
            return 'string'

    def serialize_where(self, exp: Any, env: str = 'links') -> Any:
        if isinstance(exp, list):
            return [self.serialize_where(e, env) for e in exp]
        elif isinstance(exp, dict):
            keys = exp.keys()
            result = {}
            for key in keys:
                key_type = type(exp[key])
                setted = False
                is_id_field = key in ['type_id', 'from_id', 'to_id']
                if env == 'links':
                    if key_type in (str, int):
                        if key == 'value' or key == self.type_to_name(key_type):
                            setted = result[self.type_to_name(key_type)] = {'value': {'_eq': exp[key]}}
                        else:
                            setted = result[key] = {'_eq': exp[key]}
                    elif key not in self._boolExpFields and isinstance(exp[key], list):
                        setted = result[key] = self.serialize_where(self.path_to_where(*exp[key]))
                elif env == 'value':
                    if key_type in (str, int):
                        setted = result[key] = {'_eq': exp[key]}

                ids = [
                    'rule_id', 'action_id', 'subject_id', 'object_id',
                    'link_id', 'tree_id', 'root_id', 'parent_id'
                ]
                if (
                    key_type == dict
                    and '_type_of' in exp[key]
                    and (
                        (env == 'links' and (is_id_field or key == 'id')) or
                        (env == 'selector' and key == 'item_id') or
                        (env == 'can' and key in ids) or
                        (env == 'tree' and key in ids) or
                        (env == 'value' and key == 'link_id')
                    )
                ):
                    _temp = setted = {
                        '_by_item': {
                            'path_item_id': {'_eq': exp[key]['_type_of']},
                            'group_id': {'_eq': 0}
                        }
                    }
                    if key == 'id':
                        result['_and'] = [*result.get('_and', []), _temp]
                    else:
                        result[key[:-3]] = _temp
                elif (
                    key_type == dict
                    and '_id' in exp[key]
                    and (
                        (env == 'links' and (is_id_field or key == 'id')) or
                        (env == 'selector' and key == 'item_id') or
                        (env == 'can' and key in ids) or
                        (env == 'tree' and key in ids) or
                        (env == 'value' and key == 'link_id')
                    )
                    and isinstance(exp[key]['_id'], list)
                    and len(exp[key]['_id']) >= 1
                ):
                    _temp = setted = self.serialize_where(
                        self.path_to_where(exp[key]['_id'][0], *exp[key]['_id'][1:]), 'links'
                    )
                    if key == 'id':
                        result['_and'] = [*result.get('_and', []), _temp]
                    else:
                        result[key[:-3]] = _temp

                if not setted:
                    _temp = (
                        self.serialize_where(exp[key], env) if key in self._boolExpFields else (
                            self.serialize_where(exp[key], self._serialize.get(env, {}).get('relations', {}).get(key))
                        if self._serialize.get(env, {}).get('relations', {}).get(key) else exp[key]
                        )
                    )
                    if key == '_and':
                        if '_and' in result:
                            result['_and'].extend(_temp)
                        else:
                            result['_and'] = _temp
                    else:
                        result[key] = _temp
            return result
        else:
            if exp is None:
                raise ValueError('undefined in query')
            return exp

    def __init__(self, options: Optional[DeepClientOptions] = None):
        if options is None:
            options = DeepClientOptions()

        self.__dict__.update(options.__dict__)
        self.client = self.gql_client if self.gql_client else None

    async def select(self, exp: Union[Dict, int, List[int]], options: Dict = {}) -> Dict:
        if not exp:
            return {"error": {"message": "!exp"}, "data": None, "loading": False, "networkStatus": None}

        if isinstance(exp, list):
            where = {"id": {"_in": exp}}
        elif isinstance(exp, dict):
            where = self.serialize_where(exp, options.get("table", "links"))
        else:
            where = {"id": {"_eq": exp}}
        
        table = options.get("table", self.table)
        returning = options.get("returning", self.default_returning(table))
        
        variables = options.get("variables", {})
        name = options.get("name", self.default_select_name)

        generated_query = generate_query({
            "queries": [
                generate_query_data({
                    "tableName": table,
                    "returning": returning,
                    "variables": {
                        "limit": where.get("limit", None),
                        **variables,
                        "where": where,
                    }
                }),
            ],
            "name": name,
        })
        
        q = await self.client.execute_async(generated_query['query'], variable_values=generated_query['variables'])
        data = q.get("q0", [])
        del q["q0"]
        return { **q, "data": data }

    def default_returning(self, table: str) -> str:
        if table == 'links':
            return self.links_select_returning
        elif table in ['strings', 'numbers', 'objects']:
            return self.values_select_returning
        elif table == 'selectors':
            return self.selectors_select_returning
        elif table == 'files':
            return self.files_select_returning
        else:
            return "id"

    async def insert(self, objects, options=None):
        if options is None:
            options = {}
        _objects = objects if isinstance(objects, list) else [objects]
        table = options.get('table', self.table)
        returning = options.get('returning', self.insertReturning)
        variables = options.get('variables', {})
        name = options.get('name', self.defaultInsertName)
        q = {}
        try:
            q = await self.apollo_client.mutate(generate_serial({
                'actions': [insert_mutation(table, {**variables, 'objects': _objects},
                                            {'tableName': table, 'operation': 'insert', 'returning': returning})],
                'name': name
            }))
        except Exception as e:
            if 'graphQLErrors' in e and len(e['graphQLErrors']) > 0 and 'extensions' in e['graphQLErrors'][
                0] and 'internal' in e['graphQLErrors'][0]['extensions'] and 'error' in \
                    e['graphQLErrors'][0]['extensions']['internal']:
                e.message = e['graphQLErrors'][0]['extensions']['internal']['error']['message']
            if not self._silent(options):
                raise e
            return {**q, 'data': q['data']['m0']['returning'] if 'data' in q and 'm0' in q['data'] and 'returning' in
                                                                 q['data']['m0'] else None, 'error': e}

    async def update(self, exp: Union[Dict, int, List[int]], value: Dict, options: Dict = {}) -> Dict:
        if isinstance(exp, list):
            where = {"id": {"_in": exp}}
        elif isinstance(exp, dict):
            where = self.serialize_where(exp, options.get("table", self.table) if options.get("table",
                                                                                              self.table) else 'value')
        else:
            where = {"id": {"_eq": exp}}

        table = options.get("table", self.table)
        returning = options.get("returning", self.update_returning)
        variables = options.get("variables", {})
        name = options.get("name", self.default_update_name)

        try:
            generated_serial = generate_serial({
                "actions": [update_mutation(table, {**variables, "where": where, "_set": value},
                                            {"tableName": table, "operation": "update", "returning": returning})],
                "name": name,
            })

            q = await self.client.execute_async(generated_serial['query.py'],
                                                variable_values=generated_serial['variables'])
        except Exception as e:
            sql_error = e.graphQLErrors[0].extensions.internal.error if e.graphQLErrors[
                0].extensions.internal.error else None
            if sql_error and sql_error.message:
                e.message = sql_error.message
            if not self._silent(options):
                raise e
            return {**q, "data": q.get("m0", {}).get("returning", None), "error": e}

        data = q.get("m0", {}).get("returning", [])
        del q["m0"]
        return {**q, "data": data}

    async def update(self):
        raise NotImplementedError("Method not implemented")

    async def delete(self):
        raise NotImplementedError("Method not implemented")

    async def serial(self):
        raise NotImplementedError("Method not implemented")

    async def reserve(self):
        raise NotImplementedError("Method not implemented")

    async def wait_for(self):
        raise NotImplementedError("Method not implemented")

    # async def id(self, start: Union[DeepClientStartItem, BoolExpLink], *path: DeepClientPathItem) -> int:
    async def id(self, start: Any, *path: Any) -> int:
        if isinstance(start, dict):
            return (await self.select(start)).get("data")[0].get("id")
        
        if self._ids.get(start) and self._ids[start].get(path[0]):
            return self._ids[start][path[0]]
        
        q = await self.select(path_to_where(start, *path))
        if q.get("error"):
            raise Exception(q["error"])

        result = q.get("data")[0].get("id") or self._ids.get(start).get(path[0]) or 0
        if not result and path[-1] != True:
            raise Exception(f"Id not found by {json.dumps([start, *path])}")

        return result

    def id_local(self):
        raise NotImplementedError("Method not implemented")

    async def guest(self):
        raise NotImplementedError("Method not implemented")

    async def jwt(self):
        raise NotImplementedError("Method not implemented")

    async def whoami(self):
        raise NotImplementedError("Method not implemented")

    async def login(self):
        raise NotImplementedError("Method not implemented")

    async def logout(self):
        raise NotImplementedError("Method not implemented")

    async def can(self):
        raise NotImplementedError("Method not implemented")

    async def name(self):
        raise NotImplementedError("Method not implemented")

    def name_local(self):
        raise NotImplementedError("Method not implemented")
