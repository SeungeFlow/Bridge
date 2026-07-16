-- vocab.branch SQLite MVP schema v0.1
-- Pass 18 design only.
-- This file is a schema draft. Do not execute in pass18.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS scan_run (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_name TEXT NOT NULL,
    scanner_version TEXT NOT NULL,
    repo_9dot0_commit TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    scope_note TEXT NOT NULL,
    is_whole_repo_scan INTEGER NOT NULL DEFAULT 0,
    is_db_build INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS source_file (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    repo TEXT NOT NULL,
    branch TEXT NOT NULL,
    commit_hash TEXT NOT NULL,
    path TEXT NOT NULL,
    raw_url TEXT NOT NULL,
    source_status TEXT NOT NULL DEFAULT 'source_identity_candidate',
    file_role TEXT NOT NULL,
    UNIQUE(repo, commit_hash, path)
);

CREATE TABLE IF NOT EXISTS readme_source (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file_id INTEGER NOT NULL,
    baseline_order INTEGER,
    baseline_class TEXT NOT NULL,
    note TEXT,
    FOREIGN KEY(source_file_id) REFERENCES source_file(id)
);

CREATE TABLE IF NOT EXISTS vocab_term (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    term TEXT NOT NULL,
    normalized_term TEXT NOT NULL,
    surface_language TEXT DEFAULT 'unknown',
    term_kind TEXT DEFAULT 'raw_candidate',
    is_readme_vocab INTEGER NOT NULL DEFAULT 1,
    is_structural_trigger INTEGER NOT NULL DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(normalized_term)
);

CREATE TABLE IF NOT EXISTS term_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    term_id INTEGER NOT NULL,
    status TEXT NOT NULL,
    score INTEGER DEFAULT 0,
    status_source TEXT NOT NULL,
    note TEXT,
    FOREIGN KEY(term_id) REFERENCES vocab_term(id)
);

CREATE TABLE IF NOT EXISTS term_occurrence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scan_run_id INTEGER NOT NULL,
    term_id INTEGER NOT NULL,
    source_file_id INTEGER NOT NULL,
    line_no INTEGER NOT NULL,
    context TEXT,
    occurrence_status TEXT NOT NULL DEFAULT 'raw_occurrence',
    FOREIGN KEY(scan_run_id) REFERENCES scan_run(id),
    FOREIGN KEY(term_id) REFERENCES vocab_term(id),
    FOREIGN KEY(source_file_id) REFERENCES source_file(id)
);

CREATE TABLE IF NOT EXISTS raw_url_index (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file_id INTEGER NOT NULL,
    raw_url TEXT NOT NULL,
    raw_url_line_anchor TEXT,
    access_status TEXT DEFAULT 'candidate',
    FOREIGN KEY(source_file_id) REFERENCES source_file(id)
);

CREATE TABLE IF NOT EXISTS term_relation_candidate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_term_id INTEGER NOT NULL,
    to_term_id INTEGER NOT NULL,
    relation_type TEXT NOT NULL DEFAULT 'candidate_relation',
    evidence_source_file_id INTEGER,
    guard_status TEXT NOT NULL DEFAULT 'not_final_judgment',
    note TEXT,
    FOREIGN KEY(from_term_id) REFERENCES vocab_term(id),
    FOREIGN KEY(to_term_id) REFERENCES vocab_term(id),
    FOREIGN KEY(evidence_source_file_id) REFERENCES source_file(id)
);

CREATE TABLE IF NOT EXISTS term_card_candidate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    term_id INTEGER NOT NULL,
    candidate_slug TEXT NOT NULL,
    candidate_path TEXT,
    reason TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'candidate',
    FOREIGN KEY(term_id) REFERENCES vocab_term(id)
);

CREATE TABLE IF NOT EXISTS reader_query_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query_text TEXT NOT NULL,
    query_term TEXT,
    selected_source_file_id INTEGER,
    result_note TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(selected_source_file_id) REFERENCES source_file(id)
);

CREATE INDEX IF NOT EXISTS idx_source_file_repo_branch ON source_file(repo, branch);
CREATE INDEX IF NOT EXISTS idx_source_file_commit_path ON source_file(commit_hash, path);
CREATE INDEX IF NOT EXISTS idx_vocab_term_normalized ON vocab_term(normalized_term);
CREATE INDEX IF NOT EXISTS idx_term_occurrence_term ON term_occurrence(term_id);
CREATE INDEX IF NOT EXISTS idx_term_occurrence_source ON term_occurrence(source_file_id);
CREATE INDEX IF NOT EXISTS idx_term_status_term ON term_status(term_id);
CREATE INDEX IF NOT EXISTS idx_term_relation_from ON term_relation_candidate(from_term_id);
CREATE INDEX IF NOT EXISTS idx_term_relation_to ON term_relation_candidate(to_term_id);
