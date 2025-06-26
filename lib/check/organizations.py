from typing import Any
from libprobe.asset import Asset
from ..query import query


async def check_organizations(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict[str, list[dict[str, Any]]]:
    req = '/organizations'
    resp = await query(asset, asset_config, asset_config, req)
    items: list[dict[str, Any]] = []
    for org in resp:
        licensing_model = org.get('licensing', {}).get('model')
        cloud_region = org.get('cloud', {}).get('region', {}).get('name')
        management_details = org.get('management', {}).get('details', [])

        try:
            org_id = int(org["id"])
        except Exception:
            raise Exception(
                'Organization ID is expected as integer value '
                f'(got: {org["id"]})')

        try:
            api_enabled = org['api']['enabled']
        except KeyError:
            raise Exception('Api Enabled missing in organization data')

        management_customer_number = None
        for detail in management_details:
            if detail.get('name') == 'customer number':
                try:
                    management_customer_number = int(detail.get('value'))
                except Exception:
                    pass

        items.append({
            "name": org["id"],  # str
            "id": org_id,  # int
            "url": org["url"],  # str
            "apiEnabled": api_enabled,  # bool
            "organizationName": org["name"],  # str
            "licensingModel": licensing_model,  # str?
            "cloudRegion": cloud_region,  # str?
            "managementCustomerNumber": management_customer_number,  # int?
        })

    return {"organizations": items}
