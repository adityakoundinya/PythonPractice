from wayml.python_client.wayml_client_async import WayMLClientAsync
import asyncio
from os import environ

environ["GRPC_DNS_RESOLVER"] = "native"
handler_name = "CustomerScoreUnifiedModelV2Handler"
k8s_ingress_dev = "kube-sweetwater-customer-score-unified-model--v2-grpc.service.intradsm1.sdeconsul.csnzoo.com"
k8s_ingress_prod = "kube-sweetwater-customer-score-unified-model--v2-grpc.service.intraiad1.consul.csnzoo.com"


async def call_server_async():
    # client = await WayMLClientAsync.get_instance(handler_name, "localhost:50051")
    # client = await WayMLClientAsync.get_instance(handler_name, k8s_ingress_dev)  # dev client
    client = await WayMLClientAsync.get_instance(handler_name, k8s_ingress_prod)  # prod client
    model_input = {"customer_guid": "cccccccc-ffff-eeee-fecd-000000000101",
                   "device_guids": [
                       "23e17d3a-60d1-546a-820c-11a9c61ec702",
                       "45e156na-34d6-646z-920f-56a9c61ec922",
                   ],
                   "requested_models": [
                       {"model": "unified_customer_30day_intent",
                           "model_version": "v2"},
                       {"model": "unified_customer_30day_GRS", "model_version": "v2"},
                       {"model": "unified_customer_direct_intent",
                           "model_version": "v2"},
                       {"model": "unified_customer_direct_GRS",
                           "model_version": "v2"},
                   ],
                   }  # example input data
    response = await client.evaluate(model_input)
    print(f'prediction response: {response}')

asyncio.run(call_server_async())
