import IPython; from IPython.config.loader import Config; cfg = Config(); cfg.InteractiveShellEmbed.local_ns = locals(); cfg.InteractiveShellEmbed.global_ns = globals(); IPython.embed(config=cfg)
