# AUTO GENERATED FILE - DO NOT EDIT

#' @export
molecule <- function(smiles=NULL) {
    
    props <- list(smiles=smiles)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Molecule',
        namespace = 'dash_chemical_flow',
        propNames = c('smiles'),
        package = 'ChemicalFlow'
        )

    structure(component, class = c('dash_component', 'list'))
}
