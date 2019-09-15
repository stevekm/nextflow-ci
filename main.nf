params.inputDir = "input"
params.outputDir = "output"

Channel.fromPath("${params.inputDir}/*.bam").set{ bam_input }

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
