params.inputDir = "input"
params.outputDir = "output"

Channel.fromPath("${params.inputDir}/*.bam").set{ bam_input }

log.info "~~~~~~~ demo Nextflow pipeline ~~~~~~~"
log.info "* Input Dir:          ${params.inputDir}"
log.info "* Output Dir:          ${params.outputDir}"
log.info "* Launch Dir:          ${workflow.launchDir}"
log.info "* Project dir:        ${workflow.projectDir}"
log.info "* Work Dir:            ${workflow.workDir}"
log.info "* Profile:            ${workflow.profile ?: '-'}"
log.info "* Script name:        ${workflow.scriptName ?: '-'}"
log.info "* Script ID:          ${workflow.scriptId ?: '-'}"
log.info "* Container engine:   ${workflow.containerEngine?:'-'}"
log.info "* Workflow session:   ${workflow.sessionId}"
log.info "* Nextflow run name:  ${workflow.runName}"
log.info "* Nextflow version:   ${workflow.nextflow.version}, build ${workflow.nextflow.build} (${workflow.nextflow.timestamp})"
log.info "* Launch command:\n${workflow.commandLine}\n"

process flagstat {
    publishDir "${params.outputDir}", mode: 'copy'
    input:
    file(bam) from bam_input

    output:
    file("${output_file}")

    script:
    output_file = "${bam}.txt"
    """
    samtools flagstat "${bam}" > "${output_file}"
    """
}
