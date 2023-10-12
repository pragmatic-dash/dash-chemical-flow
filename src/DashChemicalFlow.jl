
module DashChemicalFlow
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/dashchemicalflow.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_chemical_flow",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "async-DashChemicalFlow.js",
    external_url = "https://unpkg.com/dash_chemical_flow@0.0.1/dash_chemical_flow/async-DashChemicalFlow.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DashChemicalFlow.js.map",
    external_url = "https://unpkg.com/dash_chemical_flow@0.0.1/dash_chemical_flow/async-DashChemicalFlow.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_chemical_flow.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_chemical_flow.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
